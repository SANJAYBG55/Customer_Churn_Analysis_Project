# 📂 Project Structure

## Directory Organization

```
customer_churn_analysis/
│
├── data/                           # Data directory
│   ├── raw/                        # Original, immutable data
│   │   └── telco_churn.csv        # Source dataset (7,043 customers, 21 columns)
│   ├── processed/                  # Cleaned and transformed data
│   │   ├── clean_churn_data.csv   # Stage 1 output (cleaned)
│   │   ├── enriched_churn_data.csv # Stage 3 output (with features)
│   │   ├── data_quality_report.txt # Data validation report
│   │   └── feature_dictionary.txt  # Feature definitions
│   └── database/                   # Database files (optional)
│       └── (empty - reserved for SQLite files)
│
├── scripts/                        # Analysis scripts
│   ├── data_cleaning.py           # Stage 1: Data cleaning & validation
│   ├── eda_analysis.py            # Stage 2: Exploratory data analysis
│   ├── feature_engineering.py     # Stage 3: Feature creation
│   ├── analytical_reasoning.py    # Stage 4: Analysis & recommendations
│   ├── centralize_data.py         # Data integration utility
│   ├── data_profiling.py          # Data profiling utility
│   └── dataset_profile.py         # Dataset summary utility
│
├── dashboard/                      # Interactive dashboard
│   └── churn_dashboard.py         # Streamlit dashboard application
│
├── outputs/                        # Analysis outputs
│   ├── reports/                   # Text reports
│   │   ├── data_quality_report.txt         # Stage 1: Data quality
│   │   ├── eda_findings.txt               # Stage 2: EDA insights
│   │   ├── analysis_report.txt            # Stage 4: Full analysis
│   │   ├── business_recommendations.txt   # Stage 4: Recommendations
│   │   ├── executive_summary.txt          # Stage 4: Executive summary
│   │   └── segment_comparison.csv         # Stage 4: Segment table
│   └── visualizations/            # Charts and graphs
│       ├── churn_distribution.png
│       ├── contract_vs_churn.png
│       ├── tenure_distribution.png
│       ├── payment_method_analysis.png
│       ├── service_adoption.png
│       └── (15-20 PNG files from EDA)
│
├── docs/                           # Project documentation
│   └── business_context.md        # Business problem definition
│
├── notebooks/                      # Jupyter notebooks (optional)
│   └── (empty - reserved for exploratory notebooks)
│
├── run_full_analysis.py           # Master automation script
├── requirements.txt               # Python dependencies
├── README.md                      # Project overview
├── USAGE_GUIDE.md                 # Dashboard user guide
├── TECHNICAL_DOCUMENTATION.md     # Technical specifications
├── PROJECT_STRUCTURE.md           # This file
├── DEPLOYMENT.md                  # Deployment instructions
└── Customer Churn Project.md      # Complete learning guide

```

---

## File Descriptions

### Root Level Files

#### run_full_analysis.py
**Purpose:** Master automation script that runs entire analysis pipeline  
**Usage:** `python run_full_analysis.py`  
**Executes:** All 4 analysis stages in sequence  
**Duration:** 2-3 minutes  
**Output:** All reports and processed datasets

#### requirements.txt
**Purpose:** Python package dependencies  
**Usage:** `pip install -r requirements.txt`  
**Contains:** pandas, numpy, matplotlib, seaborn, plotly, streamlit, scipy

#### README.md
**Purpose:** Main project documentation  
**Audience:** Recruiters, portfolio viewers, GitHub visitors  
**Contains:** Project overview, key findings, quick start, skills demonstrated

#### USAGE_GUIDE.md
**Purpose:** Dashboard user manual  
**Audience:** Business users, stakeholders, managers  
**Contains:** How to navigate dashboard, filter data, export lists, use cases

#### TECHNICAL_DOCUMENTATION.md
**Purpose:** Technical specifications  
**Audience:** Data analysts, developers, technical reviewers  
**Contains:** Architecture, data schemas, methodology, code organization

#### PROJECT_STRUCTURE.md
**Purpose:** Directory organization guide  
**Audience:** Developers, collaborators, new team members  
**Contains:** File structure, descriptions, navigation

#### DEPLOYMENT.md
**Purpose:** Deployment instructions  
**Audience:** DevOps, engineers, anyone deploying to production  
**Contains:** Step-by-step deployment to Streamlit Cloud, Heroku, Docker

#### Customer Churn Project.md
**Purpose:** Complete learning guide (9 stages)  
**Audience:** Learners, students, anyone replicating project  
**Contains:** Full walkthrough, explanations, code, tests

---

### data/ Directory

#### data/raw/
**Purpose:** Original, immutable source data  
**Rule:** NEVER modify files in this folder  
**Contents:** `telco_churn.csv` (7,043 rows, 21 columns)

#### data/processed/
**Purpose:** Cleaned and transformed datasets  
**Contents:**
- `clean_churn_data.csv` - Output of Stage 1 (cleaned data)
- `enriched_churn_data.csv` - Output of Stage 3 (with engineered features)
- `data_quality_report.txt` - Data validation report
- `feature_dictionary.txt` - Feature documentation

#### data/database/
**Purpose:** Reserved for SQLite or other database files  
**Current Status:** Empty (CSV-based project)  
**Future Use:** Production database files

---

### scripts/ Directory

**Purpose:** Modular Python scripts for each analysis stage

#### data_cleaning.py
**Stage:** 1  
**Input:** `data/raw/telco_churn.csv`  
**Output:** `data/processed/clean_churn_data.csv`  
**Functions:**
- Handle missing values
- Convert data types
- Remove duplicates
- Validate data quality

**Usage:** `python scripts/data_cleaning.py`

#### eda_analysis.py
**Stage:** 2  
**Input:** `data/processed/clean_churn_data.csv`  
**Output:** 
- `outputs/reports/eda_findings.txt`
- `outputs/visualizations/*.png` (15-20 charts)

**Functions:**
- Statistical summaries
- Distribution analysis
- Correlation analysis
- Visualization generation
- Hypothesis formation

**Usage:** `python scripts/eda_analysis.py`

#### feature_engineering.py
**Stage:** 3  
**Input:** `data/processed/clean_churn_data.csv`  
**Output:** `data/processed/enriched_churn_data.csv`  
**Functions:**
- Calculate CLV, ARPU
- Create risk scores
- Build segments (Risk, Value, Tenure)
- Compute engagement metrics

**Usage:** `python scripts/feature_engineering.py`

#### analytical_reasoning.py
**Stage:** 4  
**Input:** `data/processed/enriched_churn_data.csv`  
**Output:** 
- `outputs/reports/analysis_report.txt`
- `outputs/reports/business_recommendations.txt`
- `outputs/reports/executive_summary.txt`
- `outputs/reports/segment_comparison.csv`

**Functions:**
- Validate hypotheses
- Analyze segments
- Quantify churn drivers
- Generate recommendations

**Usage:** `python scripts/analytical_reasoning.py`

#### Supporting Scripts

**centralize_data.py**
- Utility for data integration (if multiple sources)
- Not required for single-CSV project

**data_profiling.py**
- Quick data profiling utility
- Generates summary statistics

**dataset_profile.py**
- Dataset overview generator
- Alternative to EDA for quick insights

---

### dashboard/ Directory

#### churn_dashboard.py
**Purpose:** Interactive Streamlit dashboard application  
**Pages:** 5 (Executive Overview, Segment Analysis, Churn Drivers, Recommendations, Customer Explorer)  
**Input:** `data/processed/enriched_churn_data.csv`  
**Usage:** `streamlit run dashboard/churn_dashboard.py`  
**Access:** `http://localhost:8501`

**Features:**
- Interactive filtering
- Real-time visualizations
- Data export
- Multi-page navigation

---

### outputs/ Directory

#### outputs/reports/
**Purpose:** Text-based analysis reports

**data_quality_report.txt**
- Data shape, types
- Missing value summary
- Duplicate check
- Quality assessment

**eda_findings.txt**
- Statistical summaries
- Distribution analysis
- Churn rate breakdowns
- Correlation findings
- Hypotheses generated

**analysis_report.txt**
- Hypothesis validation
- Segment profiling
- Churn driver quantification
- Business impact calculations

**business_recommendations.txt**
- 5 detailed recommendations
- Implementation timelines
- Expected outcomes
- Priority rankings

**executive_summary.txt**
- High-level overview
- Top findings
- Top recommendations
- Next steps

**segment_comparison.csv**
- Segment statistics table
- Churn rates by segment
- Customer counts
- Exportable format

#### outputs/visualizations/
**Purpose:** Static charts and graphs (PNG files)

**Generated Charts:**
- Churn distribution
- Contract type vs churn
- Tenure distribution
- Payment method analysis
- Service adoption charts
- Value segment comparison
- Risk segment profiles
- Correlation heatmaps
- (15-20 total PNG files)

---

### docs/ Directory

#### business_context.md
**Purpose:** Business problem definition and context  
**Contains:**
- Industry background
- Business problem
- Project goals
- Success criteria

---

### notebooks/ Directory

**Purpose:** Jupyter notebooks for exploratory work  
**Current Status:** Empty (optional)  
**Use Case:** Ad-hoc analysis, experimentation, prototyping

---

## Navigation Guide

### For Business Users

**Want to see key findings?**
→ Read `README.md` or `outputs/reports/executive_summary.txt`

**Want to explore data?**
→ Run `streamlit run dashboard/churn_dashboard.py`

**Want to export customer lists?**
→ Use dashboard's Customer Explorer page

### For Data Analysts

**Want to understand methodology?**
→ Read `TECHNICAL_DOCUMENTATION.md`

**Want to modify analysis?**
→ Edit scripts in `scripts/` directory

**Want to see code?**
→ Check `scripts/` for modular scripts

**Want to run full pipeline?**
→ Execute `python run_full_analysis.py`

### For Developers

**Want to understand structure?**
→ Read this file (`PROJECT_STRUCTURE.md`)

**Want to set up environment?**
→ Install from `requirements.txt`

**Want to deploy?**
→ Follow `DEPLOYMENT.md`

**Want to contribute?**
→ Follow structure, add to appropriate directory

### For Learners

**Want to learn process?**
→ Follow `Customer Churn Project.md` (9 stages)

**Want to see outputs?**
→ Check `outputs/` directory

**Want to replicate?**
→ Run `python run_full_analysis.py`

---

## File Size Reference

| File/Directory | Approximate Size | Notes |
|----------------|------------------|-------|
| data/raw/telco_churn.csv | ~1 MB | Original dataset |
| data/processed/*.csv | ~2.5 MB total | Clean + enriched |
| outputs/reports/*.txt | ~100 KB total | Text reports |
| outputs/visualizations/*.png | ~3 MB total | 15-20 charts |
| scripts/*.py | ~200 KB total | Python scripts |
| dashboard/churn_dashboard.py | ~50 KB | Dashboard app |
| **Total Project Size** | **~7-10 MB** | Lightweight |

---

## Adding New Files

### Adding a New Analysis Script

**Location:** `scripts/new_analysis.py`

**Template:**
```python
"""
NEW ANALYSIS SCRIPT
Description of what this script does
"""

import pandas as pd

# Load data
df = pd.read_csv("data/processed/enriched_churn_data.csv")

# Perform analysis
# ...

# Save output
df.to_csv("outputs/new_output.csv", index=False)
print("Analysis complete!")
```

### Adding a New Report

**Location:** `outputs/reports/new_report.txt`

**Generated by:** Analysis script

**Format:** Plain text with clear sections

### Adding a New Visualization

**Location:** `outputs/visualizations/new_chart.png`

**Generated by:** EDA or analysis script

**Format:** PNG (1200x800px recommended)

### Adding Documentation

**Location:** Root level (`.md` file)

**Naming Convention:** UPPERCASE_WITH_UNDERSCORES.md

**Examples:** `CONTRIBUTING.md`, `CHANGELOG.md`

---

## Maintenance Guidelines

### What to Version Control (Git)

✅ **Include:**
- All Python scripts (`scripts/`, `dashboard/`)
- All documentation (`.md` files)
- `requirements.txt`
- `run_full_analysis.py`
- Sample data (small datasets only)

❌ **Exclude (.gitignore):**
- Large data files (`data/raw/*.csv` if >10MB)
- Output files (`outputs/`)
- Cache files (`__pycache__/`, `.ipynb_checkpoints/`)
- Environment files (`.env`, `venv/`)

### What to Backup

**Critical:**
- `data/raw/` (source data)
- `scripts/` (all analysis code)
- Documentation files

**Optional:**
- `outputs/` (can be regenerated)
- `data/processed/` (can be regenerated)

### Cleaning Up

**Safe to Delete:**
- `outputs/` (regenerate with scripts)
- `data/processed/` (regenerate with pipeline)
- `__pycache__/` (Python cache)

**Never Delete:**
- `data/raw/` (source data)
- `scripts/` (analysis code)
- `dashboard/` (dashboard code)
- Documentation files

---

## Troubleshooting

### "File Not Found" Error

**Check:**
1. Are you in project root directory?
2. Did you run previous stages?
3. Are file paths correct?

**Solution:**
```bash
cd path/to/customer_churn_analysis
python run_full_analysis.py
```

### "Module Not Found" Error

**Check:** Dependencies installed?

**Solution:**
```bash
pip install -r requirements.txt
```

### Missing Output Files

**Check:** Did analysis scripts complete successfully?

**Solution:**
```bash
python run_full_analysis.py
```

---

**Last Updated:** January 2026
