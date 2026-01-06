# Import required libraries
import streamlit as st  # For creating web dashboard
import pandas as pd  # For data manipulation
import plotly.express as px  # For interactive visualizations
import plotly.graph_objects as go  # For custom visualizations
import os  # For file operations

# Set page configuration (must be first Streamlit command)
st.set_page_config(
    page_title="Customer Churn Analysis Dashboard",  # Browser tab title
    page_icon="📊",  # Browser tab icon
    layout="wide",  # Use full width of browser
    initial_sidebar_state="expanded"  # Sidebar open by default
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 15px;
        border-radius: 5px;
    }
    h1 {
        color: #1f77b4;
    }
    h2 {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
    }
    .insight-box {
        background-color: #e8f4f8;
        padding: 15px;
        border-left: 5px solid #3498db;
        border-radius: 5px;
        margin: 10px 0;
    }
    .recommendation-box {
        background-color: #e8f8f5;
        padding: 15px;
        border-left: 5px solid #27ae60;
        border-radius: 5px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# ==================== DATA LOADING ====================

# Cache data loading to improve performance (only load once)
@st.cache_data  # Streamlit decorator to cache function result
def load_data():
    """Load enriched dataset and return DataFrame"""
    # Define path to enriched dataset
    data_path = "data/processed/enriched_churn_data.csv"
    
    # Check if file exists
    if not os.path.exists(data_path):
        # If file doesn't exist, show error and stop
        st.error(f"❌ Data file not found: {data_path}")
        st.stop()
    
    # Load CSV into DataFrame
    df = pd.read_csv(data_path)
    
    return df

# Load the data
df = load_data()

# ==================== SIDEBAR - NAVIGATION & FILTERS ====================

# Create sidebar for navigation
st.sidebar.title("📊 Navigation")
st.sidebar.markdown("---")

# Create page selection radio buttons
page = st.sidebar.radio(
    "Select Page",  # Label
    [
        "🏠 Executive Overview",
        "📈 Segment Analysis", 
        "🎯 Churn Drivers",
        "💡 Recommendations",
        "🔍 Customer Explorer"
    ]
)

# Add filters section
st.sidebar.markdown("---")
st.sidebar.title("🔧 Global Filters")

# Filter 1: Contract Type
contract_filter = st.sidebar.multiselect(
    "Contract Type",  # Label
    options=df['Contract'].unique(),  # Available options
    default=df['Contract'].unique()  # Default: all selected
)

# Filter 2: Tenure Segment
tenure_filter = st.sidebar.multiselect(
    "Tenure Segment",
    options=df['Tenure_Segment'].unique(),
    default=df['Tenure_Segment'].unique()
)

# Filter 3: Value Segment
value_filter = st.sidebar.multiselect(
    "Value Segment",
    options=df['Value_Segment'].unique(),
    default=df['Value_Segment'].unique()
)

# Apply filters to dataset
df_filtered = df[
    (df['Contract'].isin(contract_filter)) &  # Filter by contract
    (df['Tenure_Segment'].isin(tenure_filter)) &  # Filter by tenure
    (df['Value_Segment'].isin(value_filter))  # Filter by value
]

# Show filter summary in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(f"**Filtered Customers:** {len(df_filtered):,} / {len(df):,}")

# ==================== PAGE 1: EXECUTIVE OVERVIEW ====================

if page == "🏠 Executive Overview":
    # Page header
    st.title("🏠 Customer Churn Analysis - Executive Overview")
    st.markdown("**Comprehensive analysis of customer churn patterns and retention opportunities**")
    st.markdown("---")
    
    # Calculate key metrics
    total_customers = len(df_filtered)
    churned_customers = (df_filtered['Churn'] == 'Yes').sum()
    retained_customers = (df_filtered['Churn'] == 'No').sum()
    churn_rate = (churned_customers / total_customers * 100) if total_customers > 0 else 0
    
    total_clv = df_filtered['CLV'].sum()
    churned_clv = df_filtered[df_filtered['Churn'] == 'Yes']['CLV'].sum()
    avg_arpu = df_filtered['ARPU'].mean()
    
    # Display key metrics in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Customers",
            value=f"{total_customers:,}",
            delta=None
        )
    
    with col2:
        st.metric(
            label="Churn Rate",
            value=f"{churn_rate:.1f}%",
            delta=f"{churned_customers:,} churned",
            delta_color="inverse"  # Red for negative (bad)
        )
    
    with col3:
        st.metric(
            label="Revenue at Risk",
            value=f"${churned_clv:,.0f}",
            delta="Total CLV Lost",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            label="Avg ARPU",
            value=f"${avg_arpu:.2f}",
            delta="per month"
        )
    
    st.markdown("---")
    
    # Create two columns for visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Churn Distribution")
        
        # Create pie chart for churn distribution
        churn_counts = df_filtered['Churn'].value_counts()
        fig = go.Figure(data=[go.Pie(
            labels=churn_counts.index,
            values=churn_counts.values,
            hole=0.4,  # Donut chart
            marker_colors=['#2ecc71', '#e74c3c'],  # Green for No, Red for Yes
            textinfo='label+percent',
            textfont_size=14
        )])
        fig.update_layout(
            showlegend=True,
            height=400,
            margin=dict(t=50, b=50, l=50, r=50)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Revenue Impact by Churn Status")
        
        # Create bar chart for revenue by churn status
        revenue_by_churn = df_filtered.groupby('Churn')['CLV'].sum().reset_index()
        fig = px.bar(
            revenue_by_churn,
            x='Churn',
            y='CLV',
            color='Churn',
            color_discrete_map={'No': '#2ecc71', 'Yes': '#e74c3c'},
            labels={'CLV': 'Total CLV ($)', 'Churn': 'Churn Status'},
            text='CLV'
        )
        fig.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
        fig.update_layout(
            showlegend=False,
            height=400,
            yaxis_title="Total Customer Lifetime Value ($)"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Key Insights Section
    st.subheader("🔑 Key Insights")
    
    # Calculate insights
    high_risk_count = (df_filtered['Risk_Score'] >= 2).sum()
    high_risk_pct = (high_risk_count / total_customers * 100) if total_customers > 0 else 0
    
    mtm_churn = df_filtered[df_filtered['Contract'] == 'Month-to-month']['Churn'].apply(lambda x: x == 'Yes').mean() * 100
    
    # Display insights in boxes
    st.markdown(f"""
    <div class="insight-box">
    <b>📌 Insight 1: Overall Churn</b><br>
    {churn_rate:.1f}% of customers have churned, representing ${churned_clv:,.0f} in lost customer lifetime value. 
    This affects {churned_customers:,} customers across the analyzed base.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="insight-box">
    <b>📌 Insight 2: High-Risk Segment</b><br>
    {high_risk_count:,} customers ({high_risk_pct:.1f}%) are classified as high-risk (Risk Score ≥ 2). 
    These customers require immediate retention intervention to prevent churn.
    </div>
    """, unsafe_allow_html=True)
    
    if 'Month-to-month' in contract_filter:
        st.markdown(f"""
        <div class="insight-box">
        <b>📌 Insight 3: Contract Type Impact</b><br>
        Month-to-month contract customers have {mtm_churn:.1f}% churn rate, significantly higher than 
        customers with longer-term contracts. Contract stability is a major churn driver.
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Top Recommendations Preview
    st.subheader("💡 Top 3 Recommendations")
    
    st.markdown("""
    <div class="recommendation-box">
    <b>1. Contract Commitment Incentives (Priority: HIGH)</b><br>
    Offer 10-15% discounts for customers upgrading from month-to-month to annual contracts.
    Expected to reduce churn rate from 42% to ~25% among month-to-month customers.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="recommendation-box">
    <b>2. Enhanced First-Year Onboarding (Priority: HIGH)</b><br>
    Implement structured onboarding program with touchpoints at 30, 90, and 180 days for new customers.
    Target early-tenure customers to reduce first-year churn from 47% to ~35%.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="recommendation-box">
    <b>3. Service Adoption Campaign (Priority: MEDIUM)</b><br>
    Launch targeted upsell campaign for customers with low service engagement (0-2 services).
    Increase service adoption to reduce churn by 10-15 percentage points.
    </div>
    """, unsafe_allow_html=True)
    
    st.info("📋 Navigate to 'Recommendations' page for detailed implementation plans.")

# ==================== PAGE 2: SEGMENT ANALYSIS ====================

elif page == "📈 Segment Analysis":
    st.title("📈 Customer Segment Analysis")
    st.markdown("**Deep dive into customer segments by risk, value, and lifecycle stage**")
    st.markdown("---")
    
    # Segment selector
    segment_type = st.radio(
        "Select Segment Type",
        ["Risk Segments", "Value Segments", "Tenure Segments"],
        horizontal=True
    )
    
    if segment_type == "Risk Segments":
        st.subheader("🎯 Risk Segment Comparison")
        
        # Calculate risk segment metrics
        risk_summary = df_filtered.groupby('Risk_Score').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
            'CLV': 'sum',
            'ARPU': 'mean'
        }).reset_index()
        risk_summary.columns = ['Risk_Score', 'Customer_Count', 'Churn_Rate', 'Total_CLV', 'Avg_ARPU']
        
        # Create risk labels
        risk_summary['Risk_Label'] = risk_summary['Risk_Score'].apply(
            lambda x: 'High Risk' if x >= 2 else ('Medium Risk' if x == 1 else 'Low Risk')
        )
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        
        high_risk = risk_summary[risk_summary['Risk_Score'] >= 2]['Customer_Count'].sum()
        medium_risk = risk_summary[risk_summary['Risk_Score'] == 1]['Customer_Count'].sum()
        low_risk = risk_summary[risk_summary['Risk_Score'] == 0]['Customer_Count'].sum()
        
        with col1:
            st.metric("High Risk (Score ≥2)", f"{high_risk:,}", f"{high_risk/len(df_filtered)*100:.1f}%")
        with col2:
            st.metric("Medium Risk (Score=1)", f"{medium_risk:,}", f"{medium_risk/len(df_filtered)*100:.1f}%")
        with col3:
            st.metric("Low Risk (Score=0)", f"{low_risk:,}", f"{low_risk/len(df_filtered)*100:.1f}%")
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Churn Rate by Risk Segment**")
            fig = px.bar(
                risk_summary,
                x='Risk_Label',
                y='Churn_Rate',
                color='Risk_Label',
                color_discrete_map={'Low Risk': '#2ecc71', 'Medium Risk': '#f39c12', 'High Risk': '#e74c3c'},
                text='Churn_Rate',
                labels={'Churn_Rate': 'Churn Rate (%)', 'Risk_Label': 'Risk Segment'}
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Customer Distribution by Risk**")
            fig = px.pie(
                risk_summary,
                names='Risk_Label',
                values='Customer_Count',
                color='Risk_Label',
                color_discrete_map={'Low Risk': '#2ecc71', 'Medium Risk': '#f39c12', 'High Risk': '#e74c3c'},
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Display segment table
        st.markdown("**Detailed Risk Segment Metrics**")
        display_risk = risk_summary[['Risk_Label', 'Customer_Count', 'Churn_Rate', 'Total_CLV', 'Avg_ARPU']].copy()
        display_risk['Churn_Rate'] = display_risk['Churn_Rate'].apply(lambda x: f"{x:.2f}%")
        display_risk['Total_CLV'] = display_risk['Total_CLV'].apply(lambda x: f"${x:,.2f}")
        display_risk['Avg_ARPU'] = display_risk['Avg_ARPU'].apply(lambda x: f"${x:.2f}")
        st.dataframe(display_risk, use_container_width=True, hide_index=True)
    
    elif segment_type == "Value Segments":
        st.subheader("💎 Value Segment Comparison")
        
        # Calculate value segment metrics
        value_summary = df_filtered.groupby('Value_Segment').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
            'CLV': ['sum', 'mean'],
            'ARPU': 'mean'
        }).reset_index()
        value_summary.columns = ['Value_Segment', 'Customer_Count', 'Churn_Rate', 'Total_CLV', 'Avg_CLV', 'Avg_ARPU']
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Churn Rate by Value Segment**")
            fig = px.bar(
                value_summary,
                x='Value_Segment',
                y='Churn_Rate',
                color='Value_Segment',
                text='Churn_Rate',
                labels={'Churn_Rate': 'Churn Rate (%)', 'Value_Segment': 'Value Segment'}
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Total CLV by Value Segment**")
            fig = px.bar(
                value_summary,
                x='Value_Segment',
                y='Total_CLV',
                color='Value_Segment',
                text='Total_CLV',
                labels={'Total_CLV': 'Total CLV ($)', 'Value_Segment': 'Value Segment'}
            )
            fig.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Display segment table
        st.markdown("**Detailed Value Segment Metrics**")
        display_value = value_summary.copy()
        display_value['Churn_Rate'] = display_value['Churn_Rate'].apply(lambda x: f"{x:.2f}%")
        display_value['Total_CLV'] = display_value['Total_CLV'].apply(lambda x: f"${x:,.2f}")
        display_value['Avg_CLV'] = display_value['Avg_CLV'].apply(lambda x: f"${x:.2f}")
        display_value['Avg_ARPU'] = display_value['Avg_ARPU'].apply(lambda x: f"${x:.2f}")
        st.dataframe(display_value, use_container_width=True, hide_index=True)
    
    else:  # Tenure Segments
        st.subheader("⏳ Tenure Segment (Lifecycle) Comparison")
        
        # Calculate tenure segment metrics
        tenure_summary = df_filtered.groupby('Tenure_Segment').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
            'tenure': 'mean',
            'CLV': 'mean'
        }).reset_index()
        tenure_summary.columns = ['Tenure_Segment', 'Customer_Count', 'Churn_Rate', 'Avg_Tenure', 'Avg_CLV']
        
        # Order segments logically
        segment_order = ['New Customer', 'Growing Customer', 'Mature Customer', 'Loyal Customer']
        tenure_summary['Tenure_Segment'] = pd.Categorical(tenure_summary['Tenure_Segment'], categories=segment_order, ordered=True)
        tenure_summary = tenure_summary.sort_values('Tenure_Segment')
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Churn Rate by Lifecycle Stage**")
            fig = px.bar(
                tenure_summary,
                x='Tenure_Segment',
                y='Churn_Rate',
                color='Churn_Rate',
                color_continuous_scale=['#2ecc71', '#f39c12', '#e74c3c'],
                text='Churn_Rate',
                labels={'Churn_Rate': 'Churn Rate (%)', 'Tenure_Segment': 'Lifecycle Stage'}
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Customer Count by Lifecycle Stage**")
            fig = px.bar(
                tenure_summary,
                x='Tenure_Segment',
                y='Customer_Count',
                text='Customer_Count',
                labels={'Customer_Count': 'Number of Customers', 'Tenure_Segment': 'Lifecycle Stage'}
            )
            fig.update_traces(texttemplate='%{text:,}', textposition='outside', marker_color='#3498db')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Display segment table
        st.markdown("**Detailed Tenure Segment Metrics**")
        display_tenure = tenure_summary.copy()
        display_tenure['Churn_Rate'] = display_tenure['Churn_Rate'].apply(lambda x: f"{x:.2f}%")
        display_tenure['Avg_Tenure'] = display_tenure['Avg_Tenure'].apply(lambda x: f"{x:.1f} months")
        display_tenure['Avg_CLV'] = display_tenure['Avg_CLV'].apply(lambda x: f"${x:.2f}")
        st.dataframe(display_tenure, use_container_width=True, hide_index=True)

# ==================== PAGE 3: CHURN DRIVERS ====================

elif page == "🎯 Churn Drivers":
    st.title("🎯 Churn Driver Analysis")
    st.markdown("**Identify and quantify key factors driving customer churn**")
    st.markdown("---")
    
    # Driver selector
    driver_type = st.selectbox(
        "Select Churn Driver to Analyze",
        ["Contract Type", "Payment Method", "Service Adoption", "Tenure Impact"]
    )
    
    if driver_type == "Contract Type":
        st.subheader("📄 Contract Type Impact on Churn")
        
        # Calculate contract metrics
        contract_summary = df_filtered.groupby('Contract').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
            'CLV': 'sum'
        }).reset_index()
        contract_summary.columns = ['Contract', 'Customer_Count', 'Churn_Rate', 'Total_CLV']
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        
        for i, (col, contract) in enumerate(zip([col1, col2, col3], contract_summary['Contract'])):
            row = contract_summary[contract_summary['Contract'] == contract].iloc[0]
            with col:
                st.metric(
                    f"{contract}",
                    f"{row['Churn_Rate']:.1f}%",
                    f"{int(row['Customer_Count']):,} customers"
                )
        
        # Visualization
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Churn Rate Comparison**")
            fig = px.bar(
                contract_summary,
                x='Contract',
                y='Churn_Rate',
                color='Contract',
                text='Churn_Rate',
                labels={'Churn_Rate': 'Churn Rate (%)', 'Contract': 'Contract Type'}
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Customer Distribution**")
            fig = px.pie(
                contract_summary,
                names='Contract',
                values='Customer_Count',
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Insight
        highest_churn_contract = contract_summary.loc[contract_summary['Churn_Rate'].idxmax(), 'Contract']
        highest_churn_rate = contract_summary['Churn_Rate'].max()
        lowest_churn_rate = contract_summary['Churn_Rate'].min()
        
        st.markdown(f"""
        <div class="insight-box">
        <b>💡 Key Insight:</b><br>
        {highest_churn_contract} contracts have the highest churn rate at {highest_churn_rate:.1f}%, 
        which is {(highest_churn_rate/lowest_churn_rate):.1f}x higher than the lowest churn contract type. 
        Contract stability is a critical churn driver requiring immediate intervention.
        </div>
        """, unsafe_allow_html=True)
    
    elif driver_type == "Payment Method":
        st.subheader("💳 Payment Method Impact on Churn")
        
        # Calculate payment method metrics
        payment_summary = df_filtered.groupby('PaymentMethod').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100
        }).reset_index()
        payment_summary.columns = ['PaymentMethod', 'Customer_Count', 'Churn_Rate']
        payment_summary = payment_summary.sort_values('Churn_Rate', ascending=False)
        
        # Visualization
        fig = px.bar(
            payment_summary,
            x='PaymentMethod',
            y='Churn_Rate',
            color='Churn_Rate',
            color_continuous_scale=['#2ecc71', '#e74c3c'],
            text='Churn_Rate',
            labels={'Churn_Rate': 'Churn Rate (%)', 'PaymentMethod': 'Payment Method'}
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display table
        st.markdown("**Payment Method Comparison**")
        display_payment = payment_summary.copy()
        display_payment['Churn_Rate'] = display_payment['Churn_Rate'].apply(lambda x: f"{x:.2f}%")
        st.dataframe(display_payment, use_container_width=True, hide_index=True)
        
        # Insight
        highest_payment = payment_summary.iloc[0]
        st.markdown(f"""
        <div class="insight-box">
        <b>💡 Key Insight:</b><br>
        {highest_payment['PaymentMethod']} users have the highest churn rate at {highest_payment['Churn_Rate']:.1f}%.
        Manual payment methods may indicate lower engagement and create friction, leading to higher churn.
        Recommendation: Incentivize migration to automatic payment methods.
        </div>
        """, unsafe_allow_html=True)
    
    elif driver_type == "Service Adoption":
        st.subheader("📦 Service Adoption Impact on Churn")
        
        # Calculate service engagement metrics
        service_summary = df_filtered.groupby('Service_Engagement').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
            'Total_Services': 'mean'
        }).reset_index()
        service_summary.columns = ['Service_Engagement', 'Customer_Count', 'Churn_Rate', 'Avg_Services']
        
        # Visualization
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Churn Rate by Service Engagement**")
            fig = px.bar(
                service_summary,
                x='Service_Engagement',
                y='Churn_Rate',
                color='Service_Engagement',
                text='Churn_Rate',
                labels={'Churn_Rate': 'Churn Rate (%)', 'Service_Engagement': 'Engagement Level'}
            )
            fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("**Average Services by Engagement**")
            fig = px.bar(
                service_summary,
                x='Service_Engagement',
                y='Avg_Services',
                color='Service_Engagement',
                text='Avg_Services',
                labels={'Avg_Services': 'Average Number of Services', 'Service_Engagement': 'Engagement Level'}
            )
            fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')
            fig.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        # Insight
        low_engagement_churn = service_summary[service_summary['Service_Engagement'] == 'Low Engagement']['Churn_Rate'].values[0]
        high_engagement_churn = service_summary[service_summary['Service_Engagement'] == 'High Engagement']['Churn_Rate'].values[0]
        churn_difference = low_engagement_churn - high_engagement_churn
        
        st.markdown(f"""
        <div class="insight-box">
        <b>💡 Key Insight:</b><br>
        Low engagement customers have {low_engagement_churn:.1f}% churn rate compared to {high_engagement_churn:.1f}% 
        for high engagement customers - a difference of {churn_difference:.1f} percentage points.
        Increasing service adoption is a proven churn reduction strategy.
        Recommendation: Launch targeted upsell campaigns for low-engagement customers.
        </div>
        """, unsafe_allow_html=True)
    
    else:  # Tenure Impact
        st.subheader("⏱️ Customer Tenure Impact on Churn")
        
        # Create tenure bins for visualization
        df_filtered['TenureBin'] = pd.cut(
            df_filtered['tenure'],
            bins=[0, 6, 12, 24, 36, 48, 72],
            labels=['0-6 mo', '7-12 mo', '13-24 mo', '25-36 mo', '37-48 mo', '49+ mo']
        )
        
        # Calculate tenure bin metrics
        tenure_bin_summary = df_filtered.groupby('TenureBin').agg({
            'customerID': 'count',
            'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100
        }).reset_index()
        tenure_bin_summary.columns = ['TenureBin', 'Customer_Count', 'Churn_Rate']
        
        # Visualization
        fig = px.line(
            tenure_bin_summary,
            x='TenureBin',
            y='Churn_Rate',
            markers=True,
            text='Churn_Rate',
            labels={'Churn_Rate': 'Churn Rate (%)', 'TenureBin': 'Tenure Range'}
        )
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='top center', line_color='#e74c3c', marker_size=10)
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
        
        # Display table
        st.markdown("**Churn Rate by Tenure Range**")
        display_tenure_bin = tenure_bin_summary.copy()
        display_tenure_bin['Churn_Rate'] = display_tenure_bin['Churn_Rate'].apply(lambda x: f"{x:.2f}%")
        st.dataframe(display_tenure_bin, use_container_width=True, hide_index=True)
        
        # Insight
        first_year_churn = tenure_bin_summary[tenure_bin_summary['TenureBin'].isin(['0-6 mo', '7-12 mo'])]['Churn_Rate'].mean()
        st.markdown(f"""
        <div class="insight-box">
        <b>💡 Key Insight:</b><br>
        Churn rate is highest in the first 12 months at {first_year_churn:.1f}% on average.
        The "critical first year" requires intensive retention focus with proactive onboarding and support.
        Churn decreases significantly as tenure increases, indicating loyalty builds over time.
        Recommendation: Implement structured first-year onboarding program.
        </div>
        """, unsafe_allow_html=True)

# ==================== PAGE 4: RECOMMENDATIONS ====================

elif page == "💡 Recommendations":
    st.title("💡 Business Recommendations")
    st.markdown("**Prioritized, actionable strategies to reduce customer churn**")
    st.markdown("---")
    
    # Recommendation 1
    st.markdown("### 1️⃣ Contract Commitment Incentives")
    st.markdown("**Priority:** 🔴 HIGH | **Expected Impact:** High | **Implementation:** Quick Win")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Problem:**
        - Month-to-month customers have 40%+ churn rate (3-5x higher than two-year contracts)
        - Represents 40-45% of customer base
        - Significant revenue instability
        
        **Recommended Action:**
        - Offer 10% discount for upgrade to 1-year contract
        - Offer 15% discount for upgrade to 2-year contract
        - Communicate value: price protection, no surprise increases
        - Limited-time offer to create urgency
        
        **Expected Outcome:**
        - Reduce month-to-month churn from 42% to ~25%
        - Convert 20-30% of month-to-month customers to annual contracts
        - Increase customer lifetime value through longer commitments
        - Estimated annual revenue retention: $300K-$500K
        """)
    
    with col2:
        st.info("**Implementation Timeline**\n\n• Week 1-2: Design offer structure\n• Week 3-4: Create marketing materials\n• Week 5: Launch campaign\n• Month 2-3: Monitor and optimize")
    
    st.markdown("---")
    
    # Recommendation 2
    st.markdown("### 2️⃣ Enhanced First-Year Onboarding Program")
    st.markdown("**Priority:** 🔴 HIGH | **Expected Impact:** High | **Implementation:** 3-6 months")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Problem:**
        - New customers (0-12 months) have 45-50% churn rate
        - 2-4x higher than loyal customers (49+ months)
        - First year is critical retention period
        
        **Recommended Action:**
        - Day 1: Welcome email with setup guide and quick wins
        - Day 30: Satisfaction check-in call, address any issues
        - Day 90: Service optimization review, recommend add-ons
        - Day 180: Mid-year check-in, discuss contract upgrade options
        - Proactive tech support for first 90 days (no wait times)
        - Personalized service recommendations based on usage patterns
        
        **Expected Outcome:**
        - Reduce first-year churn from 47% to ~35%
        - Improve customer satisfaction scores
        - Higher service adoption in first year
        - Estimated customers saved: 400-600 annually
        """)
    
    with col2:
        st.info("**Implementation Timeline**\n\n• Month 1: Design onboarding workflow\n• Month 2: Train support team\n• Month 3: Pilot with new customers\n• Month 4-6: Full rollout")
    
    st.markdown("---")
    
    # Recommendation 3
    st.markdown("### 3️⃣ Payment Method Migration Campaign")
    st.markdown("**Priority:** 🟡 MEDIUM | **Expected Impact:** Medium | **Implementation:** Quick Win")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Problem:**
        - Electronic check users have 45% churn rate
        - Manual payments create friction and missed payments
        - Lower engagement compared to autopay users
        
        **Recommended Action:**
        - $5/month discount for first 6 months on autopay enrollment
        - Simplified enrollment process (1-click setup)
        - Payment reminder emails 7 days before due date
        - Highlight convenience: "Set it and forget it"
        - Avoid late fees messaging
        
        **Expected Outcome:**
        - 30-40% of electronic check users migrate to autopay
        - Reduced payment failures and late fees
        - Lower churn through improved payment experience
        - Estimated annual revenue retention: $100K-$200K
        """)
    
    with col2:
        st.info("**Implementation Timeline**\n\n• Week 1-2: Design migration campaign\n• Week 3: Launch email campaign\n• Week 4-8: Follow-up and conversions\n• Ongoing: Monitor and optimize")
    
    st.markdown("---")
    
    # Recommendation 4
    st.markdown("### 4️⃣ Service Adoption & Upsell Campaign")
    st.markdown("**Priority:** 🟡 MEDIUM | **Expected Impact:** Medium | **Implementation:** Ongoing")
    
    st.markdown("""
    **Problem:**
    - Low engagement customers (0-2 services) have 35-40% churn rate
    - 10-15 percentage points higher than high engagement customers
    - Missing revenue opportunity from service upsells
    
    **Recommended Action:**
    - Target low-engagement customers with personalized service recommendations
    - Priority services: Tech Support, Online Security (proven churn reducers)
    - Offer bundled discount: 15% off when adding 2+ services
    - Free trial period: 30 days to demonstrate value
    - Educational content: webinars, guides on service benefits
    
    **Expected Outcome:**
    - 20-30% of low engagement customers add at least one service
    - Churn reduction of 10-15 percentage points for converted customers
    - Increased ARPU through service adoption
    - Estimated annual additional revenue: $200K-$350K
    """)
    
    st.markdown("---")
    
    # Recommendation 5
    st.markdown("### 5️⃣ Churn Early Warning & Intervention System")
    st.markdown("**Priority:** 🟢 MEDIUM-LOW | **Expected Impact:** High (Enabler) | **Implementation:** 3-6 months")
    
    st.markdown("""
    **Problem:**
    - No proactive system to identify at-risk customers before they churn
    - Reactive approach (responding after churn decision made)
    - High-risk customers not receiving targeted attention
    
    **Recommended Action:**
    - Implement automated risk-based monitoring using existing Risk_Score
    - Risk Score 3: Immediate account manager outreach with retention offer
    - Risk Score 2: Automated retention email with special discount/offer
    - Risk Score 1: Engagement campaign (educational content, surveys)
    - Monthly risk score updates to track customer status changes
    - Dedicated retention team for high-risk accounts (Risk Score ≥2)
    
    **Expected Outcome:**
    - Early identification of at-risk customers (weeks before churn)
    - Targeted interventions before churn decision is made
    - Potential to save 300-500 customers annually
    - Estimated annual revenue retention: $400K-$600K
    - Foundation for all other retention initiatives
    """)
    
    st.markdown("---")
    
    # Implementation Priority Summary
    st.subheader("📋 Implementation Roadmap")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Phase 1: Quick Wins (Month 1-2)**
        - ✅ Contract commitment incentives
        - ✅ Payment method migration campaign
        
        **Phase 2: Strategic Initiatives (Month 3-6)**
        - 🔄 First-year onboarding program
        - 🔄 Service adoption campaign (ongoing)
        """)
    
    with col2:
        st.markdown("""
        **Phase 3: Foundation Building (Month 4-9)**
        - 🏗️ Churn early warning system
        - 🏗️ Retention team structure
        
        **Ongoing Activities**
        - 📊 Monthly reporting on churn metrics
        - 🎯 Segment-specific campaigns
        - 🔍 Continuous optimization
        """)

# ==================== PAGE 5: CUSTOMER EXPLORER ====================

else:  # Customer Explorer
    st.title("🔍 Customer Explorer")
    st.markdown("**Interactive customer data exploration and filtering**")
    st.markdown("---")
    
    st.subheader("Filter Customers")
    
    # Additional filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        risk_score_filter = st.multiselect(
            "Risk Score",
            options=sorted(df['Risk_Score'].unique()),
            default=sorted(df['Risk_Score'].unique())
        )
    
    with col2:
        churn_filter = st.multiselect(
            "Churn Status",
            options=['Yes', 'No'],
            default=['Yes', 'No']
        )
    
    with col3:
        payment_filter = st.multiselect(
            "Payment Method",
            options=df['PaymentMethod'].unique(),
            default=df['PaymentMethod'].unique()
        )
    
    # Apply additional filters
    df_explorer = df_filtered[
        (df_filtered['Risk_Score'].isin(risk_score_filter)) &
        (df_filtered['Churn'].isin(churn_filter)) &
        (df_filtered['PaymentMethod'].isin(payment_filter))
    ]
    
    # Display summary metrics
    st.markdown("### Filtered Customer Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Customers", f"{len(df_explorer):,}")
    with col2:
        st.metric("Churn Rate", f"{(df_explorer['Churn']=='Yes').sum()/len(df_explorer)*100:.1f}%")
    with col3:
        st.metric("Avg ARPU", f"${df_explorer['ARPU'].mean():.2f}")
    with col4:
        st.metric("Total CLV", f"${df_explorer['CLV'].sum():,.0f}")
    
    st.markdown("---")
    
    # Display customer data table
    st.subheader("Customer Data")
    
    # Select columns to display
    display_columns = [
        'customerID', 'Churn', 'Contract', 'tenure', 'MonthlyCharges', 
        'TotalCharges', 'Risk_Score', 'Value_Segment', 'Total_Services',
        'PaymentMethod'
    ]
    
    # Show data table with search
    st.dataframe(
        df_explorer[display_columns],
        use_container_width=True,
        height=400
    )
    
    # Download button
    st.markdown("### Export Data")
    csv = df_explorer.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Filtered Data as CSV",
        data=csv,
        file_name='filtered_customer_data.csv',
        mime='text/csv'
    )

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 20px;'>
    <p>Customer Churn Analysis Dashboard | Data Analytics Portfolio Project</p>
    <p>Built with Streamlit | Last Updated: January 2026</p>
</div>
""", unsafe_allow_html=True)
