# Import required libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import matplotlib.pyplot as plt  # For creating visualizations
import seaborn as sns  # For statistical visualizations
import os  # For file operations
from datetime import datetime  # For timestamps

# Set visualization style for consistent, professional appearance
sns.set_style("whitegrid")  # Use white background with grid lines
plt.rcParams['figure.figsize'] = (10, 6)  # Default figure size
plt.rcParams['font.size'] = 10  # Default font size

# Print header
print("=" * 80)
print("STAGE 5: EXPLORATORY DATA ANALYSIS (EDA)")
print("=" * 80)
print()

# Define file paths
input_path = "data/processed/clean_churn_data.csv"
viz_dir = "outputs/visualizations"
findings_path = "outputs/reports/eda_findings.txt"

# Check if input file exists
if not os.path.exists(input_path):
    print(f"❌ ERROR: Clean dataset not found at {input_path}")
    print("Please complete Stage 4 first")
    exit()

# Create visualizations directory if it doesn't exist
os.makedirs(viz_dir, exist_ok=True)
print(f"📁 Visualizations will be saved to: {viz_dir}")
print()

# Load the clean dataset
print("📂 Loading clean dataset...")
df = pd.read_csv(input_path)
print(f"✅ Dataset loaded: {input_path}")
print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print()

# Initialize findings list to document key observations
findings = []
findings.append("=" * 80)
findings.append("EXPLORATORY DATA ANALYSIS - KEY FINDINGS")
findings.append("=" * 80)
findings.append("")
findings.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
findings.append(f"Dataset: {input_path}")
findings.append(f"Total Customers: {len(df):,}")
findings.append("")

# ==================== PART 1: DATASET OVERVIEW ====================
print("-" * 80)
print("PART 1: DATASET OVERVIEW")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 1: DATASET OVERVIEW")
findings.append("-" * 80)

# Display basic information about the dataset
print(f"Total Customers: {len(df):,}")
print(f"Total Features: {len(df.columns)}")
print()

# Display summary statistics for numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"Numeric columns: {len(numeric_cols)}")
print("\nSummary Statistics (Numeric Columns):")
print(df[numeric_cols].describe())
findings.append(f"Numeric Features: {len(numeric_cols)}")
findings.append("")

print()

# ==================== PART 2: TARGET VARIABLE ANALYSIS (CHURN) ====================
print("-" * 80)
print("PART 2: TARGET VARIABLE ANALYSIS (CHURN)")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 2: CHURN ANALYSIS")
findings.append("-" * 80)

# Calculate churn rate
churn_counts = df['Churn'].value_counts()
churn_percentages = df['Churn'].value_counts(normalize=True) * 100

print("Churn Distribution:")
for value, count in churn_counts.items():
    pct = churn_percentages[value]
    print(f"  {value}: {count:,} customers ({pct:.2f}%)")

# Store overall churn rate for findings
overall_churn_rate = churn_percentages.get('Yes', 0)
findings.append(f"Overall Churn Rate: {overall_churn_rate:.2f}%")
findings.append(f"  Churned: {churn_counts.get('Yes', 0):,} customers")
findings.append(f"  Retained: {churn_counts.get('No', 0):,} customers")
findings.append("")

print()

# Visualization 1: Churn Distribution (Pie Chart)
print("📊 Creating visualization: Churn Distribution...")
fig, ax = plt.subplots(figsize=(8, 6))

# Create pie chart with custom colors
colors = ['#2ecc71', '#e74c3c']  # Green for No, Red for Yes
wedges, texts, autotexts = ax.pie(
    churn_counts.values,  # Values to plot
    labels=churn_counts.index,  # Labels (Yes, No)
    autopct='%1.1f%%',  # Show percentages with 1 decimal
    startangle=90,  # Start from top
    colors=colors,  # Custom colors
    explode=(0, 0.1)  # Slightly separate the "Yes" slice for emphasis
)

# Make percentage text bold and white
for autotext in autotexts:
    autotext.set_color('white')  # White text on colored background
    autotext.set_fontsize(12)  # Larger font for readability
    autotext.set_weight('bold')  # Bold text

# Add title
ax.set_title('Customer Churn Distribution', fontsize=14, fontweight='bold', pad=20)

# Save figure
plt.tight_layout()  # Adjust spacing to prevent label cutoff
plt.savefig(f'{viz_dir}/churn_distribution.png', dpi=300, bbox_inches='tight')
plt.close()  # Close figure to free memory
print(f"   ✅ Saved: {viz_dir}/churn_distribution.png")
print()

# ==================== PART 3: UNIVARIATE ANALYSIS - NUMERIC VARIABLES ====================
print("-" * 80)
print("PART 3: UNIVARIATE ANALYSIS - NUMERIC VARIABLES")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 3: KEY NUMERIC VARIABLE DISTRIBUTIONS")
findings.append("-" * 80)

# Analyze key numeric variables: tenure, MonthlyCharges, TotalCharges

# --- Tenure Analysis ---
print("\n📊 Analyzing: tenure (months with company)")
print(f"  Mean: {df['tenure'].mean():.1f} months")
print(f"  Median: {df['tenure'].median():.1f} months")
print(f"  Range: {df['tenure'].min()}-{df['tenure'].max()} months")

findings.append(f"\nTenure (Customer Lifetime):")
findings.append(f"  Average: {df['tenure'].mean():.1f} months")
findings.append(f"  Median: {df['tenure'].median():.1f} months")
findings.append(f"  Range: {df['tenure'].min()}-{df['tenure'].max()} months")

# Visualization 2: Tenure Distribution
print("📊 Creating visualization: Tenure Distribution...")
fig, ax = plt.subplots(figsize=(10, 6))

# Create histogram with KDE (kernel density estimate) curve
ax.hist(df['tenure'], bins=30, color='steelblue', alpha=0.7, edgecolor='black')

# Add vertical lines for mean and median
ax.axvline(df['tenure'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: {df['tenure'].mean():.1f}")
ax.axvline(df['tenure'].median(), color='green', linestyle='--', linewidth=2, label=f"Median: {df['tenure'].median():.1f}")

# Labels and title
ax.set_xlabel('Tenure (Months)', fontsize=12)
ax.set_ylabel('Number of Customers', fontsize=12)
ax.set_title('Distribution of Customer Tenure', fontsize=14, fontweight='bold')
ax.legend()  # Show legend with mean/median lines
ax.grid(True, alpha=0.3)  # Add light grid

# Save figure
plt.tight_layout()
plt.savefig(f'{viz_dir}/tenure_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   ✅ Saved: {viz_dir}/tenure_distribution.png")

# --- MonthlyCharges Analysis ---
print("\n📊 Analyzing: MonthlyCharges")
print(f"  Mean: ${df['MonthlyCharges'].mean():.2f}")
print(f"  Median: ${df['MonthlyCharges'].median():.2f}")
print(f"  Range: ${df['MonthlyCharges'].min():.2f}-${df['MonthlyCharges'].max():.2f}")

findings.append(f"\nMonthly Charges:")
findings.append(f"  Average: ${df['MonthlyCharges'].mean():.2f}")
findings.append(f"  Median: ${df['MonthlyCharges'].median():.2f}")

# --- TotalCharges Analysis ---
print("\n📊 Analyzing: TotalCharges")
print(f"  Mean: ${df['TotalCharges'].mean():.2f}")
print(f"  Median: ${df['TotalCharges'].median():.2f}")

findings.append(f"\nTotal Charges:")
findings.append(f"  Average: ${df['TotalCharges'].mean():.2f}")
findings.append(f"  Median: ${df['TotalCharges'].median():.2f}")

# Visualization 3: Charges Distribution (side-by-side)
print("📊 Creating visualization: Charges Distribution...")
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: MonthlyCharges
axes[0].hist(df['MonthlyCharges'], bins=30, color='coral', alpha=0.7, edgecolor='black')
axes[0].axvline(df['MonthlyCharges'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: ${df['MonthlyCharges'].mean():.2f}")
axes[0].set_xlabel('Monthly Charges ($)', fontsize=11)
axes[0].set_ylabel('Number of Customers', fontsize=11)
axes[0].set_title('Monthly Charges Distribution', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Subplot 2: TotalCharges
axes[1].hist(df['TotalCharges'], bins=30, color='mediumpurple', alpha=0.7, edgecolor='black')
axes[1].axvline(df['TotalCharges'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: ${df['TotalCharges'].mean():.2f}")
axes[1].set_xlabel('Total Charges ($)', fontsize=11)
axes[1].set_ylabel('Number of Customers', fontsize=11)
axes[1].set_title('Total Charges Distribution', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

# Save figure
plt.tight_layout()
plt.savefig(f'{viz_dir}/charges_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   ✅ Saved: {viz_dir}/charges_distribution.png")

findings.append("")
print()

# ==================== PART 4: BIVARIATE ANALYSIS - CHURN VS. FEATURES ====================
print("-" * 80)
print("PART 4: BIVARIATE ANALYSIS - CHURN VS. KEY FEATURES")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 4: CHURN DRIVERS ANALYSIS")
findings.append("-" * 80)

# --- Churn by Contract Type ---
print("\n📊 Analyzing: Churn by Contract Type")

# Calculate churn rate for each contract type
churn_by_contract = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
print("Churn Rate by Contract Type:")
for contract, rate in churn_by_contract.items():
    print(f"  {contract}: {rate:.2f}%")

findings.append("\nChurn by Contract Type:")
for contract, rate in churn_by_contract.items():
    findings.append(f"  {contract}: {rate:.2f}%")

# Visualization 4: Churn Rate by Contract Type
print("📊 Creating visualization: Churn by Contract Type...")
fig, ax = plt.subplots(figsize=(10, 6))

# Create grouped bar chart
contract_churn = df.groupby(['Contract', 'Churn']).size().unstack()
contract_churn_pct = contract_churn.div(contract_churn.sum(axis=1), axis=0) * 100

# Plot bars
contract_churn_pct.plot(kind='bar', ax=ax, color=['#2ecc71', '#e74c3c'], alpha=0.8)

# Labels and formatting
ax.set_xlabel('Contract Type', fontsize=12)
ax.set_ylabel('Percentage (%)', fontsize=12)
ax.set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
ax.legend(title='Churn', labels=['No', 'Yes'])
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Horizontal labels
ax.grid(True, alpha=0.3, axis='y')

# Save figure
plt.tight_layout()
plt.savefig(f'{viz_dir}/churn_by_contract.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   ✅ Saved: {viz_dir}/churn_by_contract.png")

# --- Churn by Tenure (Binned) ---
print("\n📊 Analyzing: Churn by Tenure Groups")

# Create tenure bins (0-12, 13-24, 25-48, 49-72 months)
df['TenureGroup'] = pd.cut(
    df['tenure'],  # Column to bin
    bins=[0, 12, 24, 48, 72],  # Bin edges
    labels=['0-12 months', '13-24 months', '25-48 months', '49-72 months']  # Bin labels
)

# Calculate churn rate for each tenure group
churn_by_tenure = df.groupby('TenureGroup')['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
print("Churn Rate by Tenure Group:")
for group, rate in churn_by_tenure.items():
    print(f"  {group}: {rate:.2f}%")

findings.append("\nChurn by Tenure:")
for group, rate in churn_by_tenure.items():
    findings.append(f"  {group}: {rate:.2f}%")

# Visualization 5: Churn Rate by Tenure Group
print("📊 Creating visualization: Churn by Tenure...")
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart
churn_by_tenure.plot(kind='bar', ax=ax, color='steelblue', alpha=0.8)

# Labels and formatting
ax.set_xlabel('Tenure Group', fontsize=12)
ax.set_ylabel('Churn Rate (%)', fontsize=12)
ax.set_title('Churn Rate by Customer Tenure', fontsize=14, fontweight='bold')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
ax.grid(True, alpha=0.3, axis='y')

# Add value labels on top of bars
for i, v in enumerate(churn_by_tenure.values):
    ax.text(i, v + 1, f'{v:.1f}%', ha='center', fontsize=10, fontweight='bold')

# Save figure
plt.tight_layout()
plt.savefig(f'{viz_dir}/churn_by_tenure.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   ✅ Saved: {viz_dir}/churn_by_tenure.png")

# --- Churn by Payment Method ---
print("\n📊 Analyzing: Churn by Payment Method")

churn_by_payment = df.groupby('PaymentMethod')['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
print("Churn Rate by Payment Method:")
for method, rate in churn_by_payment.items():
    print(f"  {method}: {rate:.2f}%")

findings.append("\nChurn by Payment Method:")
for method, rate in churn_by_payment.items():
    findings.append(f"  {method}: {rate:.2f}%")

# Visualization 6: Churn by Payment Method
print("📊 Creating visualization: Churn by Payment Method...")
fig, ax = plt.subplots(figsize=(10, 6))

# Sort by churn rate for better visualization
churn_by_payment_sorted = churn_by_payment.sort_values(ascending=False)
churn_by_payment_sorted.plot(kind='barh', ax=ax, color='coral', alpha=0.8)

# Labels and formatting
ax.set_xlabel('Churn Rate (%)', fontsize=12)
ax.set_ylabel('Payment Method', fontsize=12)
ax.set_title('Churn Rate by Payment Method', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='x')

# Add value labels
for i, v in enumerate(churn_by_payment_sorted.values):
    ax.text(v + 0.5, i, f'{v:.1f}%', va='center', fontsize=10, fontweight='bold')

# Save figure
plt.tight_layout()
plt.savefig(f'{viz_dir}/churn_by_payment_method.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   ✅ Saved: {viz_dir}/churn_by_payment_method.png")

# --- Churn by Internet Service ---
print("\n📊 Analyzing: Churn by Internet Service Type")

churn_by_internet = df.groupby('InternetService')['Churn'].apply(lambda x: (x == 'Yes').sum() / len(x) * 100)
print("Churn Rate by Internet Service:")
for service, rate in churn_by_internet.items():
    print(f"  {service}: {rate:.2f}%")

findings.append("\nChurn by Internet Service:")
for service, rate in churn_by_internet.items():
    findings.append(f"  {service}: {rate:.2f}%")

findings.append("")
print()

# ==================== PART 5: CORRELATION ANALYSIS ====================
print("-" * 80)
print("PART 5: CORRELATION ANALYSIS (NUMERIC VARIABLES)")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 5: CORRELATION INSIGHTS")
findings.append("-" * 80)

# Select key numeric columns for correlation
key_numeric = ['tenure', 'MonthlyCharges', 'TotalCharges']

# Check which columns actually exist in the dataset
available_numeric = [col for col in key_numeric if col in df.columns]

# Add any additional numeric columns
additional_cols = [col for col in ['TotalPayments', 'TotalPaid'] if col in df.columns]
available_numeric.extend(additional_cols)

# Calculate correlation matrix
correlation_matrix = df[available_numeric].corr()

print("Correlation Matrix (Key Numeric Variables):")
print(correlation_matrix)
print()

# Identify strong correlations (absolute value > 0.7)
print("Strong Correlations (|r| > 0.7):")
strong_corr_found = False
for i in range(len(correlation_matrix.columns)):
    for j in range(i+1, len(correlation_matrix.columns)):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > 0.7:
            print(f"  {correlation_matrix.columns[i]} <-> {correlation_matrix.columns[j]}: {corr_value:.3f}")
            findings.append(f"Strong correlation: {correlation_matrix.columns[i]} <-> {correlation_matrix.columns[j]} (r={corr_value:.3f})")
            strong_corr_found = True

if not strong_corr_found:
    print("  No strong correlations found")
    findings.append("No strong correlations (|r| > 0.7) found among key variables")

# Visualization 7: Correlation Heatmap
print("\n📊 Creating visualization: Correlation Heatmap...")
fig, ax = plt.subplots(figsize=(10, 8))

# Create heatmap with annotations
sns.heatmap(
    correlation_matrix,  # Data to plot
    annot=True,  # Show correlation values in cells
    fmt='.2f',  # Format numbers to 2 decimal places
    cmap='coolwarm',  # Color scheme (blue=negative, red=positive)
    center=0,  # Center color scale at 0
    square=True,  # Make cells square
    linewidths=0.5,  # Lines between cells
    cbar_kws={"shrink": 0.8},  # Colorbar settings
    ax=ax
)

# Title
ax.set_title('Correlation Heatmap - Numeric Variables', fontsize=14, fontweight='bold', pad=20)

# Save figure
plt.tight_layout()
plt.savefig(f'{viz_dir}/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()
print(f"   ✅ Saved: {viz_dir}/correlation_heatmap.png")

findings.append("")
print()

# ==================== PART 6: HIGH-RISK SEGMENTS IDENTIFICATION ====================
print("-" * 80)
print("PART 6: HIGH-RISK CUSTOMER SEGMENTS")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 6: HIGH-RISK SEGMENTS")
findings.append("-" * 80)

# Define high-risk segment: Month-to-month contract + High monthly charges
high_risk_mask = (df['Contract'] == 'Month-to-month') & (df['MonthlyCharges'] > df['MonthlyCharges'].median())
high_risk_customers = df[high_risk_mask]
high_risk_churn_rate = (high_risk_customers['Churn'] == 'Yes').sum() / len(high_risk_customers) * 100

print(f"\nHigh-Risk Segment 1: Month-to-month + High Charges")
print(f"  Customers: {len(high_risk_customers):,} ({len(high_risk_customers)/len(df)*100:.1f}% of total)")
print(f"  Churn Rate: {high_risk_churn_rate:.2f}%")

findings.append("\nSegment 1: Month-to-month contracts + High monthly charges")
findings.append(f"  Size: {len(high_risk_customers):,} customers ({len(high_risk_customers)/len(df)*100:.1f}%)")
findings.append(f"  Churn Rate: {high_risk_churn_rate:.2f}%")

# Define high-risk segment 2: Low tenure + No tech support (if TechSupport column exists)
if 'TechSupport' in df.columns:
    low_tenure_no_support_mask = (df['tenure'] < 12) & (df['TechSupport'] == 'No')
    low_tenure_no_support = df[low_tenure_no_support_mask]
    low_tenure_churn_rate = (low_tenure_no_support['Churn'] == 'Yes').sum() / len(low_tenure_no_support) * 100

    print(f"\nHigh-Risk Segment 2: New Customers (tenure < 12 months) + No Tech Support")
    print(f"  Customers: {len(low_tenure_no_support):,} ({len(low_tenure_no_support)/len(df)*100:.1f}% of total)")
    print(f"  Churn Rate: {low_tenure_churn_rate:.2f}%")

    findings.append("\nSegment 2: New customers (tenure < 12 months) + No tech support")
    findings.append(f"  Size: {len(low_tenure_no_support):,} customers ({len(low_tenure_no_support)/len(df)*100:.1f}%)")
    findings.append(f"  Churn Rate: {low_tenure_churn_rate:.2f}%")

# Low-risk segment: Long tenure + Two-year contract
low_risk_mask = (df['Contract'] == 'Two year') & (df['tenure'] > 48)
low_risk_customers = df[low_risk_mask]
if len(low_risk_customers) > 0:
    low_risk_churn_rate = (low_risk_customers['Churn'] == 'Yes').sum() / len(low_risk_customers) * 100

    print(f"\nLow-Risk Segment: Two-year Contract + Long Tenure (>48 months)")
    print(f"  Customers: {len(low_risk_customers):,} ({len(low_risk_customers)/len(df)*100:.1f}% of total)")
    print(f"  Churn Rate: {low_risk_churn_rate:.2f}%")

    findings.append("\nLow-Risk Segment: Two-year contracts + Long tenure (>48 months)")
    findings.append(f"  Size: {len(low_risk_customers):,} customers ({len(low_risk_customers)/len(df)*100:.1f}%)")
    findings.append(f"  Churn Rate: {low_risk_churn_rate:.2f}%")

findings.append("")
print()

# ==================== PART 7: KEY OBSERVATIONS SUMMARY ====================
print("-" * 80)
print("PART 7: KEY OBSERVATIONS & HYPOTHESES")
print("-" * 80)

findings.append("-" * 80)
findings.append("PART 7: KEY OBSERVATIONS")
findings.append("-" * 80)

# Generate key observations based on analysis
print("\nKey Observations:")

obs1 = f"1. Overall churn rate is {overall_churn_rate:.1f}% - approximately 1 in {100/overall_churn_rate:.0f} customers leave"
print(f"  {obs1}")
findings.append(obs1)

# Find contract type with highest churn
highest_churn_contract = churn_by_contract.idxmax()
obs2 = f"2. {highest_churn_contract} contracts have highest churn rate ({churn_by_contract.max():.1f}%)"
print(f"  {obs2}")
findings.append(obs2)

obs3 = f"3. Customers in first 12 months have {churn_by_tenure.iloc[0]:.1f}% churn - retention critical in first year"
print(f"  {obs3}")
findings.append(obs3)

# Find payment method with highest churn
highest_churn_payment = churn_by_payment.idxmax()
obs4 = f"4. {highest_churn_payment} has highest churn rate ({churn_by_payment.max():.1f}%) among payment methods"
print(f"  {obs4}")
findings.append(obs4)

obs5 = f"5. Average tenure is {df['tenure'].mean():.1f} months - indicates moderate customer lifetime"
print(f"  {obs5}")
findings.append(obs5)

print("\nHypotheses for Further Investigation (Stage 7):")
findings.append("\nHypotheses for Stage 7:")

hyp1 = "- Month-to-month contracts drive churn - offer incentives for longer commitments"
print(f"  {hyp1}")
findings.append(hyp1)

hyp2 = "- Early-tenure customers at highest risk - improve onboarding and first-year support"
print(f"  {hyp2}")
findings.append(hyp2)

hyp3 = "- Payment method may indicate customer engagement level - investigate electronic check users"
print(f"  {hyp3}")
findings.append(hyp3)

hyp4 = "- Service add-ons (tech support, security) may reduce churn - test upsell strategies"
print(f"  {hyp4}")
findings.append(hyp4)

findings.append("")
print()

# ==================== SAVE FINDINGS REPORT ====================
print("-" * 80)
print("SAVING EDA FINDINGS")
print("-" * 80)

# Add final section to findings
findings.append("=" * 80)
findings.append("END OF REPORT")
findings.append("=" * 80)
findings.append("")
findings.append(f"Visualizations saved to: {viz_dir}/")
findings.append("Total visualizations: 7")
findings.append("")
findings.append("Next Steps:")
findings.append("- Stage 6: Feature Engineering & Metrics Layer")
findings.append("- Stage 7: Analytical Reasoning (hypothesis testing)")
findings.append("- Stage 8: Dashboard Development")

# Create reports directory if it doesn't exist
os.makedirs(os.path.dirname(findings_path), exist_ok=True)

# Write findings to file
with open(findings_path, 'w') as f:
    f.write('\n'.join(findings))

print(f"✅ Findings report saved: {findings_path}")
print()

# ==================== FINAL SUMMARY ====================
print("=" * 80)
print("✅ EXPLORATORY DATA ANALYSIS COMPLETE")
print("=" * 80)
print()
print("Outputs Generated:")
print(f"  📊 Visualizations: {viz_dir}/")
print(f"     - churn_distribution.png")
print(f"     - tenure_distribution.png")
print(f"     - charges_distribution.png")
print(f"     - churn_by_contract.png")
print(f"     - churn_by_tenure.png")
print(f"     - churn_by_payment_method.png")
print(f"     - correlation_heatmap.png")
print()
print(f"  📄 Findings Report: {findings_path}")
print()
print("Key Insights Discovered:")
print(f"  • Overall churn rate: {overall_churn_rate:.1f}%")
print(f"  • Highest risk: {highest_churn_contract} contracts")
print(f"  • Critical period: First 12 months (churn rate {churn_by_tenure.iloc[0]:.1f}%)")
print(f"  • Payment risk: {highest_churn_payment}")
print()
print("Next Step: Proceed to Stage 6 (Feature Engineering & Metrics Layer)")
