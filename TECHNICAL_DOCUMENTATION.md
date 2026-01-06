# 📋 Technical Documentation

## Project Architecture

### Overview

The Customer Churn Analysis project follows a **modular, pipeline-based architecture** with four distinct processing stages, a dashboard layer, and comprehensive reporting outputs.

```
┌─────────────────────────────────────────────────────────────┐
│                     DATA SOURCES                            │
│              Raw CSV (7,043 customers)                      │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  STAGE 1: DATA CLEANING                      │
│  • Missing value handling                                   │
│  • Data type validation                                     │
│  • Duplicate removal                                        │
│  • Quality checks                                           │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│              STAGE 2: EXPLORATORY ANALYSIS                   │
│  • Statistical summaries                                    │
│  • Distribution analysis                                    │
│  • Correlation analysis                                     │
│  • Visualization generation                                 │
│  • Hypothesis formation                                     │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│             STAGE 3: FEATURE ENGINEERING                     │
│  • Business metric calculation (CLV, ARPU)                  │
│  • Risk scoring                                             │
│  • Segmentation (Risk, Value, Tenure)                       │
│  • Service adoption metrics                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│            STAGE 4: ANALYTICAL REASONING                     │
│  • Hypothesis validation                                    │
│  • Segment analysis                                         │
│  • Churn driver quantification                              │
│  • Business recommendations                                 │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUTS                                  │
│  • Analysis Reports (TXT)                                   │
│  • Visualizations (PNG)                                     │
│  • Enriched Dataset (CSV)                                   │
│  • Interactive Dashboard (Streamlit)                        │
└─────────────────────────────────────────────────────────────┘
```

---

## Data Schema

### Raw Dataset Schema

**Source:** `data/raw/telco_churn.csv`

| Column | Data Type | Description | Example Values |
|--------|-----------|-------------|----------------|
| customerID | string | Unique customer identifier | "7590-VHVEG" |
| gender | string | Customer gender | "Female", "Male" |
| SeniorCitizen | int | Senior citizen flag (0/1) | 0, 1 |
| Partner | string | Has partner | "Yes", "No" |
| Dependents | string | Has dependents | "Yes", "No" |
| tenure | int | Months with company | 1-72 |
| PhoneService | string | Has phone service | "Yes", "No" |
| MultipleLines | string | Has multiple lines | "Yes", "No", "No phone service" |
| InternetService | string | Internet service type | "DSL", "Fiber optic", "No" |
| OnlineSecurity | string | Has online security | "Yes", "No", "No internet service" |
| OnlineBackup | string | Has online backup | "Yes", "No", "No internet service" |
| DeviceProtection | string | Has device protection | "Yes", "No", "No internet service" |
| TechSupport | string | Has tech support | "Yes", "No", "No internet service" |
| StreamingTV | string | Has streaming TV | "Yes", "No", "No internet service" |
| StreamingMovies | string | Has streaming movies | "Yes", "No", "No internet service" |
| Contract | string | Contract type | "Month-to-month", "One year", "Two year" |
| PaperlessBilling | string | Paperless billing | "Yes", "No" |
| PaymentMethod | string | Payment method | "Electronic check", "Mailed check", "Bank transfer", "Credit card" |
| MonthlyCharges | float | Monthly charges | 18.25-118.75 |
| TotalCharges | string | Total charges to date | "18.8"-"8684.8" (note: string with spaces) |
| Churn | string | Churn status | "Yes", "No" |

**Total Rows:** 7,043  
**Total Columns:** 21

---

### Clean Dataset Schema

**Source:** `data/processed/clean_churn_data.csv`

**Changes from Raw:**
- `TotalCharges` converted to float
- Missing values handled
- Data types standardized
- Duplicates removed

**New Columns:** None (same 21 columns, cleaner data)

---

### Enriched Dataset Schema

**Source:** `data/processed/enriched_churn_data.csv`

**Original 21 columns PLUS 14 new engineered features:**

| Feature | Data Type | Description | Calculation | Range |
|---------|-----------|-------------|-------------|-------|
| **ARPU** | float | Average Revenue Per User | MonthlyCharges | $18.25-$118.75 |
| **CLV** | float | Customer Lifetime Value | TotalCharges | $18.8-$8,684.8 |
| **Tenure_Segment** | string | Customer lifecycle stage | Based on tenure months | "New", "Growing", "Mature", "Loyal" |
| **Value_Segment** | string | Revenue tier | Based on CLV percentiles | "High", "Medium", "Low" |
| **Service_Count** | int | Number of services adopted | Count of Yes values | 0-9 |
| **Engagement_Level** | string | Service adoption tier | Based on Service_Count | "Low", "Medium", "High" |
| **Risk_Score** | int | Churn risk score | Rule-based calculation | 1-3 |
| **Risk_Segment** | string | Risk category | Based on Risk_Score | "Low", "Medium", "High" |
| **Contract_Risk** | int | Contract stability | Contract type mapping | 3, 2, 1 |
| **Tenure_Risk** | int | Tenure-based risk | Tenure brackets | 3, 2, 1 |
| **Payment_Risk** | int | Payment method risk | Payment type mapping | 2, 1 |
| **Service_Risk** | int | Engagement-based risk | Service count mapping | 3, 2, 1 |
| **Churn_Numeric** | int | Binary churn indicator | Churn Yes/No mapping | 0, 1 |
| **Revenue_at_Risk** | float | Potential lost revenue | ARPU * 12 (annual) | $219-$1,425 |

**Total Rows:** 7,043  
**Total Columns:** 35 (21 original + 14 engineered)

---

## Feature Engineering Methodology

### 1. ARPU (Average Revenue Per User)
```python
ARPU = MonthlyCharges
```
**Business Logic:** Direct monthly revenue per customer

### 2. CLV (Customer Lifetime Value)
```python
CLV = TotalCharges
```
**Business Logic:** Historical total revenue from customer

### 3. Tenure Segment
```python
if tenure <= 12: "New"
elif tenure <= 24: "Growing"
elif tenure <= 48: "Mature"
else: "Loyal"
```
**Business Logic:** Customer lifecycle stages based on relationship length

### 4. Value Segment
```python
High: CLV >= 75th percentile
Medium: 25th <= CLV < 75th percentile
Low: CLV < 25th percentile
```
**Business Logic:** Revenue-based customer tiers

### 5. Service Count
```python
Service_Count = sum of 'Yes' values in:
- PhoneService
- InternetService (DSL/Fiber)
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- MultipleLines
```
**Business Logic:** Total services adopted by customer

### 6. Engagement Level
```python
if Service_Count <= 2: "Low"
elif Service_Count <= 5: "Medium"
else: "High"
```
**Business Logic:** Engagement tiers based on service adoption

### 7. Risk Score (Composite)
```python
Risk_Score = Contract_Risk + Tenure_Risk + Payment_Risk + Service_Risk

Where:
Contract_Risk:
  - Month-to-month: 3
  - One year: 2
  - Two year: 1

Tenure_Risk:
  - 0-12 months: 3
  - 13-24 months: 2
  - 25+ months: 1

Payment_Risk:
  - Electronic check: 2
  - Other: 1

Service_Risk:
  - 0-2 services: 3
  - 3-5 services: 2
  - 6+ services: 1

Risk_Score Range: 4-11
```

### 8. Risk Segment
```python
if Risk_Score >= 9: "High"
elif Risk_Score >= 6: "Medium"
else: "Low"
```
**Business Logic:** Churn probability categories

### 9. Revenue at Risk
```python
Revenue_at_Risk = ARPU * 12
```
**Business Logic:** Annual revenue loss if customer churns

---

## Analysis Methodology

### Hypothesis Testing Framework

**4 Primary Hypotheses Validated:**

1. **Contract Commitment Hypothesis**
   - **H1:** Month-to-month customers churn more than long-term contracts
   - **Method:** Churn rate comparison by contract type
   - **Result:** VALIDATED (42.7% vs 11.3%, 3.8x difference)

2. **Tenure Hypothesis**
   - **H2:** New customers (0-12 months) churn more than loyal customers
   - **Method:** Churn rate by tenure segment
   - **Result:** VALIDATED (47.4% vs 15.2%, 3.1x difference)

3. **Payment Method Hypothesis**
   - **H3:** Electronic check users have elevated churn
   - **Method:** Churn rate by payment method
   - **Result:** VALIDATED (45.3% vs 15-18% for other methods)

4. **Service Adoption Hypothesis**
   - **H4:** Low engagement customers churn more
   - **Method:** Churn rate by engagement level
   - **Result:** VALIDATED (38.3% vs 23.1%, 15.2pp difference)

### Segmentation Strategy

**Multi-Dimensional Segmentation:**

```
Risk Segmentation (Churn Probability)
├── High Risk (Risk_Score >= 9): ~1,200 customers, 42% churn
├── Medium Risk (6 <= Risk_Score < 9): ~2,500 customers, 28% churn
└── Low Risk (Risk_Score < 6): ~3,300 customers, 18% churn

Value Segmentation (Revenue Contribution)
├── High Value (CLV >= 75th percentile): ~1,760 customers
├── Medium Value (25th <= CLV < 75th): ~3,520 customers
└── Low Value (CLV < 25th percentile): ~1,760 customers

Tenure Segmentation (Lifecycle Stage)
├── New (0-12 months): ~1,700 customers, 47% churn
├── Growing (13-24 months): ~1,500 customers, 35% churn
├── Mature (25-48 months): ~2,100 customers, 22% churn
└── Loyal (49+ months): ~1,700 customers, 15% churn
```

---

## Dashboard Architecture

### Technology Stack

- **Framework:** Streamlit 1.29.0
- **Visualization:** Plotly 5.18.0
- **Data Processing:** Pandas 2.1.4
- **Layout:** Multi-page app with sidebar navigation

### Page Structure

```
Dashboard Application
│
├── Sidebar
│   ├── Navigation (5 pages)
│   └── Global Filters (Contract, Tenure, Value)
│
├── Page 1: Executive Overview
│   ├── Metric Cards (4 KPIs)
│   ├── Churn Distribution Chart
│   ├── Revenue Impact Chart
│   ├── Key Insights Section
│   └── Top Recommendations
│
├── Page 2: Segment Analysis
│   ├── Segment Type Selector
│   ├── Segment Comparison Chart
│   ├── Segment Metrics Table
│   └── Insights Section
│
├── Page 3: Churn Drivers
│   ├── Driver Selector Dropdown
│   ├── Driver-Specific Visualizations
│   ├── Comparative Analysis Charts
│   └── Contextual Insights
│
├── Page 4: Recommendations
│   ├── 5 Prioritized Recommendations
│   ├── Implementation Details
│   ├── Timeline Estimates
│   └── Phased Roadmap
│
└── Page 5: Customer Explorer
    ├── Advanced Filters
    ├── Real-time Metrics
    ├── Customer Data Table
    └── CSV Export Function
```

### Performance Optimization

**Caching Strategy:**
```python
@st.cache_data
def load_data():
    # Data loaded once per session
    return pd.read_csv(...)
```

**Benefits:**
- Data loads only once
- Filter updates are instant
- Reduces computation time by 90%

---

## Output Files

### Report Files

**1. data_quality_report.txt**
- Data shape (rows, columns)
- Missing value summary
- Data type validation
- Duplicate check results
- Quality assessment

**2. eda_findings.txt**
- Statistical summaries
- Distribution analysis
- Churn rate breakdowns
- Correlation findings
- Key observations
- Hypotheses generated

**3. feature_dictionary.txt**
- 14 engineered features documented
- Calculation methodology
- Business interpretation
- Value ranges

**4. analysis_report.txt**
- Hypothesis validation results
- Segment profiling
- Churn driver quantification
- Statistical evidence
- Business impact calculations

**5. business_recommendations.txt**
- 5 detailed recommendations
- Problem statements
- Action steps
- Expected outcomes
- Implementation timelines
- Priority rankings

**6. executive_summary.txt**
- Overall churn rate
- Top 3-4 key findings
- Top 3 recommendations
- Next steps
- High-level numbers only

**7. segment_comparison.csv**
- Segment-level statistics table
- Churn rates by segment
- Customer counts
- Average metrics
- Revenue calculations

### Visualization Files

**Location:** `outputs/visualizations/`

**Generated Charts (15-20 PNG files):**
- Churn distribution
- Contract type vs churn
- Tenure distribution
- Payment method analysis
- Service adoption charts
- Value segment comparison
- Risk segment profiles
- Correlation heatmaps

---

## Code Organization

### Script Modularization

**scripts/data_cleaning.py**
- Input: `data/raw/telco_churn.csv`
- Output: `data/processed/clean_churn_data.csv`
- Functions: handle_missing_values(), validate_types(), remove_duplicates()

**scripts/eda_analysis.py**
- Input: `data/processed/clean_churn_data.csv`
- Output: `outputs/reports/eda_findings.txt`, `outputs/visualizations/*.png`
- Functions: generate_summary(), create_visualizations(), analyze_distributions()

**scripts/feature_engineering.py**
- Input: `data/processed/clean_churn_data.csv`
- Output: `data/processed/enriched_churn_data.csv`
- Functions: calculate_clv(), create_segments(), compute_risk_score()

**scripts/analytical_reasoning.py**
- Input: `data/processed/enriched_churn_data.csv`
- Output: Multiple report files
- Functions: validate_hypotheses(), analyze_segments(), generate_recommendations()

**dashboard/churn_dashboard.py**
- Input: `data/processed/enriched_churn_data.csv`
- Output: Interactive web application
- Structure: Multi-page Streamlit app with filters

---

## Automation

### Master Pipeline Script

**run_full_analysis.py** executes all stages sequentially:

```
Stage 1: Data Cleaning (30-45 seconds)
    ↓
Stage 2: EDA (45-60 seconds)
    ↓
Stage 3: Feature Engineering (15-30 seconds)
    ↓
Stage 4: Analytical Reasoning (30-45 seconds)
    ↓
Total: 2-3 minutes
```

**Error Handling:**
- Validates input files exist
- Checks output files created
- Exits on first failure
- Reports stage-by-stage progress

**Usage:**
```bash
python run_full_analysis.py
```

---

## Dependencies

### Core Dependencies

```
pandas==2.1.4         # Data manipulation
numpy==1.26.2         # Numerical operations
matplotlib==3.8.2     # Static visualizations
seaborn==0.13.0       # Statistical charts
plotly==5.18.0        # Interactive charts
streamlit==1.29.0     # Dashboard framework
scipy==1.11.4         # Statistical functions
```

### Installation

```bash
pip install -r requirements.txt
```

---

## Performance Metrics

### Processing Time
- Data Cleaning: 30-45 seconds
- EDA: 45-60 seconds
- Feature Engineering: 15-30 seconds
- Analytical Reasoning: 30-45 seconds
- **Total Pipeline: 2-3 minutes**

### Dataset Sizes
- Raw CSV: ~1MB
- Clean CSV: ~1MB
- Enriched CSV: ~1.5MB
- All outputs: ~5MB total

### Dashboard Performance
- Initial load: 2-3 seconds
- Filter updates: <0.5 seconds
- Page switches: Instant
- Data export: 1-2 seconds

---

## Quality Assurance

### Data Validation Checks

1. **Missing Value Check**: Ensures <1% missing
2. **Duplicate Check**: Removes duplicate customerIDs
3. **Type Validation**: Enforces correct data types
4. **Range Validation**: Checks numeric ranges (tenure 0-72, charges >0)
5. **Category Validation**: Verifies allowed category values

### Feature Validation

1. **Risk Score Validation**: Range 4-11
2. **Segment Distribution**: Ensures balanced segments
3. **CLV Calculation**: Matches TotalCharges
4. **Service Count**: Range 0-9

### Output Validation

1. **Report File Existence**: All required reports generated
2. **Visualization Count**: 15-20 charts created
3. **Dashboard Launch**: No errors on startup
4. **Filter Functionality**: All filters operational

---

## Scalability Considerations

### Current Limitations

- **Dataset Size**: Optimized for <100K rows
- **Dashboard**: Single-user local deployment
- **Processing**: Sequential, single-threaded
- **Storage**: File-based (CSV)

### Production Recommendations

**For Larger Datasets (100K+ rows):**
- Migrate to SQL database (PostgreSQL, MySQL)
- Implement data sampling for dashboard
- Add pagination to data tables
- Use Dask for parallel processing

**For Multi-User Deployment:**
- Deploy to Streamlit Cloud or Heroku
- Add user authentication
- Implement session management
- Use Redis for caching

**For Real-Time Data:**
- Connect to live database
- Implement scheduled pipeline runs
- Add incremental processing
- Use Apache Airflow for orchestration

---

## Version History

**Version 1.0** (January 2026)
- Initial release
- Complete 4-stage pipeline
- Interactive dashboard
- Comprehensive documentation

---

## Technical Contact

For technical questions or issues:
- Review README.md for overview
- Check USAGE_GUIDE.md for user instructions
- See DEPLOYMENT.md for deployment help

---

**Last Updated:** January 2026
