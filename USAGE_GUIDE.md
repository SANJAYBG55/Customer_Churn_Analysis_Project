# 📖 Dashboard Usage Guide

## Introduction

This guide explains how to use the **Customer Churn Analysis Dashboard** to explore data, generate insights, and make data-driven retention decisions.

**Target Audience:** Business users, managers, executives, marketing teams, customer success teams

---

## 🚀 Launching the Dashboard

### Step 1: Open Terminal/Command Prompt

Navigate to the project directory:
```bash
cd path/to/customer_churn_analysis
```

### Step 2: Run the Dashboard

Execute the following command:
```bash
streamlit run dashboard/churn_dashboard.py
```

### Step 3: Access in Browser

The dashboard automatically opens in your default browser at:
```
http://localhost:8501
```

If it doesn't open automatically, manually navigate to this URL.

---

## 🧭 Dashboard Navigation

### Sidebar Navigation

The left sidebar contains:
- **Page Selector**: Choose from 5 main pages
- **Global Filters**: Apply filters that affect all visualizations
- **Filtered Customer Count**: Shows how many customers match your filters

### 5 Main Pages

1. **🏠 Executive Overview** - High-level KPIs and key insights
2. **📈 Segment Analysis** - Deep dive into customer segments
3. **🎯 Churn Drivers** - Analyze what causes churn
4. **💡 Recommendations** - Actionable business strategies
5. **🔍 Customer Explorer** - Interactive data filtering and export

---

## 📊 Page-by-Page Guide

### Page 1: Executive Overview

**Purpose:** Get a quick snapshot of overall churn situation

**Key Metrics Displayed:**
- Total Customers
- Overall Churn Rate
- Revenue at Risk
- Average Revenue Per User (ARPU)

**Visualizations:**
- Churn Distribution (churned vs retained)
- Revenue Impact by Segment
- Churn Rate by Segment

**How to Use:**
1. Review the 4 key metrics at the top
2. Check the churn distribution pie chart
3. Read the "Key Insights" section for top findings
4. Note the "Top Recommendations" for quick action items

**Best For:** Executive presentations, status updates, monthly reviews

---

### Page 2: Segment Analysis

**Purpose:** Compare different customer segments to identify patterns

**Segment Types:**
- **Risk Segments**: High/Medium/Low risk (based on churn probability)
- **Value Segments**: High/Medium/Low value (based on revenue)
- **Tenure Segments**: New/Growing/Mature/Loyal (based on time with company)

**How to Use:**
1. Select segment type using radio buttons at top
2. Review segment comparison charts
3. Check the segment breakdown table for detailed statistics
4. Compare churn rates across segments
5. Identify which segments need attention

**Example Questions You Can Answer:**
- Which risk segment has the highest churn rate?
- How many high-value customers are at high risk?
- What's the churn rate for new vs loyal customers?
- Which segment represents the largest revenue opportunity?

**Best For:** Strategic planning, customer success prioritization, resource allocation

---

### Page 3: Churn Drivers

**Purpose:** Understand what factors drive customers to churn

**Available Drivers:**
- **Contract Type**: Month-to-month vs 1-year vs 2-year
- **Payment Method**: Electronic check, credit card, bank transfer, etc.
- **Service Adoption**: Number of services customer uses
- **Tenure Impact**: How length of relationship affects churn

**How to Use:**
1. Select a churn driver from the dropdown menu
2. Review the visualization showing churn rates by driver
3. Read the insights section below the chart
4. Compare different driver values to identify patterns

**Example Insights:**
- "Month-to-month customers churn 3.5x more than 2-year contracts"
- "Electronic check users have 45% churn rate"
- "Customers with 6+ services have 15% lower churn"

**Best For:** Root cause analysis, targeted campaigns, retention strategy development

---

### Page 4: Recommendations

**Purpose:** Review prioritized, actionable business recommendations

**Structure:**
Each recommendation includes:
- **Priority Level**: HIGH/MEDIUM/LOW
- **Problem Statement**: What issue it addresses
- **Recommended Action**: Specific steps to take
- **Expected Outcome**: Quantified impact
- **Implementation Timeline**: How long it will take

**5 Key Recommendations:**
1. Contract Commitment Incentives (HIGH priority)
2. Enhanced First-Year Onboarding (HIGH priority)
3. Payment Method Migration Campaign (MEDIUM priority)
4. Service Adoption & Upsell Campaign (MEDIUM priority)
5. Churn Early Warning System (MEDIUM-LOW priority)

**How to Use:**
1. Read through each recommendation
2. Note the priority levels for sequencing
3. Review implementation timelines in right column
4. Check the roadmap at bottom for phased approach

**Best For:** Action planning, budget allocation, strategic initiatives

---

### Page 5: Customer Explorer

**Purpose:** Interactively filter customers and export data for campaigns

**Features:**
- **Advanced Filters**: Risk score, churn status, payment method
- **Real-time Metrics**: Updates as you filter
- **Data Table**: View individual customer records
- **Export Function**: Download filtered customer lists as CSV

**How to Use:**

**Example 1: Export High-Risk Customer List**
1. In sidebar, keep all filters at default
2. On Customer Explorer page, select "Risk Score = 3"
3. Review the filtered customer count and metrics
4. Scroll to data table to see specific customers
5. Click "Download Filtered Data as CSV"
6. Use this list for retention outreach campaigns

**Example 2: Find Month-to-Month Electronic Check Users**
1. In sidebar, select only "Month-to-month" in Contract filter
2. On Customer Explorer page, select "Electronic check" in Payment Method filter
3. Review how many customers match (likely 800-1200)
4. Check their churn rate (likely 50%+)
5. Export this high-risk segment for targeted campaign

**Example 3: Identify New High-Value Customers**
1. In sidebar, select "New" in Tenure Segment filter
2. In sidebar, select "High" in Value Segment filter
3. Review the count (critical customers to retain)
4. Export for priority onboarding program

**Best For:** Campaign targeting, customer success outreach, data analysis

---

## 🔧 Using Global Filters

### Filter Location
Left sidebar, under "🔧 Global Filters"

### Available Filters

**1. Contract Type**
- Month-to-month
- One year
- Two year

**2. Tenure Segment**
- New (0-12 months)
- Growing (13-24 months)
- Mature (25-48 months)
- Loyal (49+ months)

**3. Value Segment**
- High (top 33%)
- Medium (middle 33%)
- Low (bottom 33%)

### How Filters Work

- **Multi-select**: Check/uncheck multiple options
- **Default**: All options selected (no filtering)
- **Effect**: Updates ALL pages and visualizations
- **Customer Count**: Shows filtered count at bottom of sidebar

### Filter Examples

**Example 1: Focus on High-Risk Month-to-Month Customers**
1. Uncheck "One year" and "Two year" in Contract Type
2. Keep all other filters at default
3. All pages now show only month-to-month customers
4. Review their specific churn drivers and patterns

**Example 2: Analyze Loyal High-Value Customers**
1. Select only "Loyal" in Tenure Segment
2. Select only "High" in Value Segment
3. See how your best customers behave
4. Compare their churn rate to overall rate

**Example 3: New Customer Analysis**
1. Select only "New" in Tenure Segment
2. Keep other filters at default
3. All visualizations show first-year customer patterns
4. Use to design onboarding program

### Resetting Filters

To reset filters:
1. Check all boxes in each filter
2. Alternatively, refresh the page (Ctrl+R or Cmd+R)

---

## 💡 Common Use Cases

### Use Case 1: Monthly Executive Review

**Goal:** Present churn status to leadership

**Steps:**
1. Navigate to Executive Overview page
2. Take screenshot of key metrics
3. Note top 3 insights
4. Review recommendations page for progress updates
5. Prepare 5-minute summary

**Time Required:** 5 minutes

---

### Use Case 2: High-Risk Customer Retention Campaign

**Goal:** Export list of at-risk customers for outreach

**Steps:**
1. Go to Customer Explorer page
2. Filter: Risk Score = 3 (High Risk)
3. Optional: Add Value Segment = High (prioritize valuable customers)
4. Review customer count (target list size)
5. Download CSV
6. Import to CRM for campaign execution

**Time Required:** 2 minutes

---

### Use Case 3: Contract Upgrade Campaign

**Goal:** Identify month-to-month customers to target for contract upgrades

**Steps:**
1. Sidebar: Select only "Month-to-month" in Contract Type
2. Navigate to Churn Drivers page
3. Select "Contract Type" driver
4. Note the churn rate difference (42% vs 11%)
5. Go to Customer Explorer
6. Download filtered customer list
7. Use for contract upgrade marketing campaign

**Time Required:** 3 minutes

---

### Use Case 4: First-Year Onboarding Analysis

**Goal:** Understand new customer churn patterns to improve onboarding

**Steps:**
1. Sidebar: Select only "New" in Tenure Segment
2. Navigate to Segment Analysis page
3. Review new customer churn rate (likely 45-50%)
4. Go to Churn Drivers page
5. Analyze which factors affect new customers most
6. Use insights to design 0-12 month onboarding program

**Time Required:** 10 minutes

---

### Use Case 5: Service Upsell Opportunity Analysis

**Goal:** Identify customers with low service adoption for upsell campaigns

**Steps:**
1. Navigate to Churn Drivers page
2. Select "Service Adoption" driver
3. Note: Low engagement (0-2 services) = 38% churn
4. High engagement (6+ services) = 23% churn
5. Go to Customer Explorer page
6. Filter by low engagement characteristics
7. Export for upsell campaign targeting

**Time Required:** 5 minutes

---

## 🎯 Best Practices

### For Business Users

✅ **Do:**
- Start with Executive Overview for context
- Use filters to explore specific segments
- Export customer lists for actionable campaigns
- Review recommendations page for strategic guidance
- Take screenshots for presentations

❌ **Don't:**
- Make decisions based on small filtered samples (<100 customers)
- Ignore the insights sections (they provide context)
- Forget to reset filters when switching analyses

### For Analysts

✅ **Do:**
- Use Customer Explorer for detailed investigations
- Cross-reference multiple churn drivers
- Validate findings across different segments
- Document filter combinations for reproducible analysis

❌ **Don't:**
- Over-filter (reducing sample size too much)
- Mix incompatible filters (e.g., Loyal + High Risk may have very few customers)

### For Executives

✅ **Do:**
- Use Executive Overview page primarily
- Review Top 3 Recommendations section
- Check churn rate trends monthly
- Ask team to export action lists from Customer Explorer

❌ **Don't:**
- Get lost in detailed driver analysis (delegate to team)
- Expect real-time data (dashboard uses static dataset snapshot)

---

## ⚡ Keyboard Shortcuts

- **Ctrl+R** (Cmd+R on Mac): Refresh page/reset filters
- **Ctrl+F** (Cmd+F): Search within page
- **Tab**: Navigate between interactive elements

---

## ❓ Troubleshooting

### Issue: Dashboard won't load

**Solution:**
1. Check terminal for error messages
2. Verify Python and packages installed: `pip list`
3. Ensure you're in correct directory
4. Try: `streamlit run dashboard/churn_dashboard.py` again

### Issue: Charts not displaying

**Solution:**
1. Check browser console (F12) for errors
2. Try different browser (Chrome recommended)
3. Verify Plotly installed: `pip install plotly`

### Issue: Filters not working

**Solution:**
1. Refresh page (Ctrl+R)
2. Ensure at least one option selected in each filter
3. Check filtered customer count (should be >0)

### Issue: Download button not working

**Solution:**
1. Check browser's download settings
2. Ensure pop-ups not blocked
3. Try different browser

### Issue: Numbers don't match expected values

**Solution:**
1. Check which filters are applied (sidebar)
2. Reset all filters to see total population
3. Verify you're looking at correct segment

---

## 📞 Support

For technical issues or questions:
- Check TECHNICAL_DOCUMENTATION.md for detailed specs
- Review README.md for project overview
- Contact: [your.email@example.com]

---

**Last Updated:** January 2026
