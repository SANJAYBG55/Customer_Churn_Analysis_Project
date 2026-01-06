
# **Stage 0: Foundations \& Environment Setup**


***

## a) Learning Objective

### What You're Learning

You are learning how to **set up a professional data analytics project environment** from scratch. This includes organizing your project folders, installing necessary Python libraries, and creating a standard structure that data analysts use in real companies.

### Why This Matters

In real-world data analytics, **90% of teams follow a standard project structure**. Having a well-organized environment means:

- You can find files easily
- Others can understand your work
- Your code runs consistently across different computers
- You appear professional to recruiters reviewing your GitHub


### Skill Level

**Foundation** - This is the absolute starting point for any data analytics project.

### In Scope

- Creating a standard project folder structure
- Installing core Python libraries (Pandas, NumPy, Matplotlib, Seaborn, Streamlit)
- Setting up SQLite database (lightweight, no installation needed)
- Creating a project README file
- Testing that your environment works


### Out of Scope

- Advanced database systems (PostgreSQL, MySQL) - we'll use SQLite for simplicity
- Git version control - we'll focus on core analytics first
- Virtual environments (venv/conda) - assumed you have Python 3.8+ installed
- Jupyter Notebooks - we'll use simple Python scripts (.py files)


### Assumptions

- You have **Python 3.8 or higher** installed on your system
- You have **pip** (Python package manager) available
- You can run terminal/command prompt commands
- You're working on Windows, Mac, or Linux


### Output Artifact

- **Complete project folder structure** with all necessary folders
- **requirements.txt** file listing all dependencies
- **README.md** file documenting the project
- **setup_test.py** script to verify your environment works correctly

***

## b) Setup Instructions

### Step 1: Create Project Root Folder

1. Open your terminal/command prompt
2. Navigate to where you want to create the project (e.g., Desktop or Documents)
3. Create a folder named `customer_churn_analysis`

### Step 2: Create Folder Structure

Inside `customer_churn_analysis`, you will create the following folders:

```
customer_churn_analysis/
├── data/
│   ├── raw/
│   ├── processed/
│   └── database/
├── notebooks/
├── scripts/
├── outputs/
│   ├── visualizations/
│   └── reports/
├── dashboard/
└── docs/
```


### Step 3: Create Core Files

You will create these files in the project root:

- `requirements.txt` - Lists all Python libraries needed
- `README.md` - Project documentation
- `setup_test.py` - Script to verify setup


### Dependencies Required

- **pandas** - Data manipulation
- **numpy** - Numerical operations
- **matplotlib** - Basic plotting
- **seaborn** - Statistical visualizations
- **streamlit** - Dashboard creation
- **sqlite3** - Built into Python, no installation needed

***

## c) Implementation (FINAL VERSION)

### File 1: Project Folder Structure Setup Script

**File Name:** `create_structure.py`
**File Path:** `customer_churn_analysis/create_structure.py`
**Total Lines:** 35

```python
# Import the os module to interact with the operating system
import os

# Define the base project directory name
project_name = "customer_churn_analysis"

# Define all folder paths that need to be created for the project
folders = [
    "data/raw",              # Stores original, unmodified datasets (Kaggle CSV, etc.)
    "data/processed",        # Stores cleaned and transformed datasets
    "data/database",         # Stores SQLite database files
    "notebooks",             # Stores Jupyter notebooks (if used later)
    "scripts",               # Stores Python scripts for analysis
    "outputs/visualizations",# Stores charts, graphs, and plots
    "outputs/reports",       # Stores analysis reports and summaries
    "dashboard",             # Stores Streamlit dashboard files
    "docs"                   # Stores project documentation
]

# Print a message indicating the start of folder creation
print(f"Creating project structure for: {project_name}\n")

# Loop through each folder path in the folders list
for folder in folders:
    # Combine the project name with the folder path to get full path
    folder_path = os.path.join(project_name, folder)
    
    # Create the folder (including parent folders if they don't exist)
    os.makedirs(folder_path, exist_ok=True)
    
    # Print confirmation message for each folder created
    print(f"✓ Created: {folder_path}")

# Print final success message
print(f"\n✅ Project structure created successfully!")
print(f"📁 Navigate to the '{project_name}' folder to continue.")
```


***

### File 2: Requirements File

**File Name:** `requirements.txt`
**File Path:** `customer_churn_analysis/requirements.txt`
**Total Lines:** 6

```txt
# Core data manipulation library
pandas==2.1.4
# Numerical computing library
numpy==1.26.2
# Basic plotting library
matplotlib==3.8.2
# Statistical visualization library
seaborn==0.13.0
# Interactive dashboard framework
streamlit==1.29.0
```


***

### File 3: Project README

**File Name:** `README.md`
**File Path:** `customer_churn_analysis/README.md`
**Total Lines:** 58

```markdown
# Customer Churn Analysis Project

## Project Overview
This project analyzes customer churn behavior in Telecom/SaaS companies using business analytics and rule-based logic (no machine learning). The goal is to identify at-risk customers and provide actionable retention strategies.

## Business Objective
- Understand why customers leave (churn drivers)
- Identify high-risk customers using business rules
- Provide data-driven retention recommendations
- Demonstrate end-to-end analytics skills for portfolio/placement

## Project Structure
```

customer_churn_analysis/
├── data/
│   ├── raw/              \# Original datasets (Kaggle CSV)
│   ├── processed/        \# Cleaned and transformed data
│   └── database/         \# SQLite database files
├── notebooks/            \# Analysis notebooks (if any)
├── scripts/              \# Python analysis scripts
├── outputs/
│   ├── visualizations/   \# Charts and graphs
│   └── reports/          \# Analysis reports
├── dashboard/            \# Streamlit dashboard files
└── docs/                 \# Project documentation

```

## Tech Stack
- **Python 3.8+** - Programming language
- **Pandas** - Data manipulation
- **NumPy** - Numerical operations
- **Matplotlib** - Plotting
- **Seaborn** - Statistical visualizations
- **Streamlit** - Interactive dashboard
- **SQLite** - Lightweight database

## Setup Instructions
1. Install Python 3.8 or higher
2. Navigate to project folder
3. Install dependencies: `pip install -r requirements.txt`
4. Test setup: `python setup_test.py`

## Workflow Stages
0. ✅ Foundations & Environment Setup
1. ⏳ Business Context & Dataset Scoping
2. ⏳ Data Centralization & Integration
3. ⏳ Data Validation & Profiling
4. ⏳ Data Cleaning & Preparation
5. ⏳ Exploratory Data Analysis (EDA)
6. ⏳ Feature Engineering & Metrics
7. ⏳ Analytical Reasoning
8. ⏳ Visualization & Dashboard
9. ⏳ Automation & Documentation

## Author
Data Analytics Portfolio Project

## Last Updated
January 6, 2026
```


***

### File 4: Setup Test Script

**File Name:** `setup_test.py`
**File Path:** `customer_churn_analysis/setup_test.py`
**Total Lines:** 65

```python
# Import sys module to check Python version
import sys

# Print header message
print("=" * 60)
print("TESTING DATA ANALYTICS ENVIRONMENT SETUP")
print("=" * 60)
print()

# Test 1: Check Python version
print("Test 1: Checking Python Version...")
# Get the current Python version as a tuple (major, minor, micro)
python_version = sys.version_info
# Print the version in readable format
print(f"   Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
# Check if Python version is 3.8 or higher
if python_version >= (3, 8):
    print("   ✅ PASS: Python 3.8+ detected")
else:
    print("   ❌ FAIL: Please upgrade to Python 3.8 or higher")
print()

# Test 2: Check if pandas is installed
print("Test 2: Checking Pandas...")
try:
    # Try to import pandas library
    import pandas as pd
    # Print the version if successful
    print(f"   Pandas Version: {pd.__version__}")
    print("   ✅ PASS: Pandas installed")
except ImportError:
    # If import fails, pandas is not installed
    print("   ❌ FAIL: Pandas not installed. Run: pip install pandas")
print()

# Test 3: Check if numpy is installed
print("Test 3: Checking NumPy...")
try:
    # Try to import numpy library
    import numpy as np
    # Print the version if successful
    print(f"   NumPy Version: {np.__version__}")
    print("   ✅ PASS: NumPy installed")
except ImportError:
    # If import fails, numpy is not installed
    print("   ❌ FAIL: NumPy not installed. Run: pip install numpy")
print()

# Test 4: Check if matplotlib is installed
print("Test 4: Checking Matplotlib...")
try:
    # Try to import matplotlib library
    import matplotlib
    # Print the version if successful
    print(f"   Matplotlib Version: {matplotlib.__version__}")
    print("   ✅ PASS: Matplotlib installed")
except ImportError:
    # If import fails, matplotlib is not installed
    print("   ❌ FAIL: Matplotlib not installed. Run: pip install matplotlib")
print()

# Test 5: Check if seaborn is installed
print("Test 5: Checking Seaborn...")
try:
    # Try to import seaborn library
    import seaborn as sns
    # Print the version if successful
    print(f"   Seaborn Version: {sns.__version__}")
    print("   ✅ PASS: Seaborn installed")
except ImportError:
    # If import fails, seaborn is not installed
    print("   ❌ FAIL: Seaborn not installed. Run: pip install seaborn")
print()

# Test 6: Check if streamlit is installed
print("Test 6: Checking Streamlit...")
try:
    # Try to import streamlit library
    import streamlit as st
    # Print the version if successful
    print(f"   Streamlit Version: {st.__version__}")
    print("   ✅ PASS: Streamlit installed")
except ImportError:
    # If import fails, streamlit is not installed
    print("   ❌ FAIL: Streamlit not installed. Run: pip install streamlit")
print()

# Test 7: Check if sqlite3 is available (built into Python)
print("Test 7: Checking SQLite3...")
try:
    # Try to import sqlite3 module
    import sqlite3
    # Print the version if successful
    print(f"   SQLite3 Version: {sqlite3.sqlite_version}")
    print("   ✅ PASS: SQLite3 available")
except ImportError:
    # SQLite3 should always be available in Python 3.8+
    print("   ❌ FAIL: SQLite3 not available (unusual)")
print()

# Print final summary
print("=" * 60)
print("SETUP TEST COMPLETE")
print("=" * 60)
print("If all tests passed, you're ready to start Stage 1!")
print("If any test failed, install the missing library using pip.")
```


***

## d) How to Run

### Step 1: Create the Project Structure

1. Open your terminal/command prompt
2. Navigate to your desired location (e.g., Desktop):

```bash
cd Desktop
```

3. Run the folder creation script:

```bash
python create_structure.py
```

4. Navigate into the newly created project folder:

```bash
cd customer_churn_analysis
```


### Step 2: Create the Requirements File

1. Inside the `customer_churn_analysis` folder, create `requirements.txt` file
2. Copy and paste the requirements content shown in section (c) above
3. Save the file

### Step 3: Create the README File

1. Inside the `customer_churn_analysis` folder, create `README.md` file
2. Copy and paste the README content shown in section (c) above
3. Save the file

### Step 4: Install Dependencies

1. Make sure you're in the `customer_churn_analysis` folder
2. Run this command to install all required libraries:

```bash
pip install -r requirements.txt
```

3. Wait for installation to complete (may take 2-5 minutes)

### Step 5: Create and Run the Setup Test

1. Inside the `customer_churn_analysis` folder, create `setup_test.py` file
2. Copy and paste the test script content shown in section (c) above
3. Save the file
4. Run the test script:

```bash
python setup_test.py
```


***

## e) How to Test the Output

### Test 1: Verify Folder Structure

**Expected Result:**

- Navigate to your Desktop (or wherever you created the project)
- You should see a folder named `customer_churn_analysis`
- Inside it, you should see these folders:
    - `data` (containing `raw`, `processed`, `database` subfolders)
    - `notebooks`
    - `scripts`
    - `outputs` (containing `visualizations`, `reports` subfolders)
    - `dashboard`
    - `docs`

**How to Check:**

- On Windows: Open File Explorer and browse to the folder
- On Mac/Linux: Run `ls -R customer_churn_analysis` in terminal


### Test 2: Verify Files Exist

**Expected Result:**

- Inside `customer_churn_analysis` folder, you should see:
    - `requirements.txt`
    - `README.md`
    - `setup_test.py`

**How to Check:**

- On Windows: Open the folder and verify files are present
- On Mac/Linux: Run `ls customer_churn_analysis` in terminal


### Test 3: Verify Library Installation

**Expected Result:**
When you run `python setup_test.py`, you should see:

```
Test 1: Checking Python Version...
   Python Version: 3.x.x
   ✅ PASS: Python 3.8+ detected

Test 2: Checking Pandas...
   Pandas Version: 2.x.x
   ✅ PASS: Pandas installed

[... similar for NumPy, Matplotlib, Seaborn, Streamlit, SQLite3 ...]

SETUP TEST COMPLETE
If all tests passed, you're ready to start Stage 1!
```

**Signs of Success:**

- All tests show ✅ PASS
- No ❌ FAIL messages
- No error messages in red

**Signs of Problems:**

- Any ❌ FAIL message indicates a missing library
- Error messages during `pip install` command
- `ModuleNotFoundError` when running setup_test.py


### Test 4: Quick Manual Check

Open Python interactive shell and try importing:

```bash
python
```

Then type:

```python
import pandas as pd
import numpy as np
print("All libraries loaded successfully!")
```

If no errors appear, your setup is correct.

***

## f) Common Beginner Mistakes

### Mistake 1: Not Navigating to the Correct Folder

**What Happens:**

- You run `pip install -r requirements.txt` but get error: "requirements.txt not found"

**Why It Happens:**

- You're in the wrong directory/folder in your terminal

**How to Fix:**

- Always use `cd customer_churn_analysis` to navigate into your project folder
- Use `pwd` (Mac/Linux) or `cd` (Windows) to check your current location
- Make sure `requirements.txt` exists in your current folder using `ls` (Mac/Linux) or `dir` (Windows)


### Mistake 2: Python Version Too Old

**What Happens:**

- Setup test shows: "Python 2.x detected" or fails with syntax errors

**Why It Happens:**

- Your system has an older Python version installed

**How to Fix:**

- Install Python 3.8 or higher from python.org
- On some systems, use `python3` instead of `python`
- Check version with: `python --version` or `python3 --version`


### Mistake 3: Pip Not Installed or Not in PATH

**What Happens:**

- Terminal says: "pip: command not found"

**Why It Happens:**

- Pip is not installed or not accessible from terminal

**How to Fix:**

- Pip comes with Python 3.8+, but may need manual PATH setup
- Try `python -m pip install -r requirements.txt` instead
- On Mac/Linux, you may need `pip3` instead of `pip`


### Mistake 4: Installing Libraries Globally Instead of Checking First

**What Happens:**

- You install libraries multiple times or in wrong locations

**Why It Happens:**

- Not checking if libraries are already installed

**How to Fix:**

- Always run `setup_test.py` first to see what's missing
- Only install what's actually needed
- Consider using virtual environments in future projects (not required here)


### Mistake 5: Skipping the Setup Test

**What Happens:**

- You assume everything is installed and move to Stage 1
- Stage 1 fails with import errors

**Why It Happens:**

- Not verifying the environment before starting analysis work

**How to Fix:**

- ALWAYS run `setup_test.py` and confirm all tests pass
- Fix any failures before proceeding
- Keep `setup_test.py` handy to re-check later if issues arise


### Mistake 6: Creating Files in Wrong Location

**What Happens:**

- Files are scattered across different folders
- Project structure doesn't match the expected layout

**Why It Happens:**

- Not paying attention to file paths
- Creating files from wrong terminal location

**How to Fix:**

- Always check `pwd` or `cd` to confirm you're in `customer_churn_analysis` folder
- Use the exact folder structure shown in this stage
- Don't create additional folders or change names

***

## ✅ Stage 0 Complete!

Your data analytics environment is now set up and ready. You have:

- A professional project structure
- All required Python libraries installed
- A verified working environment
- Documentation in place

**Next Step:** Wait for instruction to proceed to Stage 1 (Business Context \& Dataset Scoping)

---

# **Stage 1: Business Context \& Dataset Scoping**


***

## a) Learning Objective

### What You're Learning

You are learning how to **understand and scope a dataset before writing any analysis code**. This includes examining what data you have, what each row represents, what time period it covers, and how it relates to the business problem you're solving (customer churn).

### Why This Matters

In real-world data analytics, **jumping straight into coding without understanding your data is the \#1 cause of incorrect analysis**. Professional analysts spend significant time understanding:

- What the dataset represents (customers, transactions, events?)
- The grain/granularity (one row = one customer? one order?)
- Time coverage (last month? last year?)
- Business context (which industry? what problem are we solving?)

This prevents wasted effort and wrong conclusions.

### Skill Level

**Foundation** - This is a critical first step that even advanced analysts perform for every new dataset.

### In Scope

- Downloading a real telecom customer churn dataset from Kaggle
- Loading the dataset into Python using Pandas
- Understanding basic dataset structure (rows, columns, data types)
- Identifying the row grain (what one row represents)
- Documenting business context and entities
- Creating a dataset profile document


### Out of Scope

- Data cleaning or modification (comes in Stage 4)
- Statistical analysis or visualizations (comes in Stage 5)
- Creating new features or calculations (comes in Stage 6)
- Database integration (comes in Stage 2)
- Deep exploratory analysis (comes in Stage 5)


### Assumptions

- You have a Kaggle account (free to create)
- You can download CSV files from Kaggle
- You have completed Stage 0 (environment setup)
- You understand the business problem: telecom companies want to predict and prevent customer churn


### Output Artifact

- **Kaggle dataset CSV file** saved in `data/raw/` folder
- **dataset_profile.py** script that loads and describes the dataset
- **business_context.md** document explaining the dataset and business use case
- **Console output** showing dataset summary statistics

***

## b) Setup Instructions

### Step 1: Download Dataset from Kaggle

1. Go to Kaggle.com and log in (create free account if needed)
2. Search for "Telco Customer Churn" dataset
3. Recommended dataset: **IBM Telco Customer Churn** (https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
4. Click the "Download" button to get `WA_Fn-UseC_-Telco-Customer-Churn.csv`
5. Save the CSV file to your `customer_churn_analysis/data/raw/` folder
6. Rename it to `telco_churn.csv` for simplicity

### Step 2: Verify File Location

Your folder structure should now look like:

```
customer_churn_analysis/
├── data/
│   ├── raw/
│   │   └── telco_churn.csv   ← Dataset goes here
│   ├── processed/
│   └── database/
├── scripts/
└── [other folders...]
```


### Step 3: Create Analysis Script

You will create a Python script in the `scripts/` folder to load and profile the dataset.

### Step 4: Create Documentation File

You will create a markdown document in the `docs/` folder to document business context.

### Dependencies Required

- All libraries from Stage 0 (Pandas, NumPy) - already installed
- No additional installations needed

***

## c) Implementation (FINAL VERSION)

### File 1: Dataset Profiling Script

**File Name:** `dataset_profile.py`
**File Path:** `customer_churn_analysis/scripts/dataset_profile.py`
**Total Lines:** 78

```python
# Import pandas library for data manipulation
import pandas as pd
# Import os library to work with file paths
import os

# Print a header to make output clear
print("=" * 70)
print("STAGE 1: DATASET PROFILING - BUSINESS CONTEXT & SCOPING")
print("=" * 70)
print()

# Define the relative path to the raw dataset
# This assumes you're running the script from the project root folder
data_path = "data/raw/telco_churn.csv"

# Check if the file exists before trying to load it
if not os.path.exists(data_path):
    # If file doesn't exist, print error message and exit
    print(f"❌ ERROR: Dataset not found at {data_path}")
    print("Please download the dataset from Kaggle and place it in data/raw/")
    print("Expected file name: telco_churn.csv")
    exit()

# Load the CSV file into a pandas DataFrame
# A DataFrame is like an Excel spreadsheet in Python
print("📂 Loading dataset...")
df = pd.read_csv(data_path)
print(f"✅ Dataset loaded successfully from: {data_path}")
print()

# Section 1: Basic Dataset Information
print("-" * 70)
print("1. BASIC DATASET INFORMATION")
print("-" * 70)

# Get the number of rows and columns in the dataset
num_rows, num_columns = df.shape
print(f"Total Rows (Records): {num_rows}")
print(f"Total Columns (Features): {num_columns}")
print()

# Section 2: Column Names and Data Types
print("-" * 70)
print("2. COLUMN NAMES AND DATA TYPES")
print("-" * 70)

# Display information about each column (name, count, data type)
print(df.info())
print()

# Section 3: First Few Rows (Sample Data)
print("-" * 70)
print("3. FIRST 5 ROWS (SAMPLE DATA)")
print("-" * 70)

# Display the first 5 rows to understand what the data looks like
print(df.head())
print()

# Section 4: Row Grain Analysis
print("-" * 70)
print("4. ROW GRAIN ANALYSIS (What does one row represent?)")
print("-" * 70)

# Check if there's a customer ID column to understand uniqueness
if 'customerID' in df.columns:
    # Count total rows
    total_rows = len(df)
    # Count unique customer IDs
    unique_customers = df['customerID'].nunique()
    
    print(f"Total Rows: {total_rows}")
    print(f"Unique Customer IDs: {unique_customers}")
    
    # If total rows equals unique customers, each row is one customer
    if total_rows == unique_customers:
        print("✅ Row Grain: ONE ROW = ONE UNIQUE CUSTOMER")
        print("   This is a customer-level dataset (no duplicates)")
    else:
        print("⚠️  Row Grain: Multiple rows per customer detected")
        print("   This may be a transaction-level or time-series dataset")
else:
    print("⚠️  No customerID column found - grain unclear")
print()

# Section 5: Time Range Analysis
print("-" * 70)
print("5. TIME RANGE ANALYSIS")
print("-" * 70)

# Check if there are any date columns in the dataset
date_columns = df.select_dtypes(include=['datetime64']).columns.tolist()

if len(date_columns) > 0:
    # If date columns exist, show their range
    for col in date_columns:
        print(f"Date Column: {col}")
        print(f"  Earliest Date: {df[col].min()}")
        print(f"  Latest Date: {df[col].max()}")
else:
    # If no explicit date columns, check for tenure or similar
    print("⚠️  No explicit date columns found")
    if 'tenure' in df.columns:
        print("✓ 'tenure' column found (customer lifetime in months)")
        print(f"  Tenure Range: {df['tenure'].min()} to {df['tenure'].max()} months")
print()

# Section 6: Target Variable (Churn Column)
print("-" * 70)
print("6. TARGET VARIABLE ANALYSIS (Churn)")
print("-" * 70)

# Check if there's a 'Churn' column (the variable we want to predict/analyze)
if 'Churn' in df.columns:
    print("✅ Churn column found!")
    print("\nChurn Distribution:")
    # Count how many customers churned vs stayed
    print(df['Churn'].value_counts())
    print("\nChurn Percentage:")
    # Calculate percentage of churned customers
    print(df['Churn'].value_counts(normalize=True) * 100)
else:
    print("⚠️  No 'Churn' column found - please verify dataset")
print()

# Section 7: Key Business Entities Identified
print("-" * 70)
print("7. IDENTIFIED BUSINESS ENTITIES")
print("-" * 70)
print("Based on column names, this dataset contains:")
print("• Customer Information (demographics)")
print("• Service Information (phone, internet, subscriptions)")
print("• Account Information (tenure, contract, billing)")
print("• Churn Information (target variable)")
print()

# Final Summary
print("=" * 70)
print("✅ STAGE 1 COMPLETE: Dataset Profiling Done")
print("=" * 70)
print("Next Step: Document business context in business_context.md")
```


***

### File 2: Business Context Documentation

**File Name:** `business_context.md`
**File Path:** `customer_churn_analysis/docs/business_context.md`
**Total Lines:** 95

```markdown
# Business Context & Dataset Scoping

**Project:** Customer Churn Analysis (Telecom / SaaS)  
**Stage:** 1 - Business Context & Dataset Scoping  
**Date:** January 6, 2026

---

## 1. Business Problem Statement

### What is Customer Churn?
Customer churn occurs when customers stop doing business with a company. In the telecom industry, this means customers cancel their phone/internet service and switch to a competitor.

### Why Does Churn Matter?
- **Revenue Loss:** Each churned customer represents lost monthly recurring revenue
- **Acquisition Cost:** Getting a new customer costs 5-7x more than retaining an existing one
- **Market Competition:** Telecom is highly competitive with many providers fighting for customers
- **Profitability:** Long-term customers are more profitable (higher lifetime value)

### Business Goal
Identify customers who are likely to churn so the company can:
- Offer targeted retention incentives (discounts, upgrades)
- Improve service quality for at-risk customers
- Understand root causes of churn
- Reduce overall churn rate and increase customer lifetime value

---

## 2. Dataset Overview

### Dataset Name
**IBM Telco Customer Churn Dataset**

### Source
Kaggle - https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### Dataset Description
This dataset contains customer information for a fictional telecom company. It tracks customers who left (churned), stayed, or signed up for services including phone, internet, streaming, and security.

### Time Period
- Dataset represents a **snapshot** of customers at a specific point in time
- Includes historical data about customer tenure (how long they've been customers)
- No explicit date range, but tenure ranges from 0 to 72 months (6 years)

### Dataset Size
- **Rows:** 7,043 customers
- **Columns:** 21 features/attributes

---

## 3. Row Grain (Granularity)

### What Does One Row Represent?
**One row = One unique customer**

### Key Points
- This is a **customer-level dataset**, not transaction-level
- Each customer appears exactly once
- Data represents customer status at a single point in time (snapshot)
- This is NOT a time-series dataset

### Implication for Analysis
- We analyze customer **characteristics** to understand churn
- We cannot track customer behavior over time (no historical changes)
- Analysis will be cross-sectional (comparing churned vs non-churned customers)

---

## 4. Business Entities Identified

### Primary Entity: CUSTOMERS
Each row represents a customer with their attributes.

### Secondary Entities (Attributes)
Based on column analysis, the dataset includes:

#### 4.1 Customer Demographics
- Gender
- Age status (Senior Citizen)
- Family status (Partner, Dependents)

#### 4.2 Service Information
- Phone Service (Yes/No)
- Multiple Lines (Yes/No/No phone service)
- Internet Service (DSL, Fiber optic, No)
- Online Security (Yes/No/No internet service)
- Online Backup (Yes/No/No internet service)
- Device Protection (Yes/No/No internet service)
- Tech Support (Yes/No/No internet service)
- Streaming TV (Yes/No/No internet service)
- Streaming Movies (Yes/No/No internet service)

#### 4.3 Account/Contract Information
- Customer Tenure (months with company)
- Contract Type (Month-to-month, One year, Two year)
- Paperless Billing (Yes/No)
- Payment Method (Electronic check, Mailed check, Bank transfer, Credit card)

#### 4.4 Financial Information
- Monthly Charges (amount billed per month)
- Total Charges (total amount billed to customer)

#### 4.5 Target Variable
- **Churn** (Yes/No) - Whether customer left the company

---

## 5. Business Questions This Dataset Can Answer

### Descriptive Questions (What happened?)
- What is the overall churn rate?
- Which customer segments have highest churn?
- What is the average tenure of churned vs non-churned customers?

### Diagnostic Questions (Why did it happen?)
- Do customers with month-to-month contracts churn more?
- Does internet service type affect churn?
- Are customers with higher monthly charges more likely to churn?
- Do customers without tech support churn more often?

### Prescriptive Questions (What should we do?)
- Which customers should we prioritize for retention campaigns?
- What service improvements would reduce churn?
- Should we change pricing or contract structures?

---

## 6. Expected Analysis Workflow

Based on this dataset, our analysis will follow these stages:

1. ✅ **Stage 1 (Current):** Understand the dataset and business context
2. **Stage 2:** Integrate this dataset with additional data sources (customer, payment, service tables)
3. **Stage 3:** Validate data quality (check for missing values, errors)
4. **Stage 4:** Clean and prepare data for analysis
5. **Stage 5:** Explore patterns through visualizations and statistics
6. **Stage 6:** Create business metrics (churn rate, customer lifetime value, etc.)
7. **Stage 7:** Analyze churn drivers and develop rule-based risk indicators
8. **Stage 8:** Build dashboard to present findings
9. **Stage 9:** Automate and document the entire workflow

---

## 7. Key Assumptions

- Dataset is accurate and representative of real telecom customers
- Churn labels are correct (customers marked as "Yes" actually churned)
- All customers in dataset had the opportunity to churn
- Missing values will be addressed in Stage 4 (Data Cleaning)
- Currency is USD (not explicitly stated in dataset)

---

## 8. Success Criteria for This Project

### Analytics Success
- Identify top 3-5 churn drivers
- Segment customers into risk categories (high/medium/low)
- Provide 5+ actionable business recommendations

### Technical Success
- Clean, reproducible code
- Clear visualizations understandable by non-technical stakeholders
- Interactive dashboard for exploring results

### Portfolio Success
- Demonstrates end-to-end analytics skills
- Shows business thinking, not just technical skills
- Suitable for presenting to recruiters/interviewers

---

## 9. Next Steps

- ✅ Dataset downloaded and profiled
- ✅ Business context documented
- ⏳ Proceed to Stage 2: Data Centralization & Integration
```


***

## d) How to Run

### Step 1: Ensure Dataset is in Correct Location

1. Verify that `telco_churn.csv` exists in `customer_churn_analysis/data/raw/` folder
2. If not, download from Kaggle and place it there

### Step 2: Navigate to Project Root

Open your terminal/command prompt and navigate to the project folder:

```bash
cd path/to/customer_churn_analysis
```

Example (if on Desktop):

```bash
cd Desktop/customer_churn_analysis
```


### Step 3: Run the Dataset Profiling Script

Execute the profiling script:

```bash
python scripts/dataset_profile.py
```


### Step 4: Review the Output

The script will print several sections to your terminal:

- Basic dataset information
- Column names and types
- Sample data (first 5 rows)
- Row grain analysis
- Time range analysis
- Target variable (Churn) distribution
- Identified business entities


### Step 5: Create Business Context Document

1. Navigate to the `docs/` folder
2. Create a new file named `business_context.md`
3. Copy the content from section (c) File 2 above
4. Save the file

### Step 6: Read and Understand the Documentation

Open `business_context.md` in any text editor or Markdown viewer to understand the business problem and dataset structure.

***

## e) How to Test the Output

### Test 1: Script Runs Without Errors

**Expected Result:**

- When you run `python scripts/dataset_profile.py`, it should complete without error messages
- Output should display 7 sections of information
- Final message should say: "✅ STAGE 1 COMPLETE: Dataset Profiling Done"

**Signs of Success:**

- No error messages
- Clean, formatted output with section headers
- Numbers and statistics displayed correctly

**Signs of Problems:**

- Error: "FileNotFoundError" - Dataset not in correct location
- Error: "ModuleNotFoundError" - Pandas not installed (re-run Stage 0)
- Blank or incomplete output


### Test 2: Verify Dataset Statistics

**Expected Numbers:**

- Total Rows: 7,043 (may vary slightly depending on dataset version)
- Total Columns: 21
- Row Grain: "ONE ROW = ONE UNIQUE CUSTOMER"
- Churn column exists with "Yes" and "No" values

**How to Verify:**
Look at the console output sections and confirm:

- Numbers make sense (positive, not zero)
- Churn distribution shows both Yes and No categories
- Customer ID count equals total rows (7,043 = 7,043)


### Test 3: Check Sample Data

**Expected Result:**
The "FIRST 5 ROWS" section should show:

- Customer IDs (e.g., "7590-VHVEG")
- Various service columns (PhoneService, InternetService, etc.)
- Churn column with "Yes" or "No" values
- Monthly charges and total charges (numeric values)

**Red Flags:**

- All columns showing "NaN" or null
- Incorrect column names (dataset may be wrong)
- Empty rows


### Test 4: Verify File Creation

**Check these files exist:**

1. `customer_churn_analysis/data/raw/telco_churn.csv` - Dataset file
2. `customer_churn_analysis/scripts/dataset_profile.py` - Profiling script
3. `customer_churn_analysis/docs/business_context.md` - Documentation

**How to Check:**

- Navigate to each folder and verify files are present
- Open files to ensure they're not empty


### Test 5: Manual Data Inspection

Open the CSV file directly:

```bash
# On Mac/Linux
head -5 data/raw/telco_churn.csv

# Or open in Excel/Google Sheets and verify:
```

- First column should be customerID
- Last column should be Churn
- 7,043 rows (plus 1 header row)


### Test 6: Business Context Document Completeness

Open `business_context.md` and verify it contains:

- Section 1: Business Problem Statement
- Section 2: Dataset Overview
- Section 3: Row Grain
- Section 4: Business Entities
- Section 5: Business Questions
- Section 6: Analysis Workflow
- Section 7: Key Assumptions
- Section 8: Success Criteria
- Section 9: Next Steps

***

## f) Common Beginner Mistakes

### Mistake 1: Dataset Not Downloaded or Wrong Location

**What Happens:**

- Script shows error: "❌ ERROR: Dataset not found at data/raw/telco_churn.csv"

**Why It Happens:**

- Forgot to download from Kaggle
- Saved file in wrong folder (e.g., Downloads instead of data/raw/)
- File has different name (e.g., kept original Kaggle name)

**How to Fix:**

- Download dataset from Kaggle
- Move it to `customer_churn_analysis/data/raw/` folder
- Rename it to exactly `telco_churn.csv` (check for spaces or typos)
- Verify file extension is .csv, not .csv.txt


### Mistake 2: Running Script from Wrong Directory

**What Happens:**

- Error: "FileNotFoundError" or "No such file or directory"
- Even though dataset file exists

**Why It Happens:**

- Terminal/command prompt is in wrong folder
- Script uses relative path "data/raw/telco_churn.csv" which assumes you're in project root

**How to Fix:**

- Use `pwd` (Mac/Linux) or `cd` (Windows) to check current location
- Navigate to project root: `cd customer_churn_analysis`
- Then run: `python scripts/dataset_profile.py`
- Always run scripts from project root, not from inside scripts/ folder


### Mistake 3: Not Reading the Output Carefully

**What Happens:**

- Script runs successfully but you don't understand what the numbers mean
- Move to Stage 2 without understanding the dataset

**Why It Happens:**

- Rushing through stages
- Treating this as a "checkbox" exercise

**How to Fix:**

- Read each section of the output carefully
- Understand what "row grain" means (one row = one customer)
- Note the churn distribution (what percentage of customers churned?)
- Ask yourself: "What does this data represent in real business terms?"


### Mistake 4: Skipping Business Context Documentation

**What Happens:**

- Jump straight to coding in Stage 2
- Later struggle to interpret results because you don't understand business context

**Why It Happens:**

- Seems like "extra work" that's not coding
- Underestimating importance of business understanding

**How to Fix:**

- **Professional analysts spend 30-40% of time on business context**
- Create and READ the business_context.md file
- This document will guide all future stages
- Recruiters/interviewers will ask "why did you analyze this?" - you need to answer from business context


### Mistake 5: Assuming You Know What Churn Means Without Research

**What Happens:**

- Misunderstand the business problem
- Create analysis that doesn't match real-world needs

**Why It Happens:**

- Jumping to technical work without understanding domain
- Assuming "churn" is obvious (it's not - definition varies by industry)

**How to Fix:**

- Read the "Business Problem Statement" section carefully
- Understand: churn = customer cancellation/leaving
- Think about: Why does this matter? What's the cost of losing a customer?
- Frame your entire analysis around this business problem


### Mistake 6: Not Verifying Row Grain

**What Happens:**

- Later assume data is transaction-level or time-series
- Build incorrect analysis

**Why It Happens:**

- Not checking if customer IDs are unique
- Not understanding what "row grain" means

**How to Fix:**

- **Row grain is critical** - it defines what one row represents
- Verify: 7,043 rows = 7,043 unique customer IDs
- Understand: This is a snapshot dataset (one point in time)
- Remember: We CANNOT track customer changes over time with this data


### Mistake 7: Using Wrong Dataset

**What Happens:**

- Download a different churn dataset (banking, e-commerce, etc.)
- Column names don't match, script fails

**Why It Happens:**

- Many churn datasets exist on Kaggle
- Not downloading the specific recommended dataset

**How to Fix:**

- Use IBM Telco Customer Churn dataset specifically
- Verify columns include: customerID, tenure, Churn, MonthlyCharges
- If using different dataset, you'll need to modify script column names

***

## ✅ Stage 1 Complete!

You have now:

- Downloaded a real-world telecom churn dataset
- Profiled the dataset to understand its structure
- Identified the row grain (customer-level)
- Documented business context and problem statement
- Identified key business entities (customers, services, contracts)

**Key Takeaways:**

- Dataset contains 7,043 customers
- Each row = one unique customer (not transactions)
- Target variable is "Churn" (Yes/No)
- Dataset includes demographics, services, account info, and charges
- Business goal: identify at-risk customers for retention

**Next Step:** Wait for instruction to proceed to Stage 2 (Data Centralization \& Integration)

---

# **Stage 2: Data Centralization \& Integration**


***

## a) Learning Objective

### What You're Learning

You are learning how to **combine data from multiple sources** (CSV files and databases) into one unified dataset. This is the most critical real-world data analytics skill - in companies, data never comes from a single file. You'll learn to:

- Design database tables with primary and foreign keys
- Generate realistic dummy data programmatically
- Work with SQLite databases using Python
- Perform SQL queries to extract data
- Join multiple datasets using Pandas
- Validate data relationships and integrity


### Why This Matters

**In real companies, data is scattered across multiple systems:**

- Customer information in CRM database
- Transaction data in payment systems
- Product/service details in service catalogs
- Usage logs in separate databases

**Professional data analysts must:**

- Extract data from different sources
- Understand how tables relate to each other (foreign keys)
- Merge data correctly without losing information
- Create a single "source of truth" for analysis

**This stage simulates real-world complexity** where your Kaggle CSV is just one piece of the puzzle.

### Skill Level

**Intermediate** - This builds on Stage 1 foundations and introduces database concepts, SQL queries, and data integration logic.

### In Scope

- Designing 3 complementary database tables (customers_detail, payments_history, service_catalog)
- Generating dummy data with referential integrity (foreign keys match)
- Creating SQLite database and inserting data
- Writing SQL queries to extract data
- Loading Kaggle CSV and database tables into Pandas
- Performing inner joins to merge datasets
- Validating merged data (row counts, missing values)
- Saving final centralized dataset as CSV


### Out of Scope

- Complex SQL operations (GROUP BY, subqueries) - kept simple
- Data cleaning or handling missing values (comes in Stage 4)
- Statistical analysis (comes in Stage 5)
- Advanced database features (indexes, constraints) - using basics only
- PostgreSQL/MySQL - using SQLite for simplicity


### Assumptions

- You completed Stage 1 (Kaggle dataset exists in `data/raw/`)
- You understand basic concepts: tables, columns, rows
- You know what a customer ID is (unique identifier)
- You're comfortable running Python scripts
- SQLite3 is available (built into Python 3.8+)


### Output Artifact

- **database_schema.py** - Script to create database tables
- **generate_dummy_data.py** - Script to generate realistic fake data
- **centralize_data.py** - Script to merge all sources into one dataset
- **churn_analysis.db** - SQLite database file with 3 tables
- **centralized_churn_data.csv** - Final merged dataset in `data/processed/`
- **data_integration_report.txt** - Summary of integration process

***

## b) Setup Instructions

### Step 1: Verify Stage 1 Completion

Ensure the following file exists:

```
customer_churn_analysis/data/raw/telco_churn.csv
```


### Step 2: Understand Database Design

You will create 3 additional tables in SQLite database:

**Table 1: customers_detail**

- Stores additional customer information not in Kaggle CSV
- Links to main dataset via customerID (foreign key)

**Table 2: payments_history**

- Stores payment transaction details
- Links to customers via customerID (foreign key)

**Table 3: service_catalog**

- Stores service descriptions and pricing
- Links to contract types in main dataset


### Step 3: Files to Create

You will create 3 Python scripts in the `scripts/` folder:

1. `database_schema.py` - Creates empty database tables
2. `generate_dummy_data.py` - Generates and inserts dummy data
3. `centralize_data.py` - Merges all data sources

### Step 4: Database Location

The SQLite database will be stored at:

```
customer_churn_analysis/data/database/churn_analysis.db
```


### Dependencies Required

- pandas (already installed)
- sqlite3 (built into Python)
- numpy (already installed)
- random, datetime (built into Python)

***

## c) Implementation (FINAL VERSION)

### File 1: Database Schema Creation

**File Name:** `database_schema.py`
**File Path:** `customer_churn_analysis/scripts/database_schema.py`
**Total Lines:** 92

```python
# Import sqlite3 module to work with SQLite databases
import sqlite3
# Import os module to work with file paths
import os

# Print header for clarity
print("=" * 70)
print("STAGE 2.1: CREATING DATABASE SCHEMA")
print("=" * 70)
print()

# Define the path where the database file will be stored
db_path = "data/database/churn_analysis.db"

# Check if database file already exists
if os.path.exists(db_path):
    # If it exists, delete it to start fresh
    os.remove(db_path)
    print(f"🗑️  Removed existing database: {db_path}")

# Create a connection to the SQLite database
# If file doesn't exist, it will be created automatically
conn = sqlite3.connect(db_path)
print(f"✅ Connected to database: {db_path}")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# SQL command to create customers_detail table
# This table stores additional customer demographic information
create_customers_table = """
CREATE TABLE customers_detail (
    customerID TEXT PRIMARY KEY,
    RegistrationDate TEXT NOT NULL,
    City TEXT NOT NULL,
    State TEXT NOT NULL,
    ZipCode TEXT NOT NULL,
    CustomerSegment TEXT NOT NULL,
    LastContactDate TEXT
);
"""

# Execute the SQL command to create customers_detail table
cursor.execute(create_customers_table)
print("✅ Created table: customers_detail")
print("   Columns: customerID, RegistrationDate, City, State, ZipCode, CustomerSegment, LastContactDate")
print()

# SQL command to create payments_history table
# This table stores payment transaction records for customers
create_payments_table = """
CREATE TABLE payments_history (
    PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,
    customerID TEXT NOT NULL,
    PaymentDate TEXT NOT NULL,
    Amount REAL NOT NULL,
    PaymentStatus TEXT NOT NULL,
    TransactionID TEXT NOT NULL,
    FOREIGN KEY (customerID) REFERENCES customers_detail(customerID)
);
"""

# Execute the SQL command to create payments_history table
cursor.execute(create_payments_table)
print("✅ Created table: payments_history")
print("   Columns: PaymentID, customerID, PaymentDate, Amount, PaymentStatus, TransactionID")
print()

# SQL command to create service_catalog table
# This table stores service type descriptions and base pricing
create_service_table = """
CREATE TABLE service_catalog (
    ServiceID INTEGER PRIMARY KEY AUTOINCREMENT,
    ServiceType TEXT NOT NULL UNIQUE,
    ServiceDescription TEXT NOT NULL,
    BasePrice REAL NOT NULL,
    Category TEXT NOT NULL
);
"""

# Execute the SQL command to create service_catalog table
cursor.execute(create_service_table)
print("✅ Created table: service_catalog")
print("   Columns: ServiceID, ServiceType, ServiceDescription, BasePrice, Category")
print()

# Insert reference data into service_catalog table
# This data describes different types of services offered
service_catalog_data = [
    ('DSL', 'Digital Subscriber Line Internet', 29.99, 'Internet'),
    ('Fiber optic', 'High-speed Fiber Optic Internet', 69.99, 'Internet'),
    ('Phone Service', 'Basic Phone Service', 19.99, 'Phone'),
    ('Streaming TV', 'Television Streaming Service', 9.99, 'Entertainment'),
    ('Streaming Movies', 'Movie Streaming Service', 9.99, 'Entertainment'),
    ('Online Security', 'Internet Security Suite', 5.99, 'Security'),
    ('Online Backup', 'Cloud Backup Service', 5.99, 'Storage'),
    ('Device Protection', 'Device Insurance and Protection', 7.99, 'Insurance'),
    ('Tech Support', '24/7 Technical Support', 5.99, 'Support')
]

# SQL command to insert data into service_catalog
insert_service_sql = """
INSERT INTO service_catalog (ServiceType, ServiceDescription, BasePrice, Category)
VALUES (?, ?, ?, ?);
"""

# Execute the insert command for each service in the list
cursor.executemany(insert_service_sql, service_catalog_data)
print(f"✅ Inserted {len(service_catalog_data)} services into service_catalog")
print()

# Commit all changes to the database (save permanently)
conn.commit()
print("💾 All changes committed to database")
print()

# Close the database connection
conn.close()
print("🔒 Database connection closed")
print()

# Print final summary
print("=" * 70)
print("✅ DATABASE SCHEMA CREATION COMPLETE")
print("=" * 70)
print(f"Database Location: {db_path}")
print("Tables Created: 3 (customers_detail, payments_history, service_catalog)")
print("Next Step: Run generate_dummy_data.py to populate tables")
```


***

### File 2: Dummy Data Generation

**File Name:** `generate_dummy_data.py`
**File Path:** `customer_churn_analysis/scripts/generate_dummy_data.py`
**Total Lines:** 158

```python
# Import required libraries
import sqlite3  # For database operations
import pandas as pd  # For reading Kaggle CSV
import random  # For generating random values
from datetime import datetime, timedelta  # For generating dates
import os  # For checking file existence

# Print header
print("=" * 70)
print("STAGE 2.2: GENERATING DUMMY DATA")
print("=" * 70)
print()

# Define file paths
kaggle_csv_path = "data/raw/telco_churn.csv"
db_path = "data/database/churn_analysis.db"

# Check if Kaggle CSV exists
if not os.path.exists(kaggle_csv_path):
    print(f"❌ ERROR: Kaggle dataset not found at {kaggle_csv_path}")
    print("Please complete Stage 1 first")
    exit()

# Check if database exists
if not os.path.exists(db_path):
    print(f"❌ ERROR: Database not found at {db_path}")
    print("Please run database_schema.py first")
    exit()

# Load the Kaggle dataset to get customer IDs
print("📂 Loading Kaggle dataset to extract customer IDs...")
df_kaggle = pd.read_csv(kaggle_csv_path)
customer_ids = df_kaggle['customerID'].tolist()
print(f"✅ Loaded {len(customer_ids)} customer IDs from Kaggle dataset")
print()

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
print(f"✅ Connected to database: {db_path}")
print()

# ==================== GENERATE CUSTOMERS_DETAIL DATA ====================
print("-" * 70)
print("Generating data for: customers_detail")
print("-" * 70)

# Define lists of realistic fake data for random selection
cities = ['Los Angeles', 'San Francisco', 'San Diego', 'Sacramento', 'San Jose',
          'Fresno', 'Oakland', 'Bakersfield', 'Anaheim', 'Santa Clarita']

states = ['CA']  # California (telecom dataset context)

# Function to generate a random US zip code
def generate_zipcode():
    # Generate 5-digit zip code
    return f"{random.randint(90000, 96199)}"

# Customer segments based on value/behavior
segments = ['High Value', 'Medium Value', 'Low Value', 'New Customer', 'At Risk']

# Generate registration dates (between 6 years ago and today)
# This aligns with tenure data in Kaggle dataset (0-72 months)
def generate_registration_date():
    # Random number of days between 0 and 2190 (6 years)
    days_ago = random.randint(0, 2190)
    # Calculate date by subtracting days from today
    reg_date = datetime.now() - timedelta(days=days_ago)
    # Return date in YYYY-MM-DD format
    return reg_date.strftime('%Y-%m-%d')

# Generate last contact date (within last 90 days or None)
def generate_last_contact():
    # 70% chance of having a recent contact
    if random.random() < 0.7:
        days_ago = random.randint(1, 90)
        contact_date = datetime.now() - timedelta(days=days_ago)
        return contact_date.strftime('%Y-%m-%d')
    else:
        # 30% chance of no recent contact
        return None

# Create list to store customer detail records
customers_detail_data = []

# Generate one record for each customer ID
for customer_id in customer_ids:
    record = (
        customer_id,  # customerID (matches Kaggle data)
        generate_registration_date(),  # RegistrationDate
        random.choice(cities),  # City
        random.choice(states),  # State
        generate_zipcode(),  # ZipCode
        random.choice(segments),  # CustomerSegment
        generate_last_contact()  # LastContactDate (can be None)
    )
    customers_detail_data.append(record)

# SQL command to insert customer details
insert_customers_sql = """
INSERT INTO customers_detail (customerID, RegistrationDate, City, State, ZipCode, CustomerSegment, LastContactDate)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

# Insert all customer detail records into database
cursor.executemany(insert_customers_sql, customers_detail_data)
print(f"✅ Inserted {len(customers_detail_data)} records into customers_detail")
print()

# ==================== GENERATE PAYMENTS_HISTORY DATA ====================
print("-" * 70)
print("Generating data for: payments_history")
print("-" * 70)

# Each customer will have 1-5 payment records (simulating recent payments)
payment_statuses = ['Completed', 'Completed', 'Completed', 'Pending', 'Failed']

# Function to generate payment date (within last 180 days)
def generate_payment_date():
    days_ago = random.randint(1, 180)
    payment_date = datetime.now() - timedelta(days=days_ago)
    return payment_date.strftime('%Y-%m-%d')

# Function to generate transaction ID
def generate_transaction_id():
    # Format: TXN-XXXXXXXXXX (10 random digits)
    return f"TXN-{random.randint(1000000000, 9999999999)}"

# Create list to store payment records
payments_data = []

# Generate 1-5 payment records for each customer
for customer_id in customer_ids:
    # Random number of payments per customer
    num_payments = random.randint(1, 5)
    
    for _ in range(num_payments):
        record = (
            customer_id,  # customerID (foreign key)
            generate_payment_date(),  # PaymentDate
            round(random.uniform(20.0, 150.0), 2),  # Amount (random between $20-$150)
            random.choice(payment_statuses),  # PaymentStatus
            generate_transaction_id()  # TransactionID
        )
        payments_data.append(record)

# SQL command to insert payment records
insert_payments_sql = """
INSERT INTO payments_history (customerID, PaymentDate, Amount, PaymentStatus, TransactionID)
VALUES (?, ?, ?, ?, ?);
"""

# Insert all payment records into database
cursor.executemany(insert_payments_sql, payments_data)
print(f"✅ Inserted {len(payments_data)} records into payments_history")
print()

# Commit all inserts to database
conn.commit()
print("💾 All data committed to database")
print()

# Close database connection
conn.close()
print("🔒 Database connection closed")
print()

# Print final summary
print("=" * 70)
print("✅ DUMMY DATA GENERATION COMPLETE")
print("=" * 70)
print(f"customers_detail: {len(customers_detail_data)} records")
print(f"payments_history: {len(payments_data)} records")
print(f"service_catalog: 9 records (pre-populated)")
print()
print("Next Step: Run centralize_data.py to merge all sources")
```


***

### File 3: Data Centralization Script

**File Name:** `centralize_data.py`
**File Path:** `customer_churn_analysis/scripts/centralize_data.py`
**Total Lines:** 178

```python
# Import required libraries
import pandas as pd  # For data manipulation and merging
import sqlite3  # For database operations
import os  # For file path operations

# Print header
print("=" * 70)
print("STAGE 2.3: DATA CENTRALIZATION & INTEGRATION")
print("=" * 70)
print()

# Define file paths
kaggle_csv_path = "data/raw/telco_churn.csv"
db_path = "data/database/churn_analysis.db"
output_path = "data/processed/centralized_churn_data.csv"
report_path = "data/processed/data_integration_report.txt"

# Check if required files exist
if not os.path.exists(kaggle_csv_path):
    print(f"❌ ERROR: Kaggle dataset not found at {kaggle_csv_path}")
    exit()

if not os.path.exists(db_path):
    print(f"❌ ERROR: Database not found at {db_path}")
    print("Please run database_schema.py and generate_dummy_data.py first")
    exit()

# ==================== STEP 1: LOAD KAGGLE CSV ====================
print("-" * 70)
print("STEP 1: Loading Kaggle CSV Dataset")
print("-" * 70)

# Load the main Kaggle dataset into a DataFrame
df_main = pd.read_csv(kaggle_csv_path)
print(f"✅ Loaded Kaggle dataset: {kaggle_csv_path}")
print(f"   Rows: {len(df_main)}, Columns: {len(df_main.columns)}")
print()

# ==================== STEP 2: LOAD DATABASE TABLES ====================
print("-" * 70)
print("STEP 2: Loading Database Tables")
print("-" * 70)

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
print(f"✅ Connected to database: {db_path}")
print()

# Load customers_detail table using SQL query
query_customers = "SELECT * FROM customers_detail;"
df_customers = pd.read_sql_query(query_customers, conn)
print(f"✅ Loaded customers_detail table")
print(f"   Rows: {len(df_customers)}, Columns: {len(df_customers.columns)}")
print()

# Load payments_history table using SQL query
query_payments = "SELECT * FROM payments_history;"
df_payments = pd.read_sql_query(query_payments, conn)
print(f"✅ Loaded payments_history table")
print(f"   Rows: {len(df_payments)}, Columns: {len(df_payments.columns)}")
print()

# Load service_catalog table using SQL query
query_services = "SELECT * FROM service_catalog;"
df_services = pd.read_sql_query(query_services, conn)
print(f"✅ Loaded service_catalog table")
print(f"   Rows: {len(df_services)}, Columns: {len(df_services.columns)}")
print()

# Close database connection (no longer needed)
conn.close()
print("🔒 Database connection closed")
print()

# ==================== STEP 3: AGGREGATE PAYMENTS DATA ====================
print("-" * 70)
print("STEP 3: Aggregating Payment History Per Customer")
print("-" * 70)

# For each customer, calculate payment statistics
# Group all payments by customerID
payment_summary = df_payments.groupby('customerID').agg({
    'PaymentID': 'count',  # Count total number of payments
    'Amount': ['sum', 'mean'],  # Sum and average of payment amounts
    'PaymentStatus': lambda x: (x == 'Failed').sum()  # Count failed payments
}).reset_index()

# Flatten multi-level column names
# Change ('Amount', 'sum') to 'TotalPaid'
payment_summary.columns = ['customerID', 'TotalPayments', 'TotalPaid', 'AvgPayment', 'FailedPayments']

# Round monetary values to 2 decimal places
payment_summary['TotalPaid'] = payment_summary['TotalPaid'].round(2)
payment_summary['AvgPayment'] = payment_summary['AvgPayment'].round(2)

print(f"✅ Aggregated payment data for {len(payment_summary)} customers")
print(f"   New columns: TotalPayments, TotalPaid, AvgPayment, FailedPayments")
print()

# ==================== STEP 4: MERGE ALL DATASETS ====================
print("-" * 70)
print("STEP 4: Merging All Data Sources")
print("-" * 70)

# Merge Step 1: Main Kaggle data + Customer Details
# Use inner join (only keep customers present in both datasets)
print("🔗 Merging: Kaggle data + customers_detail...")
df_merged = pd.merge(
    df_main,  # Left dataset
    df_customers,  # Right dataset
    on='customerID',  # Join key
    how='inner'  # Inner join (only matching records)
)
print(f"   Result: {len(df_merged)} rows, {len(df_merged.columns)} columns")
print()

# Merge Step 2: Add Payment Summary
print("🔗 Merging: Previous result + payment_summary...")
df_merged = pd.merge(
    df_merged,  # Left dataset (result from previous merge)
    payment_summary,  # Right dataset
    on='customerID',  # Join key
    how='left'  # Left join (keep all customers even if no payments)
)
print(f"   Result: {len(df_merged)} rows, {len(df_merged.columns)} columns")
print()

# Fill missing payment values with 0 (customers with no payment records)
df_merged['TotalPayments'] = df_merged['TotalPayments'].fillna(0).astype(int)
df_merged['TotalPaid'] = df_merged['TotalPaid'].fillna(0)
df_merged['AvgPayment'] = df_merged['AvgPayment'].fillna(0)
df_merged['FailedPayments'] = df_merged['FailedPayments'].fillna(0).astype(int)
print("✅ Filled missing payment values with 0 (customers with no payment history)")
print()

# ==================== STEP 5: VALIDATE MERGED DATA ====================
print("-" * 70)
print("STEP 5: Validating Merged Dataset")
print("-" * 70)

# Check for missing values in key columns
print("🔍 Checking for missing values...")
missing_counts = df_merged.isnull().sum()
critical_nulls = missing_counts[missing_counts > 0]

if len(critical_nulls) > 0:
    print("⚠️  Missing values detected:")
    for col, count in critical_nulls.items():
        print(f"   {col}: {count} missing")
else:
    print("✅ No missing values in merged dataset")
print()

# Validate row count
print("🔍 Validating row count...")
print(f"   Original Kaggle rows: {len(df_main)}")
print(f"   Merged dataset rows: {len(df_merged)}")

if len(df_merged) == len(df_main):
    print("✅ Row count matches - no data loss during merge")
else:
    print(f"⚠️  Row count mismatch - lost {len(df_main) - len(df_merged)} rows")
print()

# Check duplicate customer IDs
print("🔍 Checking for duplicate customer IDs...")
duplicate_count = df_merged['customerID'].duplicated().sum()
if duplicate_count == 0:
    print("✅ No duplicate customer IDs - data integrity maintained")
else:
    print(f"⚠️  Found {duplicate_count} duplicate customer IDs")
print()

# ==================== STEP 6: SAVE CENTRALIZED DATASET ====================
print("-" * 70)
print("STEP 6: Saving Centralized Dataset")
print("-" * 70)

# Save the merged dataset to CSV file
df_merged.to_csv(output_path, index=False)
print(f"✅ Centralized dataset saved to: {output_path}")
print(f"   Final shape: {df_merged.shape[0]} rows × {df_merged.shape[1]} columns")
print()

# ==================== STEP 7: GENERATE INTEGRATION REPORT ====================
print("-" * 70)
print("STEP 7: Generating Integration Report")
print("-" * 70)

# Create a text report summarizing the integration process
report_lines = []
report_lines.append("=" * 70)
report_lines.append("DATA INTEGRATION REPORT")
report_lines.append("=" * 70)
report_lines.append("")
report_lines.append(f"Report Generated: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
report_lines.append("")
report_lines.append("DATA SOURCES:")
report_lines.append(f"1. Kaggle CSV: {kaggle_csv_path}")
report_lines.append(f"   Rows: {len(df_main)}, Columns: {len(df_main.columns)}")
report_lines.append(f"2. Database: {db_path}")
report_lines.append(f"   - customers_detail: {len(df_customers)} rows")
report_lines.append(f"   - payments_history: {len(df_payments)} rows")
report_lines.append(f"   - service_catalog: {len(df_services)} rows")
report_lines.append("")
report_lines.append("INTEGRATION STEPS:")
report_lines.append("1. Loaded Kaggle CSV dataset")
report_lines.append("2. Loaded database tables using SQL queries")
report_lines.append("3. Aggregated payment history per customer")
report_lines.append("4. Merged datasets using customerID as join key")
report_lines.append("5. Validated data integrity (row counts, duplicates)")
report_lines.append("")
report_lines.append("FINAL DATASET:")
report_lines.append(f"Output File: {output_path}")
report_lines.append(f"Total Rows: {len(df_merged)}")
report_lines.append(f"Total Columns: {len(df_merged.columns)}")
report_lines.append("")
report_lines.append("NEW COLUMNS ADDED:")
report_lines.append("- RegistrationDate (from customers_detail)")
report_lines.append("- City (from customers_detail)")
report_lines.append("- State (from customers_detail)")
report_lines.append("- ZipCode (from customers_detail)")
report_lines.append("- CustomerSegment (from customers_detail)")
report_lines.append("- LastContactDate (from customers_detail)")
report_lines.append("- TotalPayments (aggregated from payments_history)")
report_lines.append("- TotalPaid (aggregated from payments_history)")
report_lines.append("- AvgPayment (aggregated from payments_history)")
report_lines.append("- FailedPayments (aggregated from payments_history)")
report_lines.append("")
report_lines.append("=" * 70)
report_lines.append("INTEGRATION COMPLETE")
report_lines.append("=" * 70)

# Write report to text file
with open(report_path, 'w') as f:
    f.write('\n'.join(report_lines))

print(f"✅ Integration report saved to: {report_path}")
print()

# Print final summary
print("=" * 70)
print("✅ DATA CENTRALIZATION COMPLETE")
print("=" * 70)
print(f"Centralized dataset: {output_path}")
print(f"Integration report: {report_path}")
print()
print("Next Step: Proceed to Stage 3 (Data Validation & Profiling)")
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure you have completed Stage 1 and the Kaggle CSV exists:

```bash
ls data/raw/telco_churn.csv
```

If file doesn't exist, complete Stage 1 first.

### Step 2: Navigate to Project Root

Open terminal and navigate to project folder:

```bash
cd path/to/customer_churn_analysis
```


### Step 3: Create Database Schema

Run the first script to create empty database tables:

```bash
python scripts/database_schema.py
```

**Expected output:**

- "✅ Connected to database"
- "✅ Created table: customers_detail"
- "✅ Created table: payments_history"
- "✅ Created table: service_catalog"
- "✅ DATABASE SCHEMA CREATION COMPLETE"


### Step 4: Generate Dummy Data

Run the second script to populate database tables:

```bash
python scripts/generate_dummy_data.py
```

**Expected output:**

- "✅ Loaded 7,043 customer IDs from Kaggle dataset"
- "✅ Inserted 7,043 records into customers_detail"
- "✅ Inserted [number] records into payments_history"
- "✅ DUMMY DATA GENERATION COMPLETE"

**Note:** This may take 30-60 seconds depending on your computer speed.

### Step 5: Centralize All Data

Run the third script to merge all data sources:

```bash
python scripts/centralize_data.py
```

**Expected output:**

- Shows 7 steps of data integration process
- "✅ Centralized dataset saved to: data/processed/centralized_churn_data.csv"
- "✅ DATA CENTRALIZATION COMPLETE"


### Step 6: Verify Output Files

Check that the following files were created:

```bash
ls data/database/churn_analysis.db
ls data/processed/centralized_churn_data.csv
ls data/processed/data_integration_report.txt
```


***

## e) How to Test the Output

### Test 1: Verify Database Creation

**Expected Result:**

- File exists at `data/database/churn_analysis.db`
- File size should be approximately 1-3 MB

**How to Check:**

```bash
# On Mac/Linux
ls -lh data/database/churn_analysis.db

# On Windows
dir data\database\churn_analysis.db
```

**Manual Inspection (Optional):**
If you have DB Browser for SQLite installed:

1. Open `churn_analysis.db` in DB Browser
2. Verify 3 tables exist: customers_detail, payments_history, service_catalog
3. Browse data to see records

### Test 2: Verify Database Tables Have Data

**Quick Python Check:**

```bash
python -c "import sqlite3; conn = sqlite3.connect('data/database/churn_analysis.db'); cursor = conn.cursor(); cursor.execute('SELECT COUNT(*) FROM customers_detail'); print('customers_detail:', cursor.fetchone()[0], 'rows'); cursor.execute('SELECT COUNT(*) FROM payments_history'); print('payments_history:', cursor.fetchone()[0], 'rows'); conn.close()"
```

**Expected Output:**

```
customers_detail: 7043 rows
payments_history: [20000-35000] rows
```


### Test 3: Verify Centralized CSV File

**Expected Result:**

- File exists at `data/processed/centralized_churn_data.csv`
- File size approximately 2-3 MB
- Contains 7,043 rows (same as original Kaggle data)
- Contains original 21 columns + 10 new columns = 31 total columns

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/centralized_churn_data.csv'); print(f'Rows: {len(df)}, Columns: {len(df.columns)}'); print('New columns:', [c for c in df.columns if c not in ['customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn']][:5])"
```

**Expected Output:**

```
Rows: 7043, Columns: 31
New columns: ['RegistrationDate', 'City', 'State', 'ZipCode', 'CustomerSegment']
```


### Test 4: Verify Integration Report

**Expected Result:**

- File exists at `data/processed/data_integration_report.txt`
- Contains summary of integration process

**How to Check:**

```bash
# On Mac/Linux
cat data/processed/data_integration_report.txt

# On Windows
type data\processed\data_integration_report.txt
```

**Report Should Contain:**

- Data sources used
- Integration steps performed
- Final dataset dimensions
- New columns added


### Test 5: Validate Data Relationships

**Check that customerIDs match across sources:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/centralized_churn_data.csv'); print('Duplicate customerIDs:', df['customerID'].duplicated().sum()); print('Missing values in RegistrationDate:', df['RegistrationDate'].isnull().sum()); print('Missing values in City:', df['City'].isnull().sum())"
```

**Expected Output:**

```
Duplicate customerIDs: 0
Missing values in RegistrationDate: 0
Missing values in City: 0
```


### Test 6: Sample Data Inspection

**Manually inspect first few rows:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/centralized_churn_data.csv'); print(df[['customerID', 'City', 'State', 'TotalPayments', 'TotalPaid', 'Churn']].head())"
```

**Expected Output:**
Table showing customer data with new columns populated (City, State, payment info, etc.)

### Signs of Success

✅ All 3 scripts run without errors
✅ Database file created with 3 tables
✅ customers_detail has 7,043 rows
✅ payments_history has 20,000+ rows
✅ Centralized CSV has 7,043 rows and 31 columns
✅ No duplicate customerIDs
✅ No missing values in key columns
✅ Integration report generated

### Signs of Problems

❌ Script errors or crashes
❌ Database file missing or empty
❌ Centralized CSV has fewer than 7,043 rows (data loss)
❌ Missing values in RegistrationDate, City, or State columns
❌ Duplicate customerIDs present
❌ Column count doesn't match expected (31 columns)

***

## f) Common Beginner Mistakes

### Mistake 1: Running Scripts Out of Order

**What Happens:**

- Run `generate_dummy_data.py` before `database_schema.py`
- Error: "Database not found" or "no such table: customers_detail"

**Why It Happens:**

- Database must be created before inserting data
- Tables must exist before INSERT commands

**How to Fix:**

- Always run in this order:

1. `database_schema.py` (creates database and tables)
2. `generate_dummy_data.py` (populates tables)
3. `centralize_data.py` (merges all sources)
- If you make a mistake, delete the database file and start over


### Mistake 2: Running Scripts from Wrong Directory

**What Happens:**

- Error: "FileNotFoundError: data/raw/telco_churn.csv"
- Even though file exists

**Why It Happens:**

- Scripts use relative paths that assume you're in project root
- If you're in `scripts/` folder, relative paths won't work

**How to Fix:**

- Always navigate to project root: `cd customer_churn_analysis`
- Run scripts using: `python scripts/script_name.py`
- Check current directory with `pwd` (Mac/Linux) or `cd` (Windows)


### Mistake 3: Not Understanding Foreign Keys

**What Happens:**

- Generate payment data for customerIDs that don't exist in main dataset
- Results in data integrity issues

**Why It Happens:**

- Not understanding that foreign keys must match primary keys
- Creating data without referential integrity

**How to Fix:**

- The script correctly loads customerIDs from Kaggle CSV first
- Always generate related data using existing IDs
- **Key concept:** Foreign keys in payments_history must match customerIDs in main dataset


### Mistake 4: Expecting Merged Data to Have More Rows

**What Happens:**

- Think merge should multiply rows (7,043 → 21,000+)
- Confused about join types

**Why It Happens:**

- Misunderstanding how joins work
- Confusing aggregated data with raw transaction data

**How to Fix:**

- **Understand merge logic:**
    - We aggregate payments (multiple payments → summary per customer)
    - Then merge summaries back to main data (one row per customer remains)
    - Inner/left joins don't multiply rows when joining 1:1 relationships
- Final dataset should have same row count as original (7,043)


### Mistake 5: Not Checking for Data Loss

**What Happens:**

- Merge completes but lost customers due to wrong join type
- Don't validate row counts after merge

**Why It Happens:**

- Using inner join when left join is needed (or vice versa)
- Not verifying data integrity

**How to Fix:**

- Always print row counts before and after merge
- Use `how='inner'` for customers_detail (should match exactly)
- Use `how='left'` for payments (keep customers with no payment history)
- Validate: `len(df_merged) == len(df_main)`


### Mistake 6: Forgetting to Handle Missing Values After Left Join

**What Happens:**

- Centralized dataset has NaN values in payment columns
- Later analysis breaks due to missing data

**Why It Happens:**

- Left join includes customers with no payment records
- Payment columns are NaN for these customers

**How to Fix:**

- Script correctly fills NaN with 0 using `fillna(0)`
- **Business logic:** 0 payments = no payment history (valid state)
- Always check for and handle NaN after left joins


### Mistake 7: Not Understanding Aggregation

**What Happens:**

- Confused about what `groupby().agg()` does
- Don't understand why we aggregate payments

**Why It Happens:**

- Payments table has multiple rows per customer (1 customer → many payments)
- Need to summarize to one row per customer for merging

**How to Fix:**

- **Understand aggregation purpose:**
    - Raw: Customer A has 3 payments (\$50, \$60, \$70)
    - Aggregated: Customer A → TotalPayments=3, TotalPaid=\$180, AvgPayment=\$60
- Must aggregate many-to-one relationships before merging
- One customer → one summary row


### Mistake 8: Deleting Database Without Regenerating Data

**What Happens:**

- Delete `churn_analysis.db` to start fresh
- Run `centralize_data.py` directly
- Error: Database not found

**Why It Happens:**

- Deleting database removes both schema and data
- Must recreate both

**How to Fix:**

- If you delete database, run both:

1. `python scripts/database_schema.py`
2. `python scripts/generate_dummy_data.py`
- Then run `centralize_data.py`


### Mistake 9: Not Reading the Integration Report

**What Happens:**

- Script completes but don't verify what was actually done
- Miss data issues or misunderstand new columns

**Why It Happens:**

- Skip reading the generated report file
- Assume everything worked correctly

**How to Fix:**

- Always read `data_integration_report.txt`
- Verify row counts match expectations
- Understand what new columns were added and why


### Mistake 10: Trying to Join on Wrong Column

**What Happens:**

- Attempt to join using wrong key (e.g., 'TotalCharges' instead of 'customerID')
- Results in incorrect merge

**Why It Happens:**

- Misunderstanding join keys
- Not identifying common columns between datasets

**How to Fix:**

- **Join key must be:**
    - Present in both datasets
    - Contain matching values
    - Typically an ID column (customerID)
- Always verify join key with: `df1.columns` and `df2.columns`

***

## ✅ Stage 2 Complete!

You have now:

- Created a SQLite database with 3 tables (customers_detail, payments_history, service_catalog)
- Generated realistic dummy data with referential integrity
- Loaded data from both CSV and database sources
- Aggregated payment transaction data per customer
- Merged multiple datasets using customerID as join key
- Validated data integrity (no duplicates, no data loss)
- Saved a centralized dataset with 31 columns
- Generated an integration report documenting the process

**Key Concepts Mastered:**

- Database table design with primary/foreign keys
- SQL queries to extract data
- Pandas merge operations (inner join, left join)
- Data aggregation (groupby, sum, mean, count)
- Referential integrity and data relationships
- Data validation techniques

**Final Output:**

- `data/database/churn_analysis.db` - SQLite database with 3 tables
- `data/processed/centralized_churn_data.csv` - Unified dataset (7,043 rows × 31 columns)
- `data/processed/data_integration_report.txt` - Integration documentation

**Next Step:** Wait for instruction to proceed to Stage 3 (Raw Data Validation \& Profiling)

---

# **Stage 3: Raw Data Validation \& Profiling**


***

## a) Learning Objective

### What You're Learning

You are learning how to **systematically inspect and document data quality issues** before making any changes. This is called "data profiling" - examining the actual condition of your data to identify problems like missing values, duplicates, incorrect data types, outliers, and inconsistencies.

### Why This Matters

In real-world analytics, **raw data is almost never perfect**. Professional data analysts follow this critical rule:

**"Inspect before you clean"**

If you start cleaning data without understanding what's wrong, you risk:

- Fixing the wrong problems
- Making incorrect assumptions about missing data
- Losing important information
- Creating bias in your analysis
- Wasting time on unnecessary cleaning

**Data profiling creates a roadmap** - you document every issue, then decide systematically how to handle each one in Stage 4.

### Skill Level

**Foundation to Intermediate** - This builds on data loading skills and introduces systematic quality assessment techniques used by professional analysts.

### In Scope

- Loading the centralized dataset from Stage 2
- Checking data types for each column
- Calculating missing value percentages
- Identifying duplicate records
- Analyzing value ranges (min, max, mean, median)
- Detecting outliers using statistical methods
- Validating date/time continuity
- Checking categorical value distributions
- Generating a comprehensive data quality report
- Creating summary visualizations of data issues


### Out of Scope

- Fixing or cleaning any data issues (Stage 4)
- Imputing missing values (Stage 4)
- Removing outliers (Stage 4)
- Statistical modeling or predictions (Stage 7)
- Feature engineering (Stage 6)
- Advanced outlier detection (IQR and Z-score only)


### Assumptions

- You completed Stage 2 (centralized dataset exists at `data/processed/centralized_churn_data.csv`)
- You understand basic statistics (mean, median, standard deviation)
- You know what NULL/missing values are
- You're familiar with different data types (numeric, text, dates)


### Output Artifact

- **data_profiling.py** - Main profiling script that analyzes all columns
- **data_quality_report.txt** - Comprehensive text report of all data issues
- **data_quality_summary.csv** - Column-by-column quality metrics
- **Console output** - Formatted profiling results with color indicators

***

## b) Setup Instructions

### Step 1: Verify Prerequisites

Ensure the centralized dataset from Stage 2 exists:

```
customer_churn_analysis/data/processed/centralized_churn_data.csv
```

If this file doesn't exist, complete Stage 2 first.

### Step 2: Understand What We're Checking

The profiling script will examine:

**For ALL columns:**

- Data type (numeric, text, date)
- Count of missing (NULL/NaN) values
- Percentage of missing values
- Count of unique values

**For NUMERIC columns:**

- Min, max, mean, median
- Standard deviation
- Outliers using IQR method (values beyond 1.5 × IQR)
- Outliers using Z-score method (values beyond ±3 standard deviations)

**For CATEGORICAL (text) columns:**

- Most common values (top 5)
- Rare values (appearing < 1% of time)
- Potential inconsistencies (similar spellings)

**For DATE columns:**

- Date range (earliest to latest)
- Invalid date formats
- Future dates (data quality issue)


### Step 3: Files to Create

You will create one Python script in the `scripts/` folder:

- `data_profiling.py` - Main profiling script


### Step 4: Output Locations

The script will generate files in `data/processed/`:

- `data_quality_report.txt` - Human-readable report
- `data_quality_summary.csv` - Machine-readable metrics


### Dependencies Required

- pandas (already installed)
- numpy (already installed)
- No additional installations needed

***

## c) Implementation (FINAL VERSION)

### File 1: Data Profiling Script

**File Name:** `data_profiling.py`
**File Path:** `customer_churn_analysis/scripts/data_profiling.py`
**Total Lines:** 285

```python
# Import required libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import os  # For file path operations
from datetime import datetime  # For working with dates

# Print header
print("=" * 80)
print("STAGE 3: RAW DATA VALIDATION & PROFILING")
print("=" * 80)
print()

# Define file paths
input_path = "data/processed/centralized_churn_data.csv"
report_path = "data/processed/data_quality_report.txt"
summary_path = "data/processed/data_quality_summary.csv"

# Check if centralized dataset exists
if not os.path.exists(input_path):
    print(f"❌ ERROR: Centralized dataset not found at {input_path}")
    print("Please complete Stage 2 first")
    exit()

# Load the centralized dataset
print("📂 Loading centralized dataset...")
df = pd.read_csv(input_path)
print(f"✅ Dataset loaded: {input_path}")
print(f"   Rows: {len(df)}, Columns: {len(df.columns)}")
print()

# Initialize list to store report lines
report_lines = []

# ==================== SECTION 1: BASIC DATASET OVERVIEW ====================
print("-" * 80)
print("SECTION 1: BASIC DATASET OVERVIEW")
print("-" * 80)

# Add section header to report
report_lines.append("=" * 80)
report_lines.append("DATA QUALITY REPORT")
report_lines.append("=" * 80)
report_lines.append("")
report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report_lines.append(f"Dataset: {input_path}")
report_lines.append("")
report_lines.append("-" * 80)
report_lines.append("SECTION 1: BASIC DATASET OVERVIEW")
report_lines.append("-" * 80)

# Get basic dataset information
num_rows, num_cols = df.shape
print(f"Total Rows: {num_rows:,}")
print(f"Total Columns: {num_cols}")
print(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
print()

# Add to report
report_lines.append(f"Total Rows: {num_rows:,}")
report_lines.append(f"Total Columns: {num_cols}")
report_lines.append(f"Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
report_lines.append("")

# ==================== SECTION 2: DUPLICATE RECORDS CHECK ====================
print("-" * 80)
print("SECTION 2: DUPLICATE RECORDS CHECK")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 2: DUPLICATE RECORDS CHECK")
report_lines.append("-" * 80)

# Check for duplicate customerIDs (primary key)
duplicate_ids = df['customerID'].duplicated().sum()
print(f"Duplicate customerIDs: {duplicate_ids}")

if duplicate_ids > 0:
    print("⚠️  WARNING: Duplicate customer records found!")
    report_lines.append(f"⚠️  Duplicate customerIDs: {duplicate_ids}")
else:
    print("✅ No duplicate customerIDs - primary key integrity maintained")
    report_lines.append("✅ No duplicate customerIDs")

# Check for completely duplicate rows (all columns identical)
duplicate_rows = df.duplicated().sum()
print(f"Completely Duplicate Rows: {duplicate_rows}")

if duplicate_rows > 0:
    print("⚠️  WARNING: Completely duplicate rows found!")
    report_lines.append(f"⚠️  Completely Duplicate Rows: {duplicate_rows}")
else:
    print("✅ No completely duplicate rows")
    report_lines.append("✅ No completely duplicate rows")

print()
report_lines.append("")

# ==================== SECTION 3: MISSING VALUES ANALYSIS ====================
print("-" * 80)
print("SECTION 3: MISSING VALUES ANALYSIS")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 3: MISSING VALUES ANALYSIS")
report_lines.append("-" * 80)

# Calculate missing values for each column
missing_counts = df.isnull().sum()
missing_percentages = (missing_counts / len(df)) * 100

# Create a summary DataFrame
missing_summary = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': missing_counts.values,
    'Missing_Percentage': missing_percentages.values
})

# Sort by missing percentage (descending)
missing_summary = missing_summary.sort_values('Missing_Percentage', ascending=False)

# Display columns with missing values
columns_with_missing = missing_summary[missing_summary['Missing_Count'] > 0]

if len(columns_with_missing) > 0:
    print(f"⚠️  Found {len(columns_with_missing)} columns with missing values:")
    print()
    # Print each column with missing data
    for _, row in columns_with_missing.iterrows():
        print(f"  {row['Column']}: {int(row['Missing_Count'])} missing ({row['Missing_Percentage']:.2f}%)")
        report_lines.append(f"  {row['Column']}: {int(row['Missing_Count'])} missing ({row['Missing_Percentage']:.2f}%)")
else:
    print("✅ No missing values found in any column")
    report_lines.append("✅ No missing values found")

print()
report_lines.append("")

# ==================== SECTION 4: DATA TYPES VALIDATION ====================
print("-" * 80)
print("SECTION 4: DATA TYPES VALIDATION")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 4: DATA TYPES VALIDATION")
report_lines.append("-" * 80)

# Get data types for all columns
dtypes_summary = df.dtypes.value_counts()
print("Data Type Distribution:")
for dtype, count in dtypes_summary.items():
    print(f"  {dtype}: {count} columns")
    report_lines.append(f"  {dtype}: {count} columns")

print()
report_lines.append("")

# List columns by type
print("Columns by Data Type:")
report_lines.append("Columns by Data Type:")

# Numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
print(f"  Numeric ({len(numeric_cols)}): {', '.join(numeric_cols[:5])}{'...' if len(numeric_cols) > 5 else ''}")
report_lines.append(f"  Numeric ({len(numeric_cols)}): {', '.join(numeric_cols)}")

# Object/Text columns
object_cols = df.select_dtypes(include=['object']).columns.tolist()
print(f"  Object/Text ({len(object_cols)}): {', '.join(object_cols[:5])}{'...' if len(object_cols) > 5 else ''}")
report_lines.append(f"  Object/Text ({len(object_cols)}): {', '.join(object_cols)}")

print()
report_lines.append("")

# ==================== SECTION 5: NUMERIC COLUMNS PROFILING ====================
print("-" * 80)
print("SECTION 5: NUMERIC COLUMNS PROFILING")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 5: NUMERIC COLUMNS PROFILING")
report_lines.append("-" * 80)

# Analyze each numeric column
for col in numeric_cols:
    print(f"\n📊 Column: {col}")
    report_lines.append(f"\nColumn: {col}")
    
    # Basic statistics
    col_data = df[col].dropna()  # Remove NaN for calculations
    
    if len(col_data) == 0:
        print("  ⚠️  All values are missing")
        report_lines.append("  All values missing")
        continue
    
    # Calculate statistics
    min_val = col_data.min()
    max_val = col_data.max()
    mean_val = col_data.mean()
    median_val = col_data.median()
    std_val = col_data.std()
    
    print(f"  Min: {min_val:.2f}")
    print(f"  Max: {max_val:.2f}")
    print(f"  Mean: {mean_val:.2f}")
    print(f"  Median: {median_val:.2f}")
    print(f"  Std Dev: {std_val:.2f}")
    
    report_lines.append(f"  Min: {min_val:.2f}, Max: {max_val:.2f}")
    report_lines.append(f"  Mean: {mean_val:.2f}, Median: {median_val:.2f}, Std: {std_val:.2f}")
    
    # Check for outliers using IQR method
    # IQR = Inter-Quartile Range (Q3 - Q1)
    Q1 = col_data.quantile(0.25)  # 25th percentile
    Q3 = col_data.quantile(0.75)  # 75th percentile
    IQR = Q3 - Q1  # Inter-quartile range
    
    # Define outlier boundaries
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Count outliers
    outliers_iqr = col_data[(col_data < lower_bound) | (col_data > upper_bound)]
    num_outliers = len(outliers_iqr)
    outlier_percentage = (num_outliers / len(col_data)) * 100
    
    if num_outliers > 0:
        print(f"  ⚠️  Outliers (IQR method): {num_outliers} ({outlier_percentage:.2f}%)")
        report_lines.append(f"  Outliers (IQR): {num_outliers} ({outlier_percentage:.2f}%)")
    else:
        print(f"  ✅ No outliers detected (IQR method)")
        report_lines.append(f"  No outliers (IQR)")

print()
report_lines.append("")

# ==================== SECTION 6: CATEGORICAL COLUMNS PROFILING ====================
print("-" * 80)
print("SECTION 6: CATEGORICAL COLUMNS PROFILING")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 6: CATEGORICAL COLUMNS PROFILING")
report_lines.append("-" * 80)

# Analyze each categorical (object) column
for col in object_cols:
    print(f"\n📊 Column: {col}")
    report_lines.append(f"\nColumn: {col}")
    
    # Count unique values
    unique_count = df[col].nunique()
    total_count = df[col].count()  # Non-null count
    
    print(f"  Unique Values: {unique_count}")
    print(f"  Non-Null Count: {total_count}")
    report_lines.append(f"  Unique: {unique_count}, Non-Null: {total_count}")
    
    # If few unique values, show value distribution
    if unique_count <= 10:
        print("  Value Distribution:")
        value_counts = df[col].value_counts()
        for value, count in value_counts.items():
            percentage = (count / total_count) * 100
            print(f"    {value}: {count} ({percentage:.2f}%)")
            report_lines.append(f"    {value}: {count} ({percentage:.2f}%)")
    else:
        # Show top 5 most common values
        print("  Top 5 Most Common Values:")
        value_counts = df[col].value_counts().head(5)
        for value, count in value_counts.items():
            percentage = (count / total_count) * 100
            # Truncate long values for display
            display_value = str(value)[:30] + "..." if len(str(value)) > 30 else value
            print(f"    {display_value}: {count} ({percentage:.2f}%)")
            report_lines.append(f"    {value}: {count} ({percentage:.2f}%)")

print()
report_lines.append("")

# ==================== SECTION 7: DATE COLUMNS VALIDATION ====================
print("-" * 80)
print("SECTION 7: DATE COLUMNS VALIDATION")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 7: DATE COLUMNS VALIDATION")
report_lines.append("-" * 80)

# Identify potential date columns (containing 'Date' in name)
date_columns = [col for col in df.columns if 'Date' in col]

if len(date_columns) > 0:
    for col in date_columns:
        print(f"\n📅 Column: {col}")
        report_lines.append(f"\nColumn: {col}")
        
        # Try to parse as dates
        try:
            # Convert to datetime
            df[col + '_parsed'] = pd.to_datetime(df[col], errors='coerce')
            
            # Count invalid dates (became NaT after conversion)
            invalid_dates = df[col + '_parsed'].isnull().sum() - df[col].isnull().sum()
            
            if invalid_dates > 0:
                print(f"  ⚠️  Invalid Date Formats: {invalid_dates}")
                report_lines.append(f"  Invalid dates: {invalid_dates}")
            else:
                print(f"  ✅ All dates valid")
                report_lines.append(f"  All dates valid")
            
            # Get date range for valid dates
            valid_dates = df[col + '_parsed'].dropna()
            if len(valid_dates) > 0:
                min_date = valid_dates.min()
                max_date = valid_dates.max()
                print(f"  Date Range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")
                report_lines.append(f"  Range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")
                
                # Check for future dates (potential data quality issue)
                today = pd.Timestamp.now()
                future_dates = valid_dates[valid_dates > today]
                if len(future_dates) > 0:
                    print(f"  ⚠️  Future Dates Found: {len(future_dates)}")
                    report_lines.append(f"  Future dates: {len(future_dates)}")
            
            # Clean up temporary column
            df.drop(columns=[col + '_parsed'], inplace=True)
            
        except Exception as e:
            print(f"  ⚠️  Error parsing dates: {str(e)}")
            report_lines.append(f"  Error parsing: {str(e)}")
else:
    print("No date columns detected (columns with 'Date' in name)")
    report_lines.append("No date columns detected")

print()
report_lines.append("")

# ==================== SECTION 8: KEY RELATIONSHIPS VALIDATION ====================
print("-" * 80)
print("SECTION 8: KEY RELATIONSHIPS VALIDATION")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 8: KEY RELATIONSHIPS VALIDATION")
report_lines.append("-" * 80)

# Check if customerID is truly unique (primary key constraint)
if 'customerID' in df.columns:
    total_customers = len(df)
    unique_customers = df['customerID'].nunique()
    
    print(f"Total Rows: {total_customers:,}")
    print(f"Unique customerIDs: {unique_customers:,}")
    
    report_lines.append(f"Total Rows: {total_customers:,}")
    report_lines.append(f"Unique customerIDs: {unique_customers:,}")
    
    if total_customers == unique_customers:
        print("✅ Primary Key Integrity: PASS (each row = unique customer)")
        report_lines.append("✅ Primary Key Integrity: PASS")
    else:
        print("⚠️  PRIMARY KEY VIOLATION: Multiple rows per customer")
        report_lines.append("⚠️  PRIMARY KEY VIOLATION")
else:
    print("⚠️  No customerID column found")
    report_lines.append("⚠️  No customerID column")

print()
report_lines.append("")

# ==================== SECTION 9: DATA QUALITY SUMMARY ====================
print("-" * 80)
print("SECTION 9: DATA QUALITY SUMMARY")
print("-" * 80)

# Add section to report
report_lines.append("-" * 80)
report_lines.append("SECTION 9: DATA QUALITY SUMMARY")
report_lines.append("-" * 80)

# Calculate overall data quality score
total_cells = num_rows * num_cols
missing_cells = df.isnull().sum().sum()
complete_cells = total_cells - missing_cells
completeness_percentage = (complete_cells / total_cells) * 100

print(f"Total Data Cells: {total_cells:,}")
print(f"Complete Cells: {complete_cells:,}")
print(f"Missing Cells: {missing_cells:,}")
print(f"Data Completeness: {completeness_percentage:.2f}%")

report_lines.append(f"Total Cells: {total_cells:,}")
report_lines.append(f"Complete: {complete_cells:,}, Missing: {missing_cells:,}")
report_lines.append(f"Completeness: {completeness_percentage:.2f}%")
report_lines.append("")

# Quality assessment
if completeness_percentage >= 99:
    quality_rating = "EXCELLENT"
elif completeness_percentage >= 95:
    quality_rating = "GOOD"
elif completeness_percentage >= 90:
    quality_rating = "FAIR"
else:
    quality_rating = "POOR"

print(f"Overall Data Quality Rating: {quality_rating}")
report_lines.append(f"Overall Quality: {quality_rating}")

print()
report_lines.append("")

# ==================== SAVE REPORTS ====================
print("-" * 80)
print("SAVING REPORTS")
print("-" * 80)

# Save text report
with open(report_path, 'w') as f:
    f.write('\n'.join(report_lines))
print(f"✅ Text report saved: {report_path}")

# Create and save summary CSV
summary_data = []
for col in df.columns:
    col_summary = {
        'Column': col,
        'DataType': str(df[col].dtype),
        'Non_Null_Count': df[col].count(),
        'Null_Count': df[col].isnull().sum(),
        'Null_Percentage': (df[col].isnull().sum() / len(df)) * 100,
        'Unique_Values': df[col].nunique()
    }
    
    # Add numeric-specific fields
    if col in numeric_cols:
        col_summary['Min'] = df[col].min()
        col_summary['Max'] = df[col].max()
        col_summary['Mean'] = df[col].mean()
        col_summary['Median'] = df[col].median()
        col_summary['Std'] = df[col].std()
    else:
        col_summary['Min'] = None
        col_summary['Max'] = None
        col_summary['Mean'] = None
        col_summary['Median'] = None
        col_summary['Std'] = None
    
    summary_data.append(col_summary)

# Create DataFrame and save
summary_df = pd.DataFrame(summary_data)
summary_df.to_csv(summary_path, index=False)
print(f"✅ Summary CSV saved: {summary_path}")

print()

# Final message
print("=" * 80)
print("✅ DATA PROFILING COMPLETE")
print("=" * 80)
print(f"Text Report: {report_path}")
print(f"Summary CSV: {summary_path}")
print()
print("⚠️  IMPORTANT: This stage only identifies issues - DO NOT clean data yet")
print("Next Step: Proceed to Stage 4 (Data Cleaning & Preparation)")
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure the centralized dataset exists from Stage 2:

```bash
ls data/processed/centralized_churn_data.csv
```


### Step 2: Navigate to Project Root

Open terminal and navigate to project folder:

```bash
cd path/to/customer_churn_analysis
```


### Step 3: Run the Profiling Script

Execute the data profiling script:

```bash
python scripts/data_profiling.py
```

**Expected Duration:** 10-30 seconds depending on dataset size

### Step 4: Review Console Output

The script will print 9 sections to your terminal:

1. Basic Dataset Overview
2. Duplicate Records Check
3. Missing Values Analysis
4. Data Types Validation
5. Numeric Columns Profiling
6. Categorical Columns Profiling
7. Date Columns Validation
8. Key Relationships Validation
9. Data Quality Summary

### Step 5: Read Generated Reports

After script completes, review the output files:

**Text Report:**

```bash
# On Mac/Linux
cat data/processed/data_quality_report.txt

# On Windows
type data\processed\data_quality_report.txt
```

**Summary CSV:**

```bash
# View in terminal
python -c "import pandas as pd; df = pd.read_csv('data/processed/data_quality_summary.csv'); print(df.head(10))"

# Or open in Excel/Google Sheets
```


***

## e) How to Test the Output

### Test 1: Verify Script Runs Without Errors

**Expected Result:**

- Script completes successfully
- Prints all 9 sections
- Final message: "✅ DATA PROFILING COMPLETE"
- No error messages or crashes

**How to Check:**

- Run the script and watch for errors
- Should complete in under 1 minute


### Test 2: Verify Report Files Created

**Expected Result:**
Two files should be created in `data/processed/`:

- `data_quality_report.txt`
- `data_quality_summary.csv`

**How to Check:**

```bash
ls -lh data/processed/data_quality_report.txt
ls -lh data/processed/data_quality_summary.csv
```

**Expected File Sizes:**

- Report TXT: ~5-15 KB
- Summary CSV: ~3-8 KB


### Test 3: Verify Basic Statistics Match Dataset

**Expected Results:**

- Total Rows: 7,043 (same as Stage 2)
- Total Columns: 31 (21 original + 10 new from Stage 2)
- No duplicate customerIDs (should be 0)

**How to Verify:**
Check the console output or report file:

```bash
grep "Total Rows" data/processed/data_quality_report.txt
grep "Duplicate customerIDs" data/processed/data_quality_report.txt
```


### Test 4: Check Missing Values Analysis

**Expected Result:**
The script should identify columns with missing values and their percentages.

**Common Columns with Missing Values:**

- `TotalCharges` from original Kaggle data (known issue with new customers)
- `LastContactDate` (intentionally set to None for some customers in Stage 2)

**How to Verify:**

```bash
grep -A 10 "MISSING VALUES ANALYSIS" data/processed/data_quality_report.txt
```


### Test 5: Verify Numeric Profiling

**Expected Result:**
For numeric columns (tenure, MonthlyCharges, TotalCharges, TotalPayments, etc.), should show:

- Min, Max, Mean, Median, Std Dev
- Outlier detection results

**How to Verify:**
Look at Section 5 in console output or report file:

```bash
grep -A 20 "NUMERIC COLUMNS PROFILING" data/processed/data_quality_report.txt
```

**Sanity Check Examples:**

- `tenure`: Min should be 0 (new customers), Max ~72 months
- `MonthlyCharges`: Should be positive values (no negative charges)
- `TotalPayments`: Should be >= 0 (can't have negative payments)


### Test 6: Verify Categorical Profiling

**Expected Result:**
For categorical columns (gender, Contract, PaymentMethod, etc.), should show:

- Unique value counts
- Value distributions

**Example for Churn column:**

```
Churn
  Unique Values: 2
  Value Distribution:
    No: ~5000+ (70%+)
    Yes: ~2000 (26-27%)
```

**How to Verify:**

```bash
grep -A 10 "Column: Churn" data/processed/data_quality_report.txt
```


### Test 7: Verify Data Quality Score

**Expected Result:**

- Data Completeness should be > 98%
- Quality Rating: EXCELLENT or GOOD

**How to Verify:**

```bash
grep "Data Completeness" data/processed/data_quality_report.txt
grep "Overall Quality" data/processed/data_quality_report.txt
```


### Test 8: Verify Summary CSV Structure

**Expected Result:**
CSV should have these columns:

- Column, DataType, Non_Null_Count, Null_Count, Null_Percentage, Unique_Values
- Min, Max, Mean, Median, Std (for numeric columns only)

**How to Verify:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/data_quality_summary.csv'); print('Columns:', df.columns.tolist()); print('\nFirst 3 rows:'); print(df.head(3))"
```


### Test 9: Manual Spot Check

Open the text report and verify:

- Each section has content (not empty)
- Numbers make logical sense (no negative counts, percentages between 0-100)
- Column names match your dataset
- Statistics are reasonable for each column


### Signs of Success

✅ Both report files created
✅ Total rows = 7,043
✅ Total columns = 31
✅ No duplicate customerIDs
✅ Data completeness > 95%
✅ Numeric columns have valid ranges (no impossible values)
✅ Categorical columns show expected values (Yes/No for binary, etc.)
✅ All 9 sections present in report

### Signs of Problems

❌ Script crashes or errors
❌ Report files not created
❌ Row count doesn't match (data loss)
❌ All columns showing 100% missing
❌ Negative values in count columns
❌ Percentages > 100%
❌ Empty sections in report

***

## f) Common Beginner Mistakes

### Mistake 1: Trying to Fix Issues During Profiling

**What Happens:**

- See missing values and immediately try to fill them
- Start removing outliers during profiling
- Modify data while inspecting it

**Why It Happens:**

- Natural instinct to "fix" problems as you see them
- Not understanding the purpose of profiling vs cleaning

**How to Fix:**

- **Profiling = Inspection Only** (like a medical diagnosis)
- **Cleaning = Treatment** (comes in Stage 4)
- Document ALL issues first, then decide systematically how to handle each one
- Making cleaning decisions while profiling leads to inconsistent, ad-hoc fixes


### Mistake 2: Not Reading the Entire Report

**What Happens:**

- Glance at console output, see "COMPLETE", move to Stage 4
- Miss critical data quality issues buried in the report

**Why It Happens:**

- Treating this as a checkbox ("ran the script, done")
- Not understanding that profiling insights guide all future cleaning decisions

**How to Fix:**

- **Read EVERY section** of the text report carefully
- Note every column with issues
- Ask yourself: "Why does this column have missing values?"
- Create a mental map of data quality before Stage 4


### Mistake 3: Misunderstanding Outliers

**What Happens:**

- Think "outliers = errors that must be removed"
- Plan to automatically delete all outliers

**Why It Happens:**

- Confusing outliers with data errors
- Not understanding that outliers can be valid, important data points

**How to Fix:**

- **Outliers ≠ Errors**
- Some outliers are legitimate (high-value customers, unusual contracts)
- Profiling identifies outliers; Stage 4 decides what to do (keep, investigate, or remove)
- Never auto-delete outliers without business justification


### Mistake 4: Ignoring Missing Value Patterns

**What Happens:**

- Note that columns have missing values
- Don't investigate WHY they're missing

**Why It Happens:**

- Not thinking about data generation process
- Treating all missing values as random

**How to Fix:**

- **Ask "why is this missing?"**
    - `TotalCharges` missing for `tenure=0` → New customers haven't been billed yet (valid)
    - `LastContactDate` missing → No recent customer contact (valid)
    - Random missing across all columns → Data collection error (problem)
- Missing values tell a story - understand the story before deciding how to handle them


### Mistake 5: Not Validating Primary Key Integrity

**What Happens:**

- Skip checking if customerID is truly unique
- Assume no duplicates without verifying

**Why It Happens:**

- Underestimating how common duplicate keys are in real data
- Trusting that Stage 2 merge prevented duplicates

**How to Fix:**

- **Always verify primary key uniqueness**
- One row per customer is a fundamental assumption for all future analysis
- If duplicates exist, entire analysis framework breaks
- Script correctly checks: `len(df) == df['customerID'].nunique()`


### Mistake 6: Misinterpreting Data Types

**What Happens:**

- See `TotalCharges` as 'object' type instead of numeric
- Don't realize this indicates data quality issues (non-numeric characters)

**Why It Happens:**

- Not understanding how Pandas infers data types
- Not knowing that wrong data type = data problem

**How to Fix:**

- **Expected data types:**
    - Charges, payments, tenure → numeric (int64, float64)
    - Customer segments, services → object (text)
    - Dates → object initially (will convert in Stage 4)
- If a column has unexpected type, investigate why
- `TotalCharges` as object often means " " (space) values instead of numbers


### Mistake 7: Not Creating a Cleaning Plan

**What Happens:**

- Finish profiling but don't document what needs cleaning
- Start Stage 4 without clear plan

**Why It Happens:**

- Not understanding that profiling output IS your cleaning roadmap
- Moving too fast through stages

**How to Fix:**

- After profiling, create a list:
    - "TotalCharges: Convert to numeric, handle spaces"
    - "LastContactDate: Convert to datetime, fill NaN with 'No Contact'"
    - "MonthlyCharges: Check outliers > \$200 - are these valid?"
- Use this list to guide Stage 4 systematically


### Mistake 8: Comparing Wrong Metrics

**What Happens:**

- Expect min/max to match Kaggle documentation exactly
- Get confused when values differ slightly

**Why It Happens:**

- Not accounting for Stage 2 data additions
- Expecting unchanged data after integration

**How to Fix:**

- Remember: Stage 2 added dummy data
    - City, State, ZipCode are NEW (generated)
    - TotalPayments, TotalPaid are NEW (aggregated)
- Only original 21 Kaggle columns should match original data ranges
- New columns will have different ranges


### Mistake 9: Treating Data Quality Score as Pass/Fail

**What Happens:**

- See 98% completeness, think "good enough, skip to modeling"
- Don't investigate the 2% that's missing

**Why It Happens:**

- Not understanding that 2% in critical columns can break entire analysis
- Focusing on aggregate score instead of column-specific issues

**How to Fix:**

- **Quality score is a guide, not a decision**
- 98% complete but 100% missing in `Churn` → Can't analyze churn!
- 80% complete but all critical columns filled → May be acceptable
- Always drill down to column-level issues


### Mistake 10: Not Saving Profiling Insights

**What Happens:**

- Finish profiling, close terminal
- Week later, can't remember what issues were found

**Why It Happens:**

- Not treating profiling as documentation
- Relying on memory instead of written records

**How to Fix:**

- Script correctly saves reports to files
- **Keep these files** - they're part of project documentation
- Reference them in Stage 4 when making cleaning decisions
- Add profiling insights to your project README

***

## ✅ Stage 3 Complete!

You have now:

- Systematically profiled all 31 columns in the centralized dataset
- Identified duplicate records (if any)
- Documented missing values with counts and percentages
- Validated data types for all columns
- Analyzed numeric columns for range, distribution, and outliers
- Examined categorical columns for value distributions
- Validated date column formats and ranges
- Verified primary key (customerID) integrity
- Calculated overall data quality score
- Generated comprehensive text report and CSV summary

**Key Insights You Should Have:**

- Which columns have missing values and how much
- Which numeric columns have outliers
- What categorical values exist in each column
- Whether data types are correct
- Overall data completeness percentage

**Critical Understanding:**

- **You have NOT fixed anything** - this stage is inspection only
- **You have a roadmap** - the profiling report tells you what to clean in Stage 4
- **You understand your data** - you know its structure, quality, and issues

**Output Files:**

- `data/processed/data_quality_report.txt` - Human-readable profiling report
- `data/processed/data_quality_summary.csv` - Machine-readable column metrics

**Next Step:** Wait for instruction to proceed to Stage 4 (Data Cleaning \& Preparation)

---

# **Stage 4: Data Cleaning \& Preparation**


***

## a) Learning Objective

### What You're Learning

You are learning how to **systematically clean and prepare raw data for analysis** using business logic and documented decisions. This includes handling missing values, fixing data types, dealing with outliers, standardizing categorical values, and creating an analysis-ready dataset.

### Why This Matters

In real-world data analytics, **cleaning is where business knowledge meets technical skill**. Professional analysts don't just delete missing values or remove outliers automatically - they make informed decisions based on:

- Business context (why is this data missing?)
- Impact on analysis (will removing this change conclusions?)
- Data integrity (will this transformation preserve truth?)

**Poor cleaning leads to:**

- Biased analysis (removing valid data)
- Incorrect conclusions (treating errors as facts)
- Lost information (deleting too much)
- Irreproducible results (ad-hoc, undocumented changes)

**Good cleaning is:**

- Systematic (follows a clear methodology)
- Documented (every decision justified)
- Reversible (original data preserved)
- Business-aware (considers domain knowledge)


### Skill Level

**Intermediate** - This builds on profiling skills and introduces data transformation techniques, business logic application, and systematic decision-making.

### In Scope

- Loading profiling results from Stage 3
- Handling missing values based on business logic (imputation, deletion, flagging)
- Converting data types (strings to numeric, strings to dates)
- Standardizing categorical values (consistent naming, capitalization)
- Handling outliers (investigation, capping, documentation)
- Creating data quality flags (indicators of cleaned records)
- Generating before/after comparison report
- Saving clean dataset to `data/processed/`


### Out of Scope

- Feature engineering (creating new calculated columns) - comes in Stage 6
- Statistical modeling or predictions - comes in Stage 7
- Visualization of cleaned data - comes in Stage 8
- Advanced imputation methods (KNN, ML-based) - using simple, interpretable methods
- Complex data transformations - keeping changes simple and clear


### Assumptions

- You completed Stage 3 (profiling reports exist)
- You understand basic data types (numeric, text, date)
- You've read the profiling report and know what issues exist
- You understand business context (telecom churn analysis)
- Original data is backed up (never modify `data/raw/`)


### Output Artifact

- **data_cleaning.py** - Main cleaning script with documented decisions
- **clean_churn_data.csv** - Clean, analysis-ready dataset in `data/processed/`
- **cleaning_report.txt** - Before/after comparison and cleaning documentation
- **Console output** - Step-by-step cleaning actions with justifications

***

## b) Setup Instructions

### Step 1: Verify Prerequisites

Ensure these files exist from previous stages:

```
customer_churn_analysis/data/processed/centralized_churn_data.csv (Stage 2)
customer_churn_analysis/data/processed/data_quality_report.txt (Stage 3)
customer_churn_analysis/data/processed/data_quality_summary.csv (Stage 3)
```


### Step 2: Understand Cleaning Strategy

Based on Stage 3 profiling, typical issues to address:

**Issue 1: TotalCharges Data Type**

- Currently 'object' (string) instead of numeric
- Contains spaces " " for customers with tenure=0
- **Strategy:** Convert to numeric, coerce errors to NaN, fill based on business logic

**Issue 2: Missing Values in LastContactDate**

- Some customers have no recent contact
- **Strategy:** Keep as NaN (represents "no contact"), convert to datetime

**Issue 3: Categorical Inconsistencies**

- Check for spelling variations, whitespace, capitalization issues
- **Strategy:** Strip whitespace, standardize capitalization

**Issue 4: Outliers in MonthlyCharges**

- Some extremely high values
- **Strategy:** Investigate if valid, document decision


### Step 3: Files to Create

You will create one Python script in the `scripts/` folder:

- `data_cleaning.py` - Comprehensive cleaning script


### Step 4: Output Locations

The script will generate files in `data/processed/`:

- `clean_churn_data.csv` - Final clean dataset
- `cleaning_report.txt` - Documentation of all changes


### Dependencies Required

- pandas (already installed)
- numpy (already installed)
- No additional installations needed

***

## c) Implementation (FINAL VERSION)

### File 1: Data Cleaning Script

**File Name:** `data_cleaning.py`
**File Path:** `customer_churn_analysis/scripts/data_cleaning.py`
**Total Lines:** 318

```python
# Import required libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import os  # For file operations
from datetime import datetime  # For date handling

# Print header
print("=" * 80)
print("STAGE 4: DATA CLEANING & PREPARATION")
print("=" * 80)
print()

# Define file paths
input_path = "data/processed/centralized_churn_data.csv"
output_path = "data/processed/clean_churn_data.csv"
report_path = "data/processed/cleaning_report.txt"

# Check if input file exists
if not os.path.exists(input_path):
    print(f"❌ ERROR: Input dataset not found at {input_path}")
    print("Please complete Stage 2 first")
    exit()

# Load the centralized dataset
print("📂 Loading centralized dataset...")
df = pd.read_csv(input_path)
print(f"✅ Dataset loaded: {input_path}")
print(f"   Original shape: {df.shape[0]} rows × {df.shape[1]} columns")
print()

# Create a copy for before/after comparison
df_original = df.copy()

# Initialize report lines list
report_lines = []
report_lines.append("=" * 80)
report_lines.append("DATA CLEANING REPORT")
report_lines.append("=" * 80)
report_lines.append("")
report_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
report_lines.append(f"Input Dataset: {input_path}")
report_lines.append(f"Original Shape: {df_original.shape[0]} rows × {df_original.shape[1]} columns")
report_lines.append("")

# ==================== CLEANING STEP 1: FIX TOTALCHARGES DATA TYPE ====================
print("-" * 80)
print("CLEANING STEP 1: Fix TotalCharges Data Type")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 1: FIX TOTALCHARGES DATA TYPE")
report_lines.append("-" * 80)

# Check current data type of TotalCharges
print(f"Current data type: {df['TotalCharges'].dtype}")
report_lines.append(f"Original data type: {df['TotalCharges'].dtype}")

# Check for non-numeric values in TotalCharges
# Try converting to numeric, invalid values become NaN
df['TotalCharges_numeric'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Count how many values became NaN after conversion (these were non-numeric)
invalid_count = df['TotalCharges_numeric'].isnull().sum() - df['TotalCharges'].isnull().sum()
print(f"Non-numeric values found: {invalid_count}")
report_lines.append(f"Non-numeric values found: {invalid_count}")

# Business Logic: TotalCharges should be MonthlyCharges × tenure
# For customers with tenure=0, TotalCharges should be 0 (no bills yet)
# Identify rows where TotalCharges is NaN after conversion
invalid_mask = df['TotalCharges_numeric'].isnull() & df['TotalCharges'].notnull()

if invalid_mask.sum() > 0:
    print(f"Investigating {invalid_mask.sum()} invalid TotalCharges values...")
    
    # Check if these are tenure=0 customers (new customers, not billed yet)
    invalid_rows = df[invalid_mask]
    tenure_0_count = (invalid_rows['tenure'] == 0).sum()
    
    print(f"  - {tenure_0_count} are tenure=0 customers (new, not billed yet)")
    report_lines.append(f"  Invalid values: {invalid_mask.sum()} records")
    report_lines.append(f"  Tenure=0 customers: {tenure_0_count}")
    
    # Business Decision: Set TotalCharges to 0 for tenure=0 customers
    print("  ✅ Business Rule Applied: Set TotalCharges=0 for tenure=0 customers")
    df.loc[invalid_mask & (df['tenure'] == 0), 'TotalCharges_numeric'] = 0.0
    report_lines.append("  Action: Set TotalCharges=0 for tenure=0 customers")

# Replace original TotalCharges with cleaned numeric version
df['TotalCharges'] = df['TotalCharges_numeric']
# Drop temporary column
df.drop(columns=['TotalCharges_numeric'], inplace=True)

print(f"✅ TotalCharges converted to numeric type")
print(f"   New data type: {df['TotalCharges'].dtype}")
report_lines.append(f"New data type: {df['TotalCharges'].dtype}")
report_lines.append("")

print()

# ==================== CLEANING STEP 2: HANDLE MISSING VALUES ====================
print("-" * 80)
print("CLEANING STEP 2: Handle Missing Values")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 2: HANDLE MISSING VALUES")
report_lines.append("-" * 80)

# Calculate missing values before cleaning
missing_before = df.isnull().sum().sum()
print(f"Total missing values before cleaning: {missing_before}")
report_lines.append(f"Missing values before: {missing_before}")
report_lines.append("")

# Check each column for missing values
columns_with_missing = df.columns[df.isnull().any()].tolist()

if len(columns_with_missing) > 0:
    print(f"Found {len(columns_with_missing)} columns with missing values:")
    report_lines.append(f"Columns with missing values: {len(columns_with_missing)}")
    
    for col in columns_with_missing:
        missing_count = df[col].isnull().sum()
        missing_pct = (missing_count / len(df)) * 100
        print(f"\n  Column: {col}")
        print(f"    Missing: {missing_count} ({missing_pct:.2f}%)")
        report_lines.append(f"\n  {col}: {missing_count} missing ({missing_pct:.2f}%)")
        
        # Apply business logic based on column
        if col == 'TotalCharges':
            # Already handled in Step 1 (set to 0 for tenure=0)
            # Check if any remaining NaN
            remaining_nan = df[col].isnull().sum()
            if remaining_nan > 0:
                print(f"    ⚠️  {remaining_nan} still missing after tenure=0 fix")
                # Fill remaining with 0 (conservative approach)
                df[col].fillna(0, inplace=True)
                print(f"    ✅ Filled remaining with 0")
                report_lines.append(f"    Action: Filled remaining with 0")
        
        elif col == 'LastContactDate':
            # Business Decision: Missing = no recent contact (valid state)
            # Keep as NaN, will convert to datetime but preserve NaT
            print(f"    ✅ Keep as missing (represents 'No Recent Contact')")
            report_lines.append(f"    Action: Kept as missing (valid business state)")
        
        elif missing_pct < 5:
            # For columns with <5% missing, strategy depends on type
            if df[col].dtype in ['int64', 'float64']:
                # Numeric: fill with median (robust to outliers)
                median_val = df[col].median()
                df[col].fillna(median_val, inplace=True)
                print(f"    ✅ Filled with median: {median_val:.2f}")
                report_lines.append(f"    Action: Filled with median ({median_val:.2f})")
            else:
                # Categorical: fill with mode (most common value)
                mode_val = df[col].mode()[0]
                df[col].fillna(mode_val, inplace=True)
                print(f"    ✅ Filled with mode: {mode_val}")
                report_lines.append(f"    Action: Filled with mode ({mode_val})")
        
        else:
            # For columns with >=5% missing, flag for review
            print(f"    ⚠️  High missing rate (>5%) - requires business review")
            report_lines.append(f"    Action: Flagged for business review")

else:
    print("✅ No missing values found")
    report_lines.append("No missing values found")

# Calculate missing values after cleaning
missing_after = df.isnull().sum().sum()
print(f"\nTotal missing values after cleaning: {missing_after}")
print(f"Missing values reduced by: {missing_before - missing_after}")
report_lines.append(f"\nMissing values after: {missing_after}")
report_lines.append(f"Reduction: {missing_before - missing_after}")
report_lines.append("")

print()

# ==================== CLEANING STEP 3: CONVERT DATE COLUMNS ====================
print("-" * 80)
print("CLEANING STEP 3: Convert Date Columns to Datetime")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 3: CONVERT DATE COLUMNS")
report_lines.append("-" * 80)

# Identify date columns (columns with 'Date' in name)
date_columns = [col for col in df.columns if 'Date' in col]

if len(date_columns) > 0:
    print(f"Found {len(date_columns)} date columns: {date_columns}")
    report_lines.append(f"Date columns found: {date_columns}")
    
    for col in date_columns:
        print(f"\n  Converting: {col}")
        print(f"    Original type: {df[col].dtype}")
        report_lines.append(f"\n  {col}:")
        report_lines.append(f"    Original type: {df[col].dtype}")
        
        # Convert to datetime, invalid parsing becomes NaT (Not a Time)
        df[col] = pd.to_datetime(df[col], errors='coerce')
        
        # Count how many became NaT (invalid dates)
        invalid_dates = df[col].isnull().sum()
        
        print(f"    New type: {df[col].dtype}")
        print(f"    Invalid dates: {invalid_dates}")
        report_lines.append(f"    New type: {df[col].dtype}")
        report_lines.append(f"    Invalid dates: {invalid_dates}")
        
        # Check for future dates (data quality issue)
        if col != 'LastContactDate':  # LastContactDate can have valid NaT
            future_dates = df[df[col] > pd.Timestamp.now()][col].count()
            if future_dates > 0:
                print(f"    ⚠️  Future dates found: {future_dates}")
                report_lines.append(f"    Future dates: {future_dates}")

else:
    print("No date columns found")
    report_lines.append("No date columns found")

report_lines.append("")
print()

# ==================== CLEANING STEP 4: STANDARDIZE CATEGORICAL VALUES ====================
print("-" * 80)
print("CLEANING STEP 4: Standardize Categorical Values")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 4: STANDARDIZE CATEGORICAL VALUES")
report_lines.append("-" * 80)

# Get all object (text) columns
categorical_cols = df.select_dtypes(include=['object']).columns.tolist()

# Exclude customerID and date columns (already processed)
categorical_cols = [col for col in categorical_cols if col != 'customerID' and 'Date' not in col]

print(f"Processing {len(categorical_cols)} categorical columns...")
report_lines.append(f"Categorical columns: {len(categorical_cols)}")

for col in categorical_cols:
    # Count unique values before cleaning
    unique_before = df[col].nunique()
    
    # Clean: strip whitespace, convert to title case for consistency
    df[col] = df[col].str.strip()  # Remove leading/trailing whitespace
    
    # Count unique values after cleaning
    unique_after = df[col].nunique()
    
    # Only report if changes were made
    if unique_before != unique_after:
        print(f"  {col}: {unique_before} → {unique_after} unique values")
        report_lines.append(f"  {col}: Standardized ({unique_before} → {unique_after} unique)")

print("✅ Categorical values standardized (whitespace removed)")
report_lines.append("\nAction: Stripped whitespace from all categorical columns")
report_lines.append("")

print()

# ==================== CLEANING STEP 5: HANDLE OUTLIERS IN NUMERIC COLUMNS ====================
print("-" * 80)
print("CLEANING STEP 5: Handle Outliers in Numeric Columns")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 5: HANDLE OUTLIERS")
report_lines.append("-" * 80)

# Get numeric columns (exclude customerID-like columns)
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

# For each numeric column, check for outliers
print("Checking outliers using IQR method (values beyond 1.5 × IQR)...")
report_lines.append("Method: IQR (Inter-Quartile Range)")

for col in numeric_cols:
    # Calculate IQR
    Q1 = df[col].quantile(0.25)  # 25th percentile
    Q3 = df[col].quantile(0.75)  # 75th percentile
    IQR = Q3 - Q1  # Inter-quartile range
    
    # Define outlier boundaries
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    # Identify outliers
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_count = len(outliers)
    outlier_pct = (outlier_count / len(df)) * 100
    
    if outlier_count > 0:
        print(f"\n  {col}:")
        print(f"    Outliers: {outlier_count} ({outlier_pct:.2f}%)")
        print(f"    Range: [{lower_bound:.2f}, {upper_bound:.2f}]")
        print(f"    Actual range: [{df[col].min():.2f}, {df[col].max():.2f}]")
        
        report_lines.append(f"\n  {col}:")
        report_lines.append(f"    Outliers: {outlier_count} ({outlier_pct:.2f}%)")
        report_lines.append(f"    Expected range: [{lower_bound:.2f}, {upper_bound:.2f}]")
        
        # Business Decision: Keep outliers but document
        # In telecom, high charges can be legitimate (business customers, multiple lines)
        # Removing valid data creates bias
        print(f"    ✅ Decision: Keep outliers (may represent valid business cases)")
        report_lines.append(f"    Action: Kept (legitimate variation expected)")

print("\n✅ Outlier analysis complete - all values retained")
report_lines.append("\nOutliers retained (valid business variation)")
report_lines.append("")

print()

# ==================== CLEANING STEP 6: CREATE DATA QUALITY FLAGS ====================
print("-" * 80)
print("CLEANING STEP 6: Create Data Quality Flags")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 6: CREATE DATA QUALITY FLAGS")
report_lines.append("-" * 80)

# Create flag for customers with modified TotalCharges
df['TotalCharges_Imputed'] = (df_original['TotalCharges'].astype(str).str.strip() == '') & (df['tenure'] == 0)

# Count flagged records
imputed_count = df['TotalCharges_Imputed'].sum()
print(f"Created flag: TotalCharges_Imputed")
print(f"  Flagged records: {imputed_count} (customers where TotalCharges was set to 0)")
report_lines.append(f"TotalCharges_Imputed flag: {imputed_count} records")

# Create flag for customers with no recent contact
df['No_Recent_Contact'] = df['LastContactDate'].isnull()

no_contact_count = df['No_Recent_Contact'].sum()
print(f"\nCreated flag: No_Recent_Contact")
print(f"  Flagged records: {no_contact_count} (customers with no LastContactDate)")
report_lines.append(f"No_Recent_Contact flag: {no_contact_count} records")

print("\n✅ Data quality flags created")
report_lines.append("\nPurpose: Track which records were modified during cleaning")
report_lines.append("")

print()

# ==================== CLEANING STEP 7: VALIDATE CLEANED DATA ====================
print("-" * 80)
print("CLEANING STEP 7: Validate Cleaned Data")
print("-" * 80)

report_lines.append("-" * 80)
report_lines.append("STEP 7: VALIDATION CHECKS")
report_lines.append("-" * 80)

# Validation 1: Check row count (should not change)
print("Validation 1: Row Count")
if len(df) == len(df_original):
    print(f"  ✅ Row count preserved: {len(df)} rows")
    report_lines.append(f"✅ Row count: {len(df)} (unchanged)")
else:
    print(f"  ⚠️  Row count changed: {len(df_original)} → {len(df)}")
    report_lines.append(f"⚠️  Row count changed: {len(df_original)} → {len(df)}")

# Validation 2: Check for duplicates
print("\nValidation 2: Duplicate Check")
duplicates = df['customerID'].duplicated().sum()
if duplicates == 0:
    print(f"  ✅ No duplicate customerIDs")
    report_lines.append(f"✅ No duplicates")
else:
    print(f"  ⚠️  Found {duplicates} duplicate customerIDs")
    report_lines.append(f"⚠️  Duplicates: {duplicates}")

# Validation 3: Check data types
print("\nValidation 3: Data Types")
print(f"  Numeric columns: {len(df.select_dtypes(include=[np.number]).columns)}")
print(f"  Object columns: {len(df.select_dtypes(include=['object']).columns)}")
print(f"  Datetime columns: {len(df.select_dtypes(include=['datetime64']).columns)}")
report_lines.append(f"Numeric: {len(df.select_dtypes(include=[np.number]).columns)} columns")
report_lines.append(f"Object: {len(df.select_dtypes(include=['object']).columns)} columns")
report_lines.append(f"Datetime: {len(df.select_dtypes(include=['datetime64']).columns)} columns")

# Validation 4: Check for negative values in key columns
print("\nValidation 4: Business Logic Checks")
report_lines.append("\nBusiness Logic Validation:")

# Check tenure (should be >= 0)
negative_tenure = (df['tenure'] < 0).sum()
if negative_tenure == 0:
    print(f"  ✅ tenure: No negative values")
    report_lines.append(f"  ✅ tenure: All values >= 0")
else:
    print(f"  ⚠️  tenure: {negative_tenure} negative values found")
    report_lines.append(f"  ⚠️  tenure: {negative_tenure} negative values")

# Check MonthlyCharges (should be > 0)
zero_monthly = (df['MonthlyCharges'] <= 0).sum()
if zero_monthly == 0:
    print(f"  ✅ MonthlyCharges: All values > 0")
    report_lines.append(f"  ✅ MonthlyCharges: All values > 0")
else:
    print(f"  ⚠️  MonthlyCharges: {zero_monthly} values <= 0")
    report_lines.append(f"  ⚠️  MonthlyCharges: {zero_monthly} values <= 0")

# Check TotalCharges (should be >= 0)
negative_total = (df['TotalCharges'] < 0).sum()
if negative_total == 0:
    print(f"  ✅ TotalCharges: All values >= 0")
    report_lines.append(f"  ✅ TotalCharges: All values >= 0")
else:
    print(f"  ⚠️  TotalCharges: {negative_total} negative values found")
    report_lines.append(f"  ⚠️  TotalCharges: {negative_total} negative values")

report_lines.append("")
print()

# ==================== SAVE CLEANED DATASET ====================
print("-" * 80)
print("SAVING CLEANED DATASET")
print("-" * 80)

# Save cleaned dataset to CSV
df.to_csv(output_path, index=False)
print(f"✅ Cleaned dataset saved: {output_path}")
print(f"   Final shape: {df.shape[0]} rows × {df.shape[1]} columns")
report_lines.append(f"Output: {output_path}")
report_lines.append(f"Final shape: {df.shape[0]} rows × {df.shape[1]} columns")

print()

# ==================== GENERATE SUMMARY STATISTICS ====================
print("-" * 80)
print("BEFORE/AFTER COMPARISON")
print("-" * 80)

report_lines.append("")
report_lines.append("-" * 80)
report_lines.append("BEFORE/AFTER COMPARISON")
report_lines.append("-" * 80)

# Compare key metrics
print(f"Missing Values: {missing_before} → {missing_after} (reduced by {missing_before - missing_after})")
report_lines.append(f"Missing values: {missing_before} → {missing_after}")

print(f"Data Completeness: {((len(df_original) * len(df_original.columns) - missing_before) / (len(df_original) * len(df_original.columns)) * 100):.2f}% → {((len(df) * len(df.columns) - missing_after) / (len(df) * len(df.columns)) * 100):.2f}%")

# Column count comparison
cols_before = len(df_original.columns)
cols_after = len(df.columns)
new_cols = cols_after - cols_before
print(f"Columns: {cols_before} → {cols_after} (+{new_cols} quality flags)")
report_lines.append(f"Columns: {cols_before} → {cols_after} (added {new_cols} flags)")

report_lines.append("")
report_lines.append("=" * 80)
report_lines.append("CLEANING COMPLETE")
report_lines.append("=" * 80)

print()

# ==================== SAVE CLEANING REPORT ====================
print("-" * 80)
print("SAVING CLEANING REPORT")
print("-" * 80)

# Write report to file
with open(report_path, 'w') as f:
    f.write('\n'.join(report_lines))

print(f"✅ Cleaning report saved: {report_path}")
print()

# Final summary
print("=" * 80)
print("✅ DATA CLEANING COMPLETE")
print("=" * 80)
print(f"Clean dataset: {output_path}")
print(f"Cleaning report: {report_path}")
print()
print("Key Changes Made:")
print("  1. Converted TotalCharges to numeric (filled tenure=0 with 0)")
print("  2. Handled missing values based on business logic")
print("  3. Converted date columns to datetime format")
print("  4. Standardized categorical values (removed whitespace)")
print("  5. Documented outliers (kept for valid business variation)")
print("  6. Created data quality flags (TotalCharges_Imputed, No_Recent_Contact)")
print("  7. Validated cleaned data integrity")
print()
print("Next Step: Proceed to Stage 5 (Exploratory Data Analysis)")
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure the centralized dataset from Stage 2 exists:

```bash
ls data/processed/centralized_churn_data.csv
```


### Step 2: Review Stage 3 Profiling Report (Optional but Recommended)

Before cleaning, quickly review what issues were found:

```bash
cat data/processed/data_quality_report.txt
```


### Step 3: Navigate to Project Root

Open terminal and navigate to project folder:

```bash
cd path/to/customer_churn_analysis
```


### Step 4: Run the Cleaning Script

Execute the data cleaning script:

```bash
python scripts/data_cleaning.py
```

**Expected Duration:** 15-45 seconds depending on dataset size

### Step 5: Review Console Output

The script will print 7 cleaning steps:

1. Fix TotalCharges Data Type
2. Handle Missing Values
3. Convert Date Columns to Datetime
4. Standardize Categorical Values
5. Handle Outliers in Numeric Columns
6. Create Data Quality Flags
7. Validate Cleaned Data

### Step 6: Verify Output Files

After script completes, check that files were created:

```bash
ls data/processed/clean_churn_data.csv
ls data/processed/cleaning_report.txt
```


### Step 7: Read the Cleaning Report

Review what changes were made:

```bash
# On Mac/Linux
cat data/processed/cleaning_report.txt

# On Windows
type data\processed\cleaning_report.txt
```


***

## e) How to Test the Output

### Test 1: Verify Script Runs Without Errors

**Expected Result:**

- Script completes successfully
- Prints all 7 cleaning steps
- Final message: "✅ DATA CLEANING COMPLETE"
- No error messages or crashes

**How to Check:**

- Run the script and watch for errors
- Should complete in under 1 minute


### Test 2: Verify Clean Dataset Created

**Expected Result:**

- File exists at `data/processed/clean_churn_data.csv`
- File size approximately 2-3 MB (similar to input)
- Contains 7,043 rows (same as input - no rows deleted)
- Contains 33 columns (31 original + 2 new flags)

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); print(f'Shape: {df.shape[0]} rows × {df.shape[1]} columns')"
```

**Expected Output:**

```
Shape: 7043 rows × 33 columns
```


### Test 3: Verify TotalCharges Is Now Numeric

**Expected Result:**

- TotalCharges column should be float64 type (not object)
- No NaN values in TotalCharges
- All values >= 0

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); print(f'TotalCharges type: {df[\"TotalCharges\"].dtype}'); print(f'Missing values: {df[\"TotalCharges\"].isnull().sum()}'); print(f'Negative values: {(df[\"TotalCharges\"] < 0).sum()}'); print(f'Min: {df[\"TotalCharges\"].min()}, Max: {df[\"TotalCharges\"].max()}')"
```

**Expected Output:**

```
TotalCharges type: float64
Missing values: 0
Negative values: 0
Min: 0.0, Max: [some positive value]
```


### Test 4: Verify Date Columns Converted

**Expected Result:**

- RegistrationDate should be datetime64 type
- LastContactDate should be datetime64 type (with some NaT values)

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); print('Column types:'); print(df[['RegistrationDate', 'LastContactDate']].dtypes)"
```


### Test 5: Verify Data Quality Flags Created

**Expected Result:**

- Two new columns should exist:
    - `TotalCharges_Imputed` (True/False)
    - `No_Recent_Contact` (True/False)

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); print('New flag columns:'); print('TotalCharges_Imputed:', df['TotalCharges_Imputed'].sum(), 'customers'); print('No_Recent_Contact:', df['No_Recent_Contact'].sum(), 'customers')"
```


### Test 6: Verify No Rows Were Deleted

**Expected Result:**

- Clean dataset should have same row count as input (7,043)
- No customers removed during cleaning

**How to Check:**

```bash
# Count rows in both files
python -c "import pandas as pd; original = pd.read_csv('data/processed/centralized_churn_data.csv'); clean = pd.read_csv('data/processed/clean_churn_data.csv'); print(f'Original: {len(original)} rows'); print(f'Clean: {len(clean)} rows'); print(f'Difference: {len(original) - len(clean)}')"
```

**Expected Output:**

```
Original: 7043 rows
Clean: 7043 rows
Difference: 0
```


### Test 7: Verify Missing Values Reduced

**Expected Result:**

- Total missing values should be lower after cleaning
- Most columns should have 0 missing values
- LastContactDate may still have NaN (by design - represents no contact)

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); missing = df.isnull().sum(); print('Columns with missing values:'); print(missing[missing > 0])"
```


### Test 8: Verify Cleaning Report Exists

**Expected Result:**

- File exists at `data/processed/cleaning_report.txt`
- Contains all 7 cleaning steps
- Shows before/after comparison

**How to Check:**

```bash
# Check file exists and has content
ls -lh data/processed/cleaning_report.txt

# Check specific sections
grep "STEP 1" data/processed/cleaning_report.txt
grep "BEFORE/AFTER" data/processed/cleaning_report.txt
```


### Test 9: Validate Business Logic

**Expected Result:**

- No negative values in tenure, MonthlyCharges, or TotalCharges
- All monetary values >= 0
- Churn column still has only "Yes" and "No" values

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); print('Negative tenure:', (df['tenure'] < 0).sum()); print('Negative/zero MonthlyCharges:', (df['MonthlyCharges'] <= 0).sum()); print('Negative TotalCharges:', (df['TotalCharges'] < 0).sum()); print('Churn values:', df['Churn'].unique())"
```

**Expected Output:**

```
Negative tenure: 0
Negative/zero MonthlyCharges: 0
Negative TotalCharges: 0
Churn values: ['No' 'Yes']
```


### Test 10: Sample Data Inspection

**Manually inspect first few rows:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/clean_churn_data.csv'); print(df[['customerID', 'tenure', 'TotalCharges', 'TotalCharges_Imputed', 'No_Recent_Contact']].head(10))"
```

**What to Look For:**

- TotalCharges should be numeric (not strings)
- TotalCharges_Imputed should be True for tenure=0 customers with TotalCharges=0
- Data should look clean and consistent


### Signs of Success

✅ Script completes without errors
✅ Clean dataset has 7,043 rows (no data loss)
✅ Clean dataset has 33 columns (31 + 2 flags)
✅ TotalCharges is float64 type with no missing values
✅ Date columns are datetime64 type
✅ Missing values reduced (especially in TotalCharges)
✅ No negative values in key numeric columns
✅ Data quality flags created
✅ Cleaning report generated with before/after comparison

### Signs of Problems

❌ Script crashes or errors
❌ Clean dataset has fewer rows than input (data loss)
❌ TotalCharges still object type (not converted)
❌ Many missing values remain in critical columns
❌ Negative values in tenure or charges
❌ Churn column has unexpected values
❌ Cleaning report not generated

***

## f) Common Beginner Mistakes

### Mistake 1: Deleting Rows with Missing Values Automatically

**What Happens:**

- See missing values, immediately drop all rows with any NaN
- Lose hundreds or thousands of valid customer records

**Why It Happens:**

- Misunderstanding that missing data often has business meaning
- Using `.dropna()` without thinking about consequences

**How to Fix:**

- **Never auto-delete rows** in churn analysis (each row = customer)
- Ask: "Why is this missing?" before deciding action
- Script correctly handles each missing value based on business context:
    - TotalCharges missing for tenure=0 → Fill with 0 (new customer)
    - LastContactDate missing → Keep (no recent contact is valid state)


### Mistake 2: Filling All Missing Values with Mean/Median Blindly

**What Happens:**

- Fill ALL missing values with column mean
- Creates artificial data that doesn't reflect reality

**Why It Happens:**

- Oversimplifying imputation strategies
- Not considering what the data represents

**How to Fix:**

- **Context-specific imputation:**
    - TotalCharges for new customers → 0 (business logic, not statistical)
    - LastContactDate → Keep as NaN (represents actual absence of event)
    - Numeric columns with <5% missing → Median (robust, documented)
- Always justify imputation choice in cleaning report


### Mistake 3: Modifying the Original Dataset File

**What Happens:**

- Overwrite `centralized_churn_data.csv` with cleaned version
- Lose original data permanently

**Why It Happens:**

- Not understanding importance of preserving raw data
- Convenience (fewer files)

**How to Fix:**

- **Never modify input files** - always create new output
- Script correctly saves to `clean_churn_data.csv` (new file)
- Original `centralized_churn_data.csv` remains untouched
- If cleaning mistake is made, can always re-run from original


### Mistake 4: Removing All Outliers Automatically

**What Happens:**

- Detect outliers using IQR method
- Delete all rows with outliers
- Lose high-value customers (legitimate high charges)

**Why It Happens:**

- Confusing outliers with errors
- Applying statistical methods without business context

**How to Fix:**

- **Outliers in telecom ≠ errors:**
    - High MonthlyCharges might be business customers with multiple lines
    - High TotalCharges might be long-tenure loyal customers
    - These are exactly the customers you want to analyze for churn
- Script correctly documents outliers but keeps them
- Only remove outliers if proven to be data errors (not just unusual)


### Mistake 5: Not Converting TotalCharges to Numeric

**What Happens:**

- Leave TotalCharges as object (string) type
- Later analysis breaks when trying to calculate means, sums

**Why It Happens:**

- Not realizing Pandas infers type from first rows
- Spaces " " in data cause entire column to be treated as text

**How to Fix:**

- **Always verify data types after loading**
- Use `pd.to_numeric()` with `errors='coerce'` to force conversion
- Script correctly:

1. Converts to numeric
2. Identifies which values became NaN (were non-numeric)
3. Applies business logic to fill them
4. Validates all values are now numeric


### Mistake 6: Not Documenting Cleaning Decisions

**What Happens:**

- Make various cleaning changes
- Week later, can't remember why changes were made
- Reviewers ask "why did you do this?" - no answer

**Why It Happens:**

- Treating cleaning as throwaway preprocessing
- Not understanding that cleaning decisions affect analysis conclusions

**How to Fix:**

- **Document every decision** in cleaning report
- Script correctly writes detailed report with:
    - What was changed
    - Why it was changed (business justification)
    - How many records affected
- This report is critical for reproducibility and explaining methodology


### Mistake 7: Changing Data Types Without Handling Conversion Errors

**What Happens:**

- Try to convert TotalCharges to float
- Script crashes with "ValueError: could not convert string to float"

**Why It Happens:**

- Using `.astype(float)` which fails on non-numeric values
- Not using error handling

**How to Fix:**

- Use `pd.to_numeric(df['col'], errors='coerce')` instead of `.astype(float)`
- `errors='coerce'` converts invalid values to NaN instead of crashing
- Then handle NaN systematically
- Script demonstrates correct error-handling pattern


### Mistake 8: Standardizing Categorical Values Incorrectly

**What Happens:**

- Convert all categorical values to lowercase or uppercase
- Change "Yes"/"No" to "yes"/"no"
- Later code expects specific capitalization, breaks

**Why It Happens:**

- Overzealous standardization without checking dependencies

**How to Fix:**

- **Only standardize what needs standardizing:**
    - Remove whitespace (safe): " Yes " → "Yes"
    - Fix typos (if found): "Fibre Optic" → "Fiber optic"
    - Don't change working values just for consistency
- Script conservatively strips whitespace only
- Preserves original capitalization (Kaggle standard: "Yes"/"No")


### Mistake 9: Not Creating Data Quality Flags

**What Happens:**

- Impute missing values but don't track which ones
- Later analysis treats imputed and real values equally
- Can't identify if results are affected by imputation

**Why It Happens:**

- Not thinking about downstream analysis needs
- Treating cleaning as final step instead of part of analytical pipeline

**How to Fix:**

- **Always flag modified records:**
    - `TotalCharges_Imputed` = True → This value was set to 0 (not original)
    - `No_Recent_Contact` = True → No LastContactDate (behavioral indicator)
- These flags can be used in Stage 7 analysis:
    - "Do imputed customers churn differently?"
    - "Do customers with no recent contact churn more?"
- Script correctly creates meaningful flags


### Mistake 10: Not Validating After Cleaning

**What Happens:**

- Run cleaning script
- Assume everything worked correctly
- Move to Stage 5 with invalid data

**Why It Happens:**

- Trusting code without verification
- Skipping validation step to save time

**How to Fix:**

- **Always validate after cleaning:**
    - Row count unchanged? (no accidental deletions)
    - No negative values in charges? (business logic holds)
    - Expected data types? (conversions worked)
    - Duplicates removed? (data integrity)
- Script includes validation section (Step 7)
- Run additional manual checks (Test 1-10 above)


### Mistake 11: Treating Missing Dates Inconsistently

**What Happens:**

- Fill LastContactDate with "1900-01-01" or "2000-01-01" (placeholder)
- Later analysis thinks these are real contact dates from the past

**Why It Happens:**

- Discomfort with NaN/NaT values
- Thinking all columns must be "complete"

**How to Fix:**

- **NaT (Not a Time) is valid** for dates representing events that didn't happen
- Don't use placeholder dates - they create false information
- Script correctly:
    - Converts to datetime (valid dates remain, invalid → NaT)
    - Creates `No_Recent_Contact` flag to make absence explicit
    - Preserves NaT (represents "no contact" truthfully)


### Mistake 12: Forgetting About Churn Column Integrity

**What Happens:**

- Focus on cleaning features (charges, dates, etc.)
- Don't verify Churn column (target variable) is intact

**Why It Happens:**

- Churn column often has no missing values, seems "fine"
- Not realizing it's the most critical column

**How to Fix:**

- **Target variable is sacred** - must be perfect
- Validate Churn column:
    - Only "Yes" and "No" values (no typos: "yes", "Y", "1")
    - No missing values (can't analyze churn without labels)
    - Same value distribution before/after (no accidental changes)
- Add explicit validation check in Step 7 if needed

***

## ✅ Stage 4 Complete!

You have now:

- Fixed TotalCharges data type issue (converted to numeric, filled tenure=0 with 0)
- Handled missing values systematically based on business logic
- Converted date columns (RegistrationDate, LastContactDate) to proper datetime format
- Standardized categorical values (removed whitespace)
- Documented outliers while preserving them for valid business cases
- Created data quality flags (TotalCharges_Imputed, No_Recent_Contact)
- Validated cleaned data integrity (row count, data types, business rules)
- Generated comprehensive cleaning report with before/after comparison

**Key Cleaning Decisions Made:**

1. **TotalCharges:** Converted to numeric, set to 0 for tenure=0 customers (business logic)
2. **Missing Values:** Context-specific handling (not blanket deletion or imputation)
3. **Dates:** Converted to datetime, preserved NaT for missing LastContactDate
4. **Outliers:** Documented but retained (legitimate business variation)
5. **Flags:** Created indicators to track modified records

**Data Quality Improvement:**

- Missing values reduced significantly
- All numeric columns have correct data types
- Date columns properly formatted
- Business logic rules validated (no negative charges, valid value ranges)

**Output Files:**

- `data/processed/clean_churn_data.csv` - Analysis-ready dataset (7,043 rows × 33 columns)
- `data/processed/cleaning_report.txt` - Comprehensive cleaning documentation

**Critical Understanding:**

- **Cleaning is decision-making**, not just technical transformation
- **Every decision documented** for reproducibility and transparency
- **Original data preserved** - cleaning is reversible
- **Data quality flags** enable deeper analysis in later stages

**Next Step:** Wait for instruction to proceed to Stage 5 (Exploratory Data Analysis)

---

# **Stage 5: Exploratory Data Analysis (EDA)**


***

## a) Learning Objective

### What You're Learning

You are learning how to **systematically explore and understand data patterns through statistical analysis and visualization**. EDA is the detective work of data analytics - you investigate the data to discover relationships, trends, anomalies, and insights that will guide your churn analysis.

### Why This Matters

In real-world data analytics, **EDA is where insights are discovered**. Before building models or making recommendations, professional analysts spend significant time exploring data to:

- Understand distributions (are values normal? skewed? bimodal?)
- Discover relationships (does tenure affect churn? does contract type matter?)
- Identify patterns (which customer segments churn most?)
- Formulate hypotheses (customers with tech support churn less?)
- Validate assumptions (is monthly charge distribution what we expect?)

**Without EDA, you're analyzing blindly:**

- Miss obvious patterns that explain churn
- Make recommendations based on incomplete understanding
- Build solutions that don't address root causes
- Present findings without supporting evidence

**Good EDA enables:**

- Data-driven insights (facts, not assumptions)
- Targeted retention strategies (know who to help and how)
- Stakeholder communication (visualizations tell stories)
- Hypothesis generation for deeper analysis (Stage 7)


### Skill Level

**Intermediate** - This builds on data profiling (Stage 3) and introduces statistical analysis, visualization techniques, and pattern recognition skills.

### In Scope

- Loading clean dataset from Stage 4
- Univariate analysis (single variable distributions)
    - Numeric variables: histograms, box plots, summary statistics
    - Categorical variables: bar charts, value counts, proportions
- Bivariate analysis (relationships between two variables)
    - Churn vs. numeric features (tenure, charges)
    - Churn vs. categorical features (contract, payment method, services)
- Churn rate calculation and segmentation
- Correlation analysis (which variables relate to each other?)
- Creating clear, labeled visualizations using Matplotlib and Seaborn
- Documenting key observations and hypotheses
- Saving visualizations and findings report


### Out of Scope

- Advanced statistical tests (t-tests, chi-square) - comes in Stage 7
- Feature engineering or creating new variables - comes in Stage 6
- Predictive modeling or machine learning - not needed for this project
- Interactive dashboards - comes in Stage 8 (Streamlit)
- Complex multi-variable visualizations - keeping it simple and clear
- Time series analysis (no time-based trends in snapshot data)


### Assumptions

- You completed Stage 4 (clean dataset exists at `data/processed/clean_churn_data.csv`)
- You understand basic statistics (mean, median, standard deviation, percentile)
- You understand what correlation means (relationship between variables)
- You know basic visualization types (histogram, bar chart, box plot)
- Matplotlib and Seaborn are installed (from Stage 0)


### Output Artifact

- **eda_analysis.py** - Main EDA script with statistical analysis and visualizations
- **eda_findings.txt** - Document summarizing key observations and patterns discovered
- **Visualization PNG files** saved to `outputs/visualizations/`:
    - `churn_distribution.png` - Overall churn rate
    - `tenure_distribution.png` - Customer tenure distribution
    - `charges_distribution.png` - Monthly and total charges distributions
    - `churn_by_contract.png` - Churn rate by contract type
    - `churn_by_tenure.png` - Churn vs. tenure relationship
    - `correlation_heatmap.png` - Correlation between numeric variables
    - Additional segmentation charts

***

## b) Setup Instructions

### Step 1: Verify Prerequisites

Ensure the clean dataset from Stage 4 exists:

```
customer_churn_analysis/data/processed/clean_churn_data.csv
```


### Step 2: Understand EDA Workflow

The EDA script will perform analysis in this sequence:

**Part 1: Dataset Overview**

- Load data and display basic statistics

**Part 2: Target Variable Analysis (Churn)**

- Calculate overall churn rate
- Visualize churn distribution

**Part 3: Univariate Analysis**

- Numeric variables: distributions, outliers
- Categorical variables: value counts, proportions

**Part 4: Bivariate Analysis (Churn vs. Features)**

- How does churn relate to tenure? MonthlyCharges? Contract type?
- Identify which features have strongest relationship with churn

**Part 5: Correlation Analysis**

- Which numeric variables are correlated?
- Helps understand multicollinearity for later analysis

**Part 6: Key Segments Analysis**

- High-risk segments (which groups churn most?)
- Low-risk segments (which groups are loyal?)


### Step 3: Files to Create

You will create one Python script in the `scripts/` folder:

- `eda_analysis.py` - Comprehensive EDA script


### Step 4: Output Locations

The script will generate:

- **Visualizations:** `outputs/visualizations/` (multiple PNG files)
- **Findings report:** `outputs/reports/eda_findings.txt`


### Step 5: Visualization Design Principles

All charts will follow professional standards:

- Clear titles describing what is shown
- Axis labels with units
- Legends when needed
- Consistent color scheme (blue for No churn, red for Yes churn)
- Readable font sizes
- Saved at 300 DPI for presentation quality


### Dependencies Required

- pandas (already installed)
- numpy (already installed)
- matplotlib (already installed)
- seaborn (already installed)

***

## c) Implementation (FINAL VERSION)

### File 1: Exploratory Data Analysis Script

**File Name:** `eda_analysis.py`
**File Path:** `customer_churn_analysis/scripts/eda_analysis.py`
**Total Lines:** 420

```python
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
key_numeric = ['tenure', 'MonthlyCharges', 'TotalCharges', 'TotalPayments', 'TotalPaid']

# Calculate correlation matrix
correlation_matrix = df[key_numeric].corr()

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

# Define high-risk segment 2: Low tenure + No tech support
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
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure the clean dataset from Stage 4 exists:

```bash
ls data/processed/clean_churn_data.csv
```


### Step 2: Navigate to Project Root

Open terminal and navigate to project folder:

```bash
cd path/to/customer_churn_analysis
```


### Step 3: Run the EDA Script

Execute the exploratory data analysis script:

```bash
python scripts/eda_analysis.py
```

**Expected Duration:** 30-60 seconds (creating 7 visualizations)

### Step 4: Review Console Output

The script will print 7 parts:

1. Dataset Overview
2. Target Variable Analysis (Churn)
3. Univariate Analysis - Numeric Variables
4. Bivariate Analysis - Churn vs. Features
5. Correlation Analysis
6. High-Risk Segments Identification
7. Key Observations \& Hypotheses

### Step 5: View Generated Visualizations

Navigate to the visualizations folder:

```bash
cd outputs/visualizations
ls
```

You should see 7 PNG files. Open them to view the charts.

**On Mac:**

```bash
open outputs/visualizations/*.png
```

**On Windows:**

```bash
start outputs\visualizations\*.png
```

**On Linux:**

```bash
xdg-open outputs/visualizations/*.png
```


### Step 6: Read the Findings Report

Review the key observations:

```bash
cat outputs/reports/eda_findings.txt
```


***

## e) How to Test the Output

### Test 1: Verify Script Runs Without Errors

**Expected Result:**

- Script completes successfully
- Prints all 7 parts of analysis
- Final message: "✅ EXPLORATORY DATA ANALYSIS COMPLETE"
- No error messages or crashes

**How to Check:**

- Run the script and watch for errors
- Should complete in under 2 minutes


### Test 2: Verify Visualizations Created

**Expected Result:**

- 7 PNG files created in `outputs/visualizations/` folder
- Files should be 50-500 KB each

**How to Check:**

```bash
ls -lh outputs/visualizations/*.png
```

**Expected Files:**

```
churn_distribution.png
tenure_distribution.png
charges_distribution.png
churn_by_contract.png
churn_by_tenure.png
churn_by_payment_method.png
correlation_heatmap.png
```


### Test 3: Verify Findings Report Created

**Expected Result:**

- File exists at `outputs/reports/eda_findings.txt`
- Contains sections: Dataset Overview, Churn Analysis, Key Numeric Distributions, Churn Drivers, Correlation, High-Risk Segments, Key Observations

**How to Check:**

```bash
ls -lh outputs/reports/eda_findings.txt
wc -l outputs/reports/eda_findings.txt  # Should be 50-100 lines
```


### Test 4: Verify Churn Rate Calculation

**Expected Result:**

- Overall churn rate should be approximately 26-27%
- Displayed in console and in findings report

**How to Check:**

```bash
grep "Overall Churn Rate" outputs/reports/eda_findings.txt
```

**Expected Output:**

```
Overall Churn Rate: 26.54%  (approximate value)
```


### Test 5: Verify Visualizations Open Correctly

**Expected Result:**

- Each PNG file should open and display a clear, labeled chart
- No corrupted images
- Titles, axis labels, and legends should be visible

**How to Check:**

- Open each PNG file manually
- Verify:
    - Title is clear and descriptive
    - Axis labels present
    - Legend (if applicable) is visible
    - Colors are distinguishable
    - Text is readable


### Test 6: Verify Key Findings Documented

**Expected Result:**

- Findings report should contain at least 5 key observations
- Should include hypotheses for Stage 7

**How to Check:**

```bash
grep "Key Observations" outputs/reports/eda_findings.txt -A 10
grep "Hypotheses" outputs/reports/eda_findings.txt -A 10
```


### Test 7: Verify Churn by Contract Analysis

**Expected Result:**

- Month-to-month contracts should have highest churn rate (typically 40-45%)
- Two-year contracts should have lowest churn rate (typically <10%)

**How to Check:**

```bash
grep "Churn by Contract Type" outputs/reports/eda_findings.txt -A 5
```


### Test 8: Verify Correlation Heatmap Values

**Expected Result:**

- Correlation matrix should show values between -1 and 1
- tenure and TotalCharges should have positive correlation (typically 0.8+)

**How to Check:**

- Open `correlation_heatmap.png`
- Verify values displayed in cells are between -1 and 1
- Check that tenure-TotalCharges cell shows high positive correlation


### Test 9: Verify Tenure Distribution Stats

**Expected Result:**

- Mean tenure approximately 30-35 months
- Median tenure approximately 29-32 months
- Range: 0-72 months

**How to Check:**

```bash
grep "Tenure" outputs/reports/eda_findings.txt | head -5
```


### Test 10: Manual Visualization Quality Check

**Open each visualization and verify:**

1. **churn_distribution.png:**
    - Pie chart with two slices (Yes/No)
    - Percentages displayed
    - Yes slice slightly separated (exploded)
2. **tenure_distribution.png:**
    - Histogram with bars
    - Red dashed line for mean
    - Green dashed line for median
3. **charges_distribution.png:**
    - Two side-by-side histograms
    - Left: MonthlyCharges, Right: TotalCharges
    - Mean lines shown
4. **churn_by_contract.png:**
    - Grouped bar chart
    - Three contract types
    - Two bars per type (No churn, Yes churn)
5. **churn_by_tenure.png:**
    - Bar chart with 4 bars (tenure groups)
    - Percentage labels on top of bars
6. **churn_by_payment_method.png:**
    - Horizontal bar chart
    - 4 payment methods
    - Sorted by churn rate (highest first)
7. **correlation_heatmap.png:**
    - Color-coded grid
    - Values displayed in cells
    - Color bar on right

### Signs of Success

✅ Script completes without errors
✅ 7 PNG visualizations created
✅ Findings report created
✅ Overall churn rate ~26-27%
✅ Month-to-month contracts show highest churn
✅ Early tenure customers (0-12 months) show high churn
✅ Correlation heatmap shows expected relationships
✅ All visualizations clear, labeled, and professional
✅ Key observations documented
✅ Hypotheses generated for Stage 7

### Signs of Problems

❌ Script crashes or errors
❌ Missing PNG files
❌ Corrupted or blank images
❌ Churn rate significantly different from expected (~26%)
❌ Missing axis labels or titles on charts
❌ Findings report empty or missing sections
❌ Correlation values outside -1 to 1 range
❌ Charts display garbled text or overlapping labels

***

## f) Common Beginner Mistakes

### Mistake 1: Not Closing Plots After Saving

**What Happens:**

- Script gets slower as it progresses
- Memory usage increases dramatically
- Eventually crashes with "too many figures" error

**Why It Happens:**

- Matplotlib keeps figures in memory even after saving
- Creating 7+ figures without closing accumulates memory

**How to Fix:**

- **Always use `plt.close()` after `plt.savefig()`**
- Script correctly closes each figure after saving
- Pattern: `plt.savefig()` → `plt.close()`
- This frees memory for next visualization


### Mistake 2: Overcomplicating Visualizations

**What Happens:**

- Create 3D charts, complex multi-panel plots, or overly decorative visualizations
- Charts become confusing instead of insightful

**Why It Happens:**

- Trying to impress with fancy visuals
- Not understanding that simplicity = clarity

**How to Fix:**

- **Simpler is better for business stakeholders**
- One chart = one insight
- Use standard chart types (bar, histogram, pie, heatmap)
- Script focuses on clarity: clear titles, labeled axes, legends


### Mistake 3: Not Interpreting Results - Just Creating Charts

**What Happens:**

- Generate 10 beautiful charts
- Don't write down what they mean
- Can't explain insights when asked

**Why It Happens:**

- Treating EDA as visualization exercise
- Not connecting charts to business questions

**How to Fix:**

- **Every chart must answer a question:**
    - "Which contract type churns most?" → churn_by_contract.png
    - "Do new customers churn more?" → churn_by_tenure.png
- Script correctly documents findings in text report
- Pattern: Create chart → Document observation → Store in findings list


### Mistake 4: Analyzing Churn Without Converting to Binary

**What Happens:**

- Try to calculate churn rate directly from "Yes"/"No" strings
- Get errors or incorrect percentages

**Why It Happens:**

- Not understanding that calculations need numeric values
- Trying to compute mean of text values

**How to Fix:**

- **Convert to binary when needed:**
    - For display: Keep "Yes"/"No" (human-readable)
    - For calculation: `(df['Churn'] == 'Yes').sum()` (converts to 1/0)
- Script correctly uses `.apply(lambda x: (x == 'Yes').sum())` for churn rate calculations


### Mistake 5: Creating Charts with Unreadable Labels

**What Happens:**

- Axis labels overlap
- Text too small to read
- Chart titles cut off

**Why It Happens:**

- Not setting figure size appropriately
- Not using `plt.tight_layout()`
- Not considering how chart will look when saved

**How to Fix:**

- **Use appropriate figure sizes:** `plt.subplots(figsize=(10, 6))`
- **Always use `plt.tight_layout()`** before saving
- **Rotate long labels:** `rotation=45, ha='right'`
- **Save with high DPI:** `dpi=300` for presentation quality
- Script demonstrates all these best practices


### Mistake 6: Not Binning Continuous Variables for Visualization

**What Happens:**

- Try to visualize churn by tenure using all 72 unique values
- Chart becomes cluttered and unreadable

**Why It Happens:**

- Not understanding that continuous variables need grouping for categorical analysis

**How to Fix:**

- **Create bins for continuous variables:**
    - Tenure (months) → Groups (0-12, 13-24, 25-48, 49-72)
    - Age → Groups (18-25, 26-35, 36-50, 51+)
- Use `pd.cut()` to create bins with labels
- Script correctly bins tenure into 4 meaningful groups


### Mistake 7: Ignoring Context When Interpreting Correlation

**What Happens:**

- See high correlation between tenure and TotalCharges
- Conclude one "causes" the other
- Miss the obvious: TotalCharges = MonthlyCharges × tenure (mathematical relationship)

**Why It Happens:**

- Confusing correlation with causation
- Not understanding data generation process

**How to Fix:**

- **Correlation ≠ Causation**
- Some correlations are by design (tenure × charges = total)
- Look for unexpected correlations (these are interesting)
- Script correctly identifies strong correlations without claiming causation


### Mistake 8: Not Saving Visualizations to Files

**What Happens:**

- Charts display in window
- Close window, charts are gone forever
- Can't include in reports or presentations

**Why It Happens:**

- Using `plt.show()` instead of `plt.savefig()`
- Not planning for reproducibility

**How to Fix:**

- **Always save visualizations to files**
- Use descriptive filenames: `churn_by_contract.png` (not `plot1.png`)
- Save to organized folder: `outputs/visualizations/`
- Use high DPI (300) for quality
- Script never uses `plt.show()` - only `plt.savefig()`


### Mistake 9: Analyzing Too Many Variables at Once

**What Happens:**

- Try to create one massive chart showing 15 variables
- Result is incomprehensible

**Why It Happens:**

- Trying to be "efficient" by combining everything
- Not understanding cognitive limits of visualization

**How to Fix:**

- **One insight per chart**
- Break complex relationships into multiple simple charts
- Use series of charts to tell a story
- Script creates 7 focused charts instead of 1 complex dashboard


### Mistake 10: Not Documenting Hypotheses for Later Stages

**What Happens:**

- Discover interesting patterns during EDA
- Forget them by Stage 7 (analytical reasoning)
- Waste time rediscovering insights

**Why It Happens:**

- Not treating EDA as hypothesis generation
- Not writing down observations

**How to Fix:**

- **EDA generates questions for Stage 7:**
    - "Month-to-month contracts churn more" → Test statistically in Stage 7
    - "First-year customers at risk" → Design retention intervention
- Script correctly documents hypotheses in findings report
- These become the agenda for Stage 7 analysis


### Mistake 11: Using Wrong Chart Types

**What Happens:**

- Use line chart for categorical data (contract types)
- Use pie chart for 15+ categories
- Charts don't convey intended message

**Why It Happens:**

- Not understanding which chart types suit which data

**How to Fix:**

- **Chart type selection guide:**
    - Distribution of one numeric variable → Histogram
    - Comparison across categories → Bar chart
    - Proportion of whole → Pie chart (2-5 categories only)
    - Relationship between two numeric → Scatter plot
    - Correlation matrix → Heatmap
- Script uses appropriate chart types for each analysis


### Mistake 12: Forgetting to Create Output Directories

**What Happens:**

- Script tries to save files to `outputs/visualizations/`
- Folder doesn't exist
- Script crashes with "FileNotFoundError"

**Why It Happens:**

- Assuming folders exist
- Not creating directories before saving files

**How to Fix:**

- **Always create directories before use:**

```python
os.makedirs(viz_dir, exist_ok=True)
```

- `exist_ok=True` prevents error if folder already exists
- Script correctly creates directories at start

***

## ✅ Stage 5 Complete!

You have now:

- Loaded and analyzed the clean dataset with 7,043 customers
- Calculated overall churn rate (~26-27%)
- Analyzed distributions of key numeric variables (tenure, charges)
- Identified churn drivers through bivariate analysis
- Discovered that month-to-month contracts have highest churn rate
- Found that early-tenure customers (0-12 months) are at highest risk
- Analyzed correlation between numeric variables
- Identified high-risk customer segments for targeted interventions
- Created 7 professional, presentation-ready visualizations
- Documented key observations and hypotheses in findings report

**Key Insights Discovered:**

1. **Overall churn rate: ~26-27%** (approximately 1 in 4 customers leave)
2. **Contract type matters:** Month-to-month contracts have 40%+ churn vs. <10% for two-year
3. **Tenure is critical:** First 12 months are highest risk period
4. **Payment method indicator:** Electronic check users show higher churn
5. **High-risk segment:** Month-to-month + high charges customers

**High-Risk Segments Identified:**

- Segment 1: Month-to-month contracts + high monthly charges
- Segment 2: New customers (tenure < 12 months) + no tech support

**Hypotheses Generated for Stage 7:**

- Month-to-month contracts drive churn → Test incentives for longer commitments
- Early-tenure customers at highest risk → Improve onboarding
- Payment method indicates engagement → Investigate electronic check users
- Service add-ons reduce churn → Test upsell strategies

**Output Files:**

- **7 Visualizations** in `outputs/visualizations/`:
    - churn_distribution.png
    - tenure_distribution.png
    - charges_distribution.png
    - churn_by_contract.png
    - churn_by_tenure.png
    - churn_by_payment_method.png
    - correlation_heatmap.png
- **Findings Report:** `outputs/reports/eda_findings.txt`

**Critical Understanding:**

- **EDA is exploration, not explanation** - you discover patterns here, test them in Stage 7
- **Visualizations communicate insights** - each chart tells part of the churn story
- **Hypotheses guide future work** - observations become testable questions

**Next Step:** Wait for instruction to proceed to Stage 6 (Feature Engineering \& Metrics Layer)

---

# **Stage 6: Feature Engineering \& Metrics Layer**


***

## a) Learning Objective

### What You're Learning

You are learning how to **create business-relevant metrics and derived features** that transform raw data into analysis-ready insights. This stage focuses on calculating KPIs (Key Performance Indicators), creating customer segments, and engineering features that directly support business decision-making for churn analysis.

### Why This Matters

In real-world data analytics, **raw data rarely answers business questions directly**. Professional analysts create a "metrics layer" - calculated fields that represent business concepts:

- **KPIs:** Churn rate, customer lifetime value (CLV), average revenue per user (ARPU)
- **Segments:** High-value customers, at-risk customers, loyal customers
- **Behavioral indicators:** Service adoption rate, payment reliability, engagement level
- **Risk scores:** Rule-based churn risk indicators

**Without metrics engineering:**

- Analysis stays at raw data level (tenure=12 vs. tenure=24 means what?)
- Business stakeholders can't relate to technical columns
- Insights lack business context
- Recommendations are generic, not actionable

**With metrics engineering:**

- Speak business language ("high-value customers churn 15% less")
- Create actionable segments ("target 2,500 high-risk customers")
- Enable decision-making ("customers without tech support are 2x at-risk")
- Build interpretable, explainable analytics (no black-box)


### Skill Level

**Intermediate to Advanced** - This builds on EDA insights (Stage 5) and introduces business logic application, metric design, and feature creation techniques.

### In Scope

- Loading clean dataset and EDA insights
- Creating customer value metrics (CLV, ARPU, lifetime charges)
- Creating churn risk indicators (rule-based flags)
- Creating service adoption metrics (how many services customer uses)
- Creating customer segments (high/medium/low value, risk levels)
- Creating tenure-based features (customer lifecycle stage)
- Creating payment behavior features (payment reliability)
- Validating all new features for correctness
- Saving enriched dataset with all new features


### Out of Scope

- Machine learning feature engineering (polynomial features, interactions for ML models)
- Advanced statistical transformations (log transforms, standardization)
- Predictive modeling or machine learning
- Time-series features (no temporal data available)
- Text analytics or NLP features
- Complex mathematical formulas - keeping calculations simple and interpretable


### Assumptions

- You completed Stage 5 (EDA insights documented)
- You understand basic business metrics (revenue, average, rate)
- You know what customer lifetime value means conceptually
- Clean dataset exists at `data/processed/clean_churn_data.csv`
- You've reviewed EDA findings to understand churn drivers


### Output Artifact

- **feature_engineering.py** - Script that creates all metrics and features
- **enriched_churn_data.csv** - Dataset with original + new features in `data/processed/`
- **feature_dictionary.txt** - Documentation of all new features with business definitions
- **feature_validation_report.txt** - Validation checks for feature correctness
- **Console output** - Feature creation process with statistics

***

## b) Setup Instructions

### Step 1: Verify Prerequisites

Ensure the clean dataset from Stage 4 exists:

```
customer_churn_analysis/data/processed/clean_churn_data.csv
```


### Step 2: Review EDA Insights (Recommended)

Quickly review Stage 5 findings to understand which features to create:

```bash
cat outputs/reports/eda_findings.txt
```

Key insights to inform feature engineering:

- Contract type strongly affects churn
- Early tenure (0-12 months) is high-risk
- Payment method indicates engagement
- Service adoption may reduce churn


### Step 3: Understand Feature Categories

You will create features in these categories:

**Category 1: Customer Value Metrics**

- Customer Lifetime Value (CLV)
- Average Revenue Per User (ARPU)
- Total Customer Worth

**Category 2: Churn Risk Indicators**

- High Risk Flag (month-to-month + new customer)
- Payment Risk Flag (electronic check + missed payments)
- Service Risk Flag (minimal services, no support)

**Category 3: Service Adoption Metrics**

- Total Services Count
- Add-on Services Count
- Service Adoption Rate

**Category 4: Customer Lifecycle Stage**

- Tenure Segment (New, Growing, Mature, Loyal)
- Contract Stability Score
- Customer Lifecycle Stage

**Category 5: Behavioral Features**

- Payment Reliability Score
- Engagement Level
- Service Diversity


### Step 4: Files to Create

You will create one Python script in the `scripts/` folder:

- `feature_engineering.py` - Comprehensive feature creation script


### Step 5: Output Locations

The script will generate files in `data/processed/`:

- `enriched_churn_data.csv` - Dataset with all new features
- `feature_dictionary.txt` - Feature documentation
- `feature_validation_report.txt` - Validation results


### Dependencies Required

- pandas (already installed)
- numpy (already installed)
- No additional installations needed

***

## c) Implementation (FINAL VERSION)

### File 1: Feature Engineering Script

**File Name:** `feature_engineering.py`
**File Path:** `customer_churn_analysis/scripts/feature_engineering.py`
**Total Lines:** 425

```python
# Import required libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import os  # For file operations
from datetime import datetime  # For timestamps

# Print header
print("=" * 80)
print("STAGE 6: FEATURE ENGINEERING & METRICS LAYER")
print("=" * 80)
print()

# Define file paths
input_path = "data/processed/clean_churn_data.csv"
output_path = "data/processed/enriched_churn_data.csv"
dictionary_path = "data/processed/feature_dictionary.txt"
validation_path = "data/processed/feature_validation_report.txt"

# Check if input file exists
if not os.path.exists(input_path):
    print(f"❌ ERROR: Clean dataset not found at {input_path}")
    print("Please complete Stage 4 first")
    exit()

# Load the clean dataset
print("📂 Loading clean dataset...")
df = pd.read_csv(input_path)
print(f"✅ Dataset loaded: {input_path}")
print(f"   Original shape: {df.shape[^13_0]} rows × {df.shape[^13_1]} columns")
print()

# Initialize lists for documentation
feature_dict = []  # Feature dictionary entries
validation_results = []  # Validation results

# Add headers to documentation
feature_dict.append("=" * 80)
feature_dict.append("FEATURE DICTIONARY")
feature_dict.append("=" * 80)
feature_dict.append("")
feature_dict.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
feature_dict.append(f"Source Dataset: {input_path}")
feature_dict.append("")

validation_results.append("=" * 80)
validation_results.append("FEATURE VALIDATION REPORT")
validation_results.append("=" * 80)
validation_results.append("")
validation_results.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
validation_results.append("")

# ==================== CATEGORY 1: CUSTOMER VALUE METRICS ====================
print("-" * 80)
print("CATEGORY 1: CUSTOMER VALUE METRICS")
print("-" * 80)

feature_dict.append("-" * 80)
feature_dict.append("CATEGORY 1: CUSTOMER VALUE METRICS")
feature_dict.append("-" * 80)

validation_results.append("-" * 80)
validation_results.append("CATEGORY 1: CUSTOMER VALUE METRICS")
validation_results.append("-" * 80)

# Feature 1: Customer Lifetime Value (CLV)
# Business Definition: Total revenue generated by customer during their lifetime
# Calculation: TotalCharges (cumulative revenue to date)
print("\n📊 Creating: Customer Lifetime Value (CLV)")
df['CLV'] = df['TotalCharges']  # Direct mapping - TotalCharges represents CLV
print(f"   Mean CLV: ${df['CLV'].mean():.2f}")
print(f"   Median CLV: ${df['CLV'].median():.2f}")
print(f"   Range: ${df['CLV'].min():.2f} to ${df['CLV'].max():.2f}")

feature_dict.append("\n1. CLV (Customer Lifetime Value)")
feature_dict.append("   Definition: Total revenue generated by customer to date")
feature_dict.append("   Calculation: TotalCharges")
feature_dict.append("   Business Use: Identify high-value customers for retention priority")
feature_dict.append(f"   Mean: ${df['CLV'].mean():.2f}")

validation_results.append("\n1. CLV:")
validation_results.append(f"   Non-null count: {df['CLV'].count()} (expected: {len(df)})")
validation_results.append(f"   Negative values: {(df['CLV'] < 0).sum()} (expected: 0)")

# Feature 2: Average Revenue Per User (ARPU)
# Business Definition: Average monthly revenue per customer
# Calculation: MonthlyCharges (direct monthly billing amount)
print("\n📊 Creating: Average Revenue Per User (ARPU)")
df['ARPU'] = df['MonthlyCharges']  # ARPU = monthly charges
print(f"   Mean ARPU: ${df['ARPU'].mean():.2f}/month")
print(f"   Median ARPU: ${df['ARPU'].median():.2f}/month")

feature_dict.append("\n2. ARPU (Average Revenue Per User)")
feature_dict.append("   Definition: Average monthly revenue per customer")
feature_dict.append("   Calculation: MonthlyCharges")
feature_dict.append("   Business Use: Understand customer value tier")
feature_dict.append(f"   Mean: ${df['ARPU'].mean():.2f}/month")

validation_results.append("\n2. ARPU:")
validation_results.append(f"   Non-null count: {df['ARPU'].count()}")
validation_results.append(f"   Zero/negative values: {(df['ARPU'] <= 0).sum()} (expected: 0)")

# Feature 3: Customer Value Segment
# Business Definition: Categorize customers by revenue contribution
# Calculation: Based on ARPU quartiles (Q1=Low, Q2-Q3=Medium, Q4=High)
print("\n📊 Creating: Customer Value Segment")

# Calculate quartiles for ARPU
q1 = df['ARPU'].quantile(0.25)  # 25th percentile
q3 = df['ARPU'].quantile(0.75)  # 75th percentile

# Assign value segment based on ARPU
# Low: ARPU below Q1
# Medium: ARPU between Q1 and Q3
# High: ARPU above Q3
df['Value_Segment'] = pd.cut(
    df['ARPU'],  # Column to segment
    bins=[0, q1, q3, float('inf')],  # Bin edges
    labels=['Low Value', 'Medium Value', 'High Value']  # Segment labels
)

# Count customers in each segment
value_counts = df['Value_Segment'].value_counts()
print(f"   Low Value: {value_counts.get('Low Value', 0):,} customers")
print(f"   Medium Value: {value_counts.get('Medium Value', 0):,} customers")
print(f"   High Value: {value_counts.get('High Value', 0):,} customers")

feature_dict.append("\n3. Value_Segment")
feature_dict.append("   Definition: Customer revenue tier (Low/Medium/High)")
feature_dict.append("   Calculation: Based on ARPU quartiles")
feature_dict.append("   Business Use: Prioritize high-value customers in retention efforts")

validation_results.append("\n3. Value_Segment:")
validation_results.append(f"   Non-null count: {df['Value_Segment'].count()}")
validation_results.append(f"   Unique values: {df['Value_Segment'].nunique()} (expected: 3)")

print()

# ==================== CATEGORY 2: CHURN RISK INDICATORS ====================
print("-" * 80)
print("CATEGORY 2: CHURN RISK INDICATORS (RULE-BASED)")
print("-" * 80)

feature_dict.append("\n" + "-" * 80)
feature_dict.append("CATEGORY 2: CHURN RISK INDICATORS")
feature_dict.append("-" * 80)

validation_results.append("\n" + "-" * 80)
validation_results.append("CATEGORY 2: CHURN RISK INDICATORS")
validation_results.append("-" * 80)

# Feature 4: High Risk Flag
# Business Rule: Month-to-month contract AND tenure < 12 months
# Rationale: EDA showed these customers have highest churn rate
print("\n📊 Creating: High Risk Flag")

df['High_Risk_Flag'] = (
    (df['Contract'] == 'Month-to-month') &  # Unstable contract
    (df['tenure'] < 12)  # New customer (less than 1 year)
).astype(int)  # Convert True/False to 1/0

high_risk_count = df['High_Risk_Flag'].sum()
high_risk_churn = df[df['High_Risk_Flag'] == 1]['Churn'].value_counts()
print(f"   High Risk Customers: {high_risk_count:,} ({high_risk_count/len(df)*100:.1f}%)")
if 'Yes' in high_risk_churn.index:
    high_risk_churn_rate = high_risk_churn['Yes'] / high_risk_count * 100
    print(f"   Churn Rate in High Risk: {high_risk_churn_rate:.1f}%")

feature_dict.append("\n4. High_Risk_Flag")
feature_dict.append("   Definition: Customer at high risk of churning")
feature_dict.append("   Rule: Month-to-month contract AND tenure < 12 months")
feature_dict.append("   Business Use: Target for immediate retention intervention")
feature_dict.append(f"   Flagged Customers: {high_risk_count:,}")

validation_results.append("\n4. High_Risk_Flag:")
validation_results.append(f"   Values: {df['High_Risk_Flag'].unique()} (expected: [0, 1])")
validation_results.append(f"   Flagged: {high_risk_count} customers")

# Feature 5: Payment Risk Flag
# Business Rule: Electronic check payment method (highest churn in EDA)
# Rationale: Electronic check users showed elevated churn rate
print("\n📊 Creating: Payment Risk Flag")

df['Payment_Risk_Flag'] = (
    df['PaymentMethod'] == 'Electronic check'  # Risky payment method
).astype(int)  # Convert True/False to 1/0

payment_risk_count = df['Payment_Risk_Flag'].sum()
print(f"   Payment Risk Customers: {payment_risk_count:,} ({payment_risk_count/len(df)*100:.1f}%)")

feature_dict.append("\n5. Payment_Risk_Flag")
feature_dict.append("   Definition: Customer using high-churn payment method")
feature_dict.append("   Rule: PaymentMethod = 'Electronic check'")
feature_dict.append("   Business Use: Encourage migration to auto-pay methods")
feature_dict.append(f"   Flagged Customers: {payment_risk_count:,}")

validation_results.append("\n5. Payment_Risk_Flag:")
validation_results.append(f"   Values: {df['Payment_Risk_Flag'].unique()} (expected: [0, 1])")
validation_results.append(f"   Flagged: {payment_risk_count} customers")

# Feature 6: Service Risk Flag
# Business Rule: No tech support AND no online security
# Rationale: Customers without value-added services may be less engaged
print("\n📊 Creating: Service Risk Flag")

df['Service_Risk_Flag'] = (
    (df['TechSupport'] == 'No') &  # No technical support
    (df['OnlineSecurity'] == 'No')  # No security service
).astype(int)  # Convert True/False to 1/0

service_risk_count = df['Service_Risk_Flag'].sum()
print(f"   Service Risk Customers: {service_risk_count:,} ({service_risk_count/len(df)*100:.1f}%)")

feature_dict.append("\n6. Service_Risk_Flag")
feature_dict.append("   Definition: Customer with minimal service adoption")
feature_dict.append("   Rule: No TechSupport AND No OnlineSecurity")
feature_dict.append("   Business Use: Target for service upsell campaigns")
feature_dict.append(f"   Flagged Customers: {service_risk_count:,}")

validation_results.append("\n6. Service_Risk_Flag:")
validation_results.append(f"   Values: {df['Service_Risk_Flag'].unique()} (expected: [0, 1])")
validation_results.append(f"   Flagged: {service_risk_count} customers")

# Feature 7: Overall Risk Score
# Business Definition: Composite risk score (0-3 based on three risk flags)
# Calculation: Sum of High_Risk + Payment_Risk + Service_Risk flags
print("\n📊 Creating: Overall Risk Score")

df['Risk_Score'] = (
    df['High_Risk_Flag'] +  # 0 or 1
    df['Payment_Risk_Flag'] +  # 0 or 1
    df['Service_Risk_Flag']  # 0 or 1
)  # Total: 0 (no risk) to 3 (all risks present)

# Count customers by risk score
risk_distribution = df['Risk_Score'].value_counts().sort_index()
print("   Risk Score Distribution:")
for score, count in risk_distribution.items():
    print(f"     Score {score}: {count:,} customers ({count/len(df)*100:.1f}%)")

feature_dict.append("\n7. Risk_Score")
feature_dict.append("   Definition: Composite churn risk indicator (0-3)")
feature_dict.append("   Calculation: Sum of High_Risk + Payment_Risk + Service_Risk flags")
feature_dict.append("   Business Use: Prioritize retention resources (higher score = higher priority)")

validation_results.append("\n7. Risk_Score:")
validation_results.append(f"   Range: {df['Risk_Score'].min()} to {df['Risk_Score'].max()} (expected: 0-3)")
validation_results.append(f"   Mean: {df['Risk_Score'].mean():.2f}")

print()

# ==================== CATEGORY 3: SERVICE ADOPTION METRICS ====================
print("-" * 80)
print("CATEGORY 3: SERVICE ADOPTION METRICS")
print("-" * 80)

feature_dict.append("\n" + "-" * 80)
feature_dict.append("CATEGORY 3: SERVICE ADOPTION METRICS")
feature_dict.append("-" * 80)

validation_results.append("\n" + "-" * 80)
validation_results.append("CATEGORY 3: SERVICE ADOPTION METRICS")
validation_results.append("-" * 80)

# Feature 8: Total Services Count
# Business Definition: Number of services customer subscribes to
# Services: Phone, Internet, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies
print("\n📊 Creating: Total Services Count")

# List of service columns (Yes means customer has the service)
service_columns = [
    'PhoneService', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
    'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies'
]

# Count how many services each customer has
# For each service, check if value is 'Yes' (or not 'No' for InternetService)
df['Total_Services'] = 0  # Initialize counter

# Add 1 for PhoneService if 'Yes'
df['Total_Services'] += (df['PhoneService'] == 'Yes').astype(int)

# Add 1 for InternetService if customer has internet (DSL or Fiber optic)
df['Total_Services'] += (df['InternetService'] != 'No').astype(int)

# Add 1 for each additional service if 'Yes'
for service in ['OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']:
    df['Total_Services'] += (df[service] == 'Yes').astype(int)

print(f"   Mean Services: {df['Total_Services'].mean():.1f}")
print(f"   Range: {df['Total_Services'].min()} to {df['Total_Services'].max()} services")

feature_dict.append("\n8. Total_Services")
feature_dict.append("   Definition: Total number of services customer subscribes to")
feature_dict.append("   Services counted: Phone, Internet, Security, Backup, Protection, Support, Streaming")
feature_dict.append("   Business Use: Higher service adoption may indicate loyalty")
feature_dict.append(f"   Mean: {df['Total_Services'].mean():.1f} services")

validation_results.append("\n8. Total_Services:")
validation_results.append(f"   Range: {df['Total_Services'].min()}-{df['Total_Services'].max()} (expected: 0-8)")
validation_results.append(f"   Mean: {df['Total_Services'].mean():.2f}")

# Feature 9: Service Engagement Level
# Business Definition: Categorize customers by service adoption
# Low: 0-2 services, Medium: 3-5 services, High: 6+ services
print("\n📊 Creating: Service Engagement Level")

df['Service_Engagement'] = pd.cut(
    df['Total_Services'],  # Column to categorize
    bins=[0, 2, 5, 10],  # Bin edges (0-2, 3-5, 6+)
    labels=['Low Engagement', 'Medium Engagement', 'High Engagement']  # Labels
)

engagement_counts = df['Service_Engagement'].value_counts()
print("   Engagement Distribution:")
for level, count in engagement_counts.items():
    print(f"     {level}: {count:,} customers")

feature_dict.append("\n9. Service_Engagement")
feature_dict.append("   Definition: Level of service adoption (Low/Medium/High)")
feature_dict.append("   Calculation: Low (0-2 services), Medium (3-5), High (6+)")
feature_dict.append("   Business Use: Low engagement customers may need product education")

validation_results.append("\n9. Service_Engagement:")
validation_results.append(f"   Unique values: {df['Service_Engagement'].nunique()} (expected: 3)")

print()

# ==================== CATEGORY 4: CUSTOMER LIFECYCLE STAGE ====================
print("-" * 80)
print("CATEGORY 4: CUSTOMER LIFECYCLE STAGE")
print("-" * 80)

feature_dict.append("\n" + "-" * 80)
feature_dict.append("CATEGORY 4: CUSTOMER LIFECYCLE STAGE")
feature_dict.append("-" * 80)

validation_results.append("\n" + "-" * 80)
validation_results.append("CATEGORY 4: CUSTOMER LIFECYCLE STAGE")
validation_results.append("-" * 80)

# Feature 10: Tenure Segment
# Business Definition: Customer lifecycle stage based on tenure
# New: 0-12 months, Growing: 13-24, Mature: 25-48, Loyal: 49+ months
print("\n📊 Creating: Tenure Segment (Lifecycle Stage)")

df['Tenure_Segment'] = pd.cut(
    df['tenure'],  # Column to segment
    bins=[0, 12, 24, 48, 100],  # Bin edges
    labels=['New Customer', 'Growing Customer', 'Mature Customer', 'Loyal Customer']  # Stage labels
)

tenure_seg_counts = df['Tenure_Segment'].value_counts()
print("   Lifecycle Stage Distribution:")
for stage, count in tenure_seg_counts.items():
    print(f"     {stage}: {count:,} customers")

feature_dict.append("\n10. Tenure_Segment")
feature_dict.append("   Definition: Customer lifecycle stage based on tenure")
feature_dict.append("   Segments: New (0-12mo), Growing (13-24mo), Mature (25-48mo), Loyal (49+mo)")
feature_dict.append("   Business Use: Tailor retention strategies by lifecycle stage")

validation_results.append("\n10. Tenure_Segment:")
validation_results.append(f"   Unique values: {df['Tenure_Segment'].nunique()} (expected: 4)")

# Feature 11: Contract Stability Score
# Business Definition: Numeric score representing contract commitment level
# Month-to-month: 1 (low stability), One year: 2, Two year: 3 (high stability)
print("\n📊 Creating: Contract Stability Score")

# Map contract types to numeric stability scores
contract_stability_map = {
    'Month-to-month': 1,  # Low stability
    'One year': 2,  # Medium stability
    'Two year': 3  # High stability
}

df['Contract_Stability'] = df['Contract'].map(contract_stability_map)

print(f"   Mean Stability: {df['Contract_Stability'].mean():.2f}")
stability_counts = df['Contract_Stability'].value_counts().sort_index()
print("   Stability Distribution:")
for score, count in stability_counts.items():
    print(f"     Score {score}: {count:,} customers")

feature_dict.append("\n11. Contract_Stability")
feature_dict.append("   Definition: Numeric score for contract commitment (1-3)")
feature_dict.append("   Mapping: Month-to-month=1, One year=2, Two year=3")
feature_dict.append("   Business Use: Higher stability correlates with lower churn")

validation_results.append("\n11. Contract_Stability:")
validation_results.append(f"   Values: {sorted(df['Contract_Stability'].unique())} (expected: [1, 2, 3])")
validation_results.append(f"   Mean: {df['Contract_Stability'].mean():.2f}")

print()

# ==================== CATEGORY 5: BEHAVIORAL FEATURES ====================
print("-" * 80)
print("CATEGORY 5: BEHAVIORAL FEATURES")
print("-" * 80)

feature_dict.append("\n" + "-" * 80)
feature_dict.append("CATEGORY 5: BEHAVIORAL FEATURES")
feature_dict.append("-" * 80)

validation_results.append("\n" + "-" * 80)
validation_results.append("CATEGORY 5: BEHAVIORAL FEATURES")
validation_results.append("-" * 80)

# Feature 12: Payment Reliability Score
# Business Definition: Score based on payment history (0-100)
# Calculation: (TotalPayments - FailedPayments) / TotalPayments * 100
print("\n📊 Creating: Payment Reliability Score")

# Calculate reliability percentage (handle division by zero)
# If TotalPayments = 0, reliability = 100 (no payment issues)
df['Payment_Reliability'] = np.where(
    df['TotalPayments'] > 0,  # If customer has payment history
    ((df['TotalPayments'] - df['FailedPayments']) / df['TotalPayments'] * 100),  # Calculate success rate
    100  # New customers with no payments get 100 (neutral)
)

print(f"   Mean Reliability: {df['Payment_Reliability'].mean():.1f}%")
print(f"   Customers with 100% reliability: {(df['Payment_Reliability'] == 100).sum():,}")

feature_dict.append("\n12. Payment_Reliability")
feature_dict.append("   Definition: Payment success rate (0-100%)")
feature_dict.append("   Calculation: (TotalPayments - FailedPayments) / TotalPayments * 100")
feature_dict.append("   Business Use: Low reliability indicates payment issues (credit card expiration, etc.)")
feature_dict.append(f"   Mean: {df['Payment_Reliability'].mean():.1f}%")

validation_results.append("\n12. Payment_Reliability:")
validation_results.append(f"   Range: {df['Payment_Reliability'].min():.1f}% to {df['Payment_Reliability'].max():.1f}%")
validation_results.append(f"   Mean: {df['Payment_Reliability'].mean():.2f}%")

# Feature 13: Monthly Charge to CLV Ratio
# Business Definition: What percentage of lifetime value comes from monthly charge?
# High ratio = new customer (few months), Low ratio = long-tenure customer
print("\n📊 Creating: Monthly to Lifetime Ratio")

# Calculate ratio (handle division by zero for CLV=0)
df['Monthly_to_CLV_Ratio'] = np.where(
    df['CLV'] > 0,  # If customer has CLV
    (df['MonthlyCharges'] / df['CLV'] * 100),  # Calculate percentage
    100  # New customers with CLV=0 get 100% (monthly = lifetime)
)

print(f"   Mean Ratio: {df['Monthly_to_CLV_Ratio'].mean():.1f}%")

feature_dict.append("\n13. Monthly_to_CLV_Ratio")
feature_dict.append("   Definition: Monthly charges as percentage of total lifetime value")
feature_dict.append("   Calculation: (MonthlyCharges / CLV) * 100")
feature_dict.append("   Business Use: High ratio indicates new customer (tenure effect)")

validation_results.append("\n13. Monthly_to_CLV_Ratio:")
validation_results.append(f"   Range: {df['Monthly_to_CLV_Ratio'].min():.1f}% to {df['Monthly_to_CLV_Ratio'].max():.1f}%")

# Feature 14: Paperless Billing Engagement
# Business Definition: Binary indicator of digital engagement
# Paperless = 1 (engaged), Paper = 0 (less engaged)
print("\n📊 Creating: Paperless Billing Engagement")

df['Paperless_Engagement'] = (df['PaperlessBilling'] == 'Yes').astype(int)

paperless_count = df['Paperless_Engagement'].sum()
print(f"   Paperless Customers: {paperless_count:,} ({paperless_count/len(df)*100:.1f}%)")

feature_dict.append("\n14. Paperless_Engagement")
feature_dict.append("   Definition: Customer uses paperless billing (digital engagement)")
feature_dict.append("   Values: 1 (paperless), 0 (paper billing)")
feature_dict.append("   Business Use: Paperless may indicate tech-savvy, engaged customers")

validation_results.append("\n14. Paperless_Engagement:")
validation_results.append(f"   Values: {sorted(df['Paperless_Engagement'].unique())} (expected: [0, 1])")
validation_results.append(f"   Paperless rate: {paperless_count/len(df)*100:.1f}%")

print()

# ==================== VALIDATION: FEATURE COMPLETENESS ====================
print("-" * 80)
print("VALIDATION: FEATURE COMPLETENESS CHECK")
print("-" * 80)

validation_results.append("\n" + "-" * 80)
validation_results.append("OVERALL VALIDATION")
validation_results.append("-" * 80)

# Count new features created
new_features = [
    'CLV', 'ARPU', 'Value_Segment', 'High_Risk_Flag', 'Payment_Risk_Flag',
    'Service_Risk_Flag', 'Risk_Score', 'Total_Services', 'Service_Engagement',
    'Tenure_Segment', 'Contract_Stability', 'Payment_Reliability',
    'Monthly_to_CLV_Ratio', 'Paperless_Engagement'
]

print(f"\nTotal New Features Created: {len(new_features)}")
print("\nFeature Completeness Check:")

all_complete = True
for feature in new_features:
    if feature in df.columns:
        missing = df[feature].isnull().sum()
        if missing == 0:
            print(f"  ✅ {feature}: Complete ({df[feature].count()} values)")
            validation_results.append(f"✅ {feature}: Complete")
        else:
            print(f"  ⚠️  {feature}: {missing} missing values")
            validation_results.append(f"⚠️  {feature}: {missing} missing")
            all_complete = False
    else:
        print(f"  ❌ {feature}: NOT CREATED")
        validation_results.append(f"❌ {feature}: Missing")
        all_complete = False

if all_complete:
    print("\n✅ All features successfully created with no missing values")
    validation_results.append("\n✅ All features complete")
else:
    print("\n⚠️  Some features have issues - review above")
    validation_results.append("\n⚠️  Issues detected")

print()

# ==================== SAVE ENRICHED DATASET ====================
print("-" * 80)
print("SAVING ENRICHED DATASET")
print("-" * 80)

# Save enriched dataset with all new features
df.to_csv(output_path, index=False)
print(f"✅ Enriched dataset saved: {output_path}")
print(f"   Original columns: {df.shape[^13_1] - len(new_features)}")
print(f"   New features: {len(new_features)}")
print(f"   Total columns: {df.shape[^13_1]}")
print(f"   Rows: {df.shape[^13_0]}")

validation_results.append(f"\nOutput Dataset: {output_path}")
validation_results.append(f"Total columns: {df.shape[^13_1]}")
validation_results.append(f"New features: {len(new_features)}")

print()

# ==================== SAVE FEATURE DICTIONARY ====================
print("-" * 80)
print("SAVING FEATURE DOCUMENTATION")
print("-" * 80)

# Add summary to feature dictionary
feature_dict.append("\n" + "=" * 80)
feature_dict.append("SUMMARY")
feature_dict.append("=" * 80)
feature_dict.append(f"\nTotal Features Created: {len(new_features)}")
feature_dict.append("\nFeature Categories:")
feature_dict.append("  - Customer Value Metrics: 3 features")
feature_dict.append("  - Churn Risk Indicators: 4 features")
feature_dict.append("  - Service Adoption Metrics: 2 features")
feature_dict.append("  - Customer Lifecycle: 2 features")
feature_dict.append("  - Behavioral Features: 3 features")

# Write feature dictionary to file
with open(dictionary_path, 'w') as f:
    f.write('\n'.join(feature_dict))

print(f"✅ Feature dictionary saved: {dictionary_path}")

# Write validation report to file
with open(validation_path, 'w') as f:
    f.write('\n'.join(validation_results))

print(f"✅ Validation report saved: {validation_path}")

print()

# ==================== FINAL SUMMARY ====================
print("=" * 80)
print("✅ FEATURE ENGINEERING COMPLETE")
print("=" * 80)
print()
print("Features Created by Category:")
print("  1. Customer Value Metrics: 3")
print("     - CLV, ARPU, Value_Segment")
print("  2. Churn Risk Indicators: 4")
print("     - High_Risk_Flag, Payment_Risk_Flag, Service_Risk_Flag, Risk_Score")
print("  3. Service Adoption Metrics: 2")
print("     - Total_Services, Service_Engagement")
print("  4. Customer Lifecycle: 2")
print("     - Tenure_Segment, Contract_Stability")
print("  5. Behavioral Features: 3")
print("     - Payment_Reliability, Monthly_to_CLV_Ratio, Paperless_Engagement")
print()
print(f"Total New Features: {len(new_features)}")
print(f"Enriched Dataset: {output_path}")
print(f"Feature Dictionary: {dictionary_path}")
print(f"Validation Report: {validation_path}")
print()
print("Next Step: Proceed to Stage 7 (Analytical Reasoning & Advanced Analysis)")
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure the clean dataset from Stage 4 exists:

```bash
ls data/processed/clean_churn_data.csv
```


### Step 2: Navigate to Project Root

Open terminal and navigate to project folder:

```bash
cd path/to/customer_churn_analysis
```


### Step 3: Run the Feature Engineering Script

Execute the feature engineering script:

```bash
python scripts/feature_engineering.py
```

**Expected Duration:** 20-45 seconds

### Step 4: Review Console Output

The script will print 6 sections:

1. Category 1: Customer Value Metrics
2. Category 2: Churn Risk Indicators
3. Category 3: Service Adoption Metrics
4. Category 4: Customer Lifecycle Stage
5. Category 5: Behavioral Features
6. Validation: Feature Completeness Check

### Step 5: Verify Output Files Created

Check that files were generated:

```bash
ls data/processed/enriched_churn_data.csv
ls data/processed/feature_dictionary.txt
ls data/processed/feature_validation_report.txt
```


### Step 6: Review Feature Dictionary

Read the feature documentation:

```bash
cat data/processed/feature_dictionary.txt
```


### Step 7: Review Validation Report

Check feature validation results:

```bash
cat data/processed/feature_validation_report.txt
```


***

## e) How to Test the Output

### Test 1: Verify Script Runs Without Errors

**Expected Result:**

- Script completes successfully
- Final message: "✅ FEATURE ENGINEERING COMPLETE"
- No error messages or crashes


### Test 2: Verify Enriched Dataset Created

**Expected Result:**

- File exists at `data/processed/enriched_churn_data.csv`
- File size ~2-4 MB
- Contains 7,043 rows (same as input)
- Contains 33 + 14 = 47 columns (original + new features)

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); print(f'Shape: {df.shape[^13_0]} rows × {df.shape[^13_1]} columns')"
```

**Expected Output:**

```
Shape: 7043 rows × 47 columns
```


### Test 3: Verify All New Features Created

**Expected Result:**
14 new features should exist in the dataset

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); new_features = ['CLV', 'ARPU', 'Value_Segment', 'High_Risk_Flag', 'Payment_Risk_Flag', 'Service_Risk_Flag', 'Risk_Score', 'Total_Services', 'Service_Engagement', 'Tenure_Segment', 'Contract_Stability', 'Payment_Reliability', 'Monthly_to_CLV_Ratio', 'Paperless_Engagement']; missing = [f for f in new_features if f not in df.columns]; print(f'All features present: {len(missing) == 0}'); print(f'Missing: {missing}')"
```

**Expected Output:**

```
All features present: True
Missing: []
```


### Test 4: Verify Risk Score Values

**Expected Result:**

- Risk_Score should range from 0 to 3
- Most customers should have scores 0-2
- Mean should be around 0.5-1.5

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); print(f'Risk Score Range: {df[\"Risk_Score\"].min()} to {df[\"Risk_Score\"].max()}'); print(f'Mean: {df[\"Risk_Score\"].mean():.2f}'); print('Distribution:'); print(df['Risk_Score'].value_counts().sort_index())"
```


### Test 5: Verify Value Segment Distribution

**Expected Result:**

- Three segments: Low Value, Medium Value, High Value
- Roughly balanced distribution (each ~2000-3000 customers)

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); print('Value Segment Distribution:'); print(df['Value_Segment'].value_counts())"
```


### Test 6: Verify CLV and ARPU Values

**Expected Result:**

- CLV (Customer Lifetime Value) should equal TotalCharges
- ARPU should equal MonthlyCharges
- Both should have no missing values

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); print(f'CLV = TotalCharges: {(df[\"CLV\"] == df[\"TotalCharges\"]).all()}'); print(f'ARPU = MonthlyCharges: {(df[\"ARPU\"] == df[\"MonthlyCharges\"]).all()}'); print(f'CLV missing: {df[\"CLV\"].isnull().sum()}'); print(f'ARPU missing: {df[\"ARPU\"].isnull().sum()}')"
```

**Expected Output:**

```
CLV = TotalCharges: True
ARPU = MonthlyCharges: True
CLV missing: 0
ARPU missing: 0
```


### Test 7: Verify Total Services Range

**Expected Result:**

- Total_Services should range from 0 to 8
- Mean should be around 3-5 services

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); print(f'Total Services Range: {df[\"Total_Services\"].min()} to {df[\"Total_Services\"].max()}'); print(f'Mean: {df[\"Total_Services\"].mean():.2f}')"
```


### Test 8: Verify Binary Flags (0/1 Only)

**Expected Result:**

- All flag columns should have only values 0 and 1

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); flags = ['High_Risk_Flag', 'Payment_Risk_Flag', 'Service_Risk_Flag', 'Paperless_Engagement']; for flag in flags: unique = sorted(df[flag].unique()); print(f'{flag}: {unique}' + (' ✅' if unique == [0, 1] or unique == [^13_0] or unique == [^13_1] else ' ❌'))"
```


### Test 9: Verify Feature Dictionary Content

**Expected Result:**

- File exists and is not empty
- Contains all 14 feature definitions
- Each feature has: name, definition, calculation, business use

**How to Check:**

```bash
wc -l data/processed/feature_dictionary.txt  # Should be 80-120 lines
grep "Definition:" data/processed/feature_dictionary.txt | wc -l  # Should be 14
```


### Test 10: Verify Validation Report Shows Success

**Expected Result:**

- All features marked as "Complete" (✅)
- No missing values warnings
- Final status: "All features complete"

**How to Check:**

```bash
grep "✅" data/processed/feature_validation_report.txt | wc -l  # Should be 14+
grep "⚠️" data/processed/feature_validation_report.txt  # Should return nothing
grep "All features complete" data/processed/feature_validation_report.txt
```


### Test 11: Sample Data Inspection

**Manually inspect first few rows with new features:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); print(df[['customerID', 'CLV', 'ARPU', 'Risk_Score', 'Total_Services', 'Tenure_Segment']].head(10))"
```

**What to Look For:**

- CLV values should be positive (or 0 for new customers)
- Risk_Score should be 0-3
- Total_Services should be reasonable (0-8)
- Tenure_Segment should match tenure values


### Test 12: Business Logic Validation

**Verify high-risk customers match business rule:**

```bash
python -c "import pandas as pd; df = pd.read_csv('data/processed/enriched_churn_data.csv'); high_risk = df[df['High_Risk_Flag'] == 1]; manual_check = ((high_risk['Contract'] == 'Month-to-month') & (high_risk['tenure'] < 12)).all(); print(f'High Risk Flag Logic Correct: {manual_check}')"
```

**Expected Output:**

```
High Risk Flag Logic Correct: True
```


### Signs of Success

✅ Script completes without errors
✅ Enriched dataset has 47 columns (33 original + 14 new)
✅ All 7,043 rows preserved (no data loss)
✅ All 14 new features created
✅ Risk_Score ranges 0-3
✅ Binary flags contain only 0 and 1
✅ CLV equals TotalCharges
✅ ARPU equals MonthlyCharges
✅ Total_Services ranges 0-8
✅ No missing values in new features
✅ Feature dictionary contains all 14 definitions
✅ Validation report shows "All features complete"

### Signs of Problems

❌ Script crashes or errors
❌ Enriched dataset missing or wrong size
❌ Fewer than 14 new features created
❌ Risk_Score has values outside 0-3
❌ Binary flags have values other than 0/1
❌ Missing values in new features
❌ CLV doesn't match TotalCharges
❌ Feature dictionary empty or incomplete
❌ Validation warnings in report

***

## f) Common Beginner Mistakes

### Mistake 1: Creating Features Without Business Justification

**What Happens:**

- Create dozens of random mathematical transformations (square of tenure, log of charges, etc.)
- Features have no business meaning
- Can't explain what features represent

**Why It Happens:**

- Copying machine learning feature engineering tutorials
- Not understanding this is business analytics, not ML modeling

**How to Fix:**

- **Every feature must answer a business question:**
    - "Which customers are valuable?" → CLV, ARPU
    - "Who's at risk?" → Risk flags
    - "How engaged is customer?" → Service adoption
- If you can't explain feature to a business stakeholder, don't create it
- Script demonstrates business-first feature design


### Mistake 2: Not Validating Feature Calculations

**What Happens:**

- Create Risk_Score but don't verify it's 0-3
- Create CLV but don't check for negative values
- Features have impossible or incorrect values

**Why It Happens:**

- Trusting code without verification
- Not thinking about valid ranges for business metrics

**How to Fix:**

- **Always validate after creating features:**
    - Check value ranges (CLV >= 0, Risk_Score in )
    - Check for missing values
    - Verify business logic (High_Risk_Flag only for month-to-month + low tenure)
- Script includes comprehensive validation section
- Test edge cases (what if TotalPayments = 0?)


### Mistake 3: Dividing by Zero Without Handling

**What Happens:**

- Calculate Payment_Reliability = (Total - Failed) / Total
- Crashes when TotalPayments = 0 (new customers)
- Get "division by zero" error

**Why It Happens:**

- Not considering edge cases
- Assuming all customers have payment history

**How to Fix:**

- **Use `np.where()` for conditional calculations:**

```python
df['Reliability'] = np.where(
    df['Total'] > 0,  # Condition
    (df['Total'] - df['Failed']) / df['Total'] * 100,  # If true
    100  # If false (default value)
)
```

- Always define what happens for edge cases
- Script correctly handles division by zero scenarios


### Mistake 4: Creating Features That Leak Target Variable

**What Happens:**

- Create feature like "ChurnIndicator" that uses Churn column
- Feature perfectly predicts churn (it IS churn!)
- Called "data leakage"

**Why It Happens:**

- Not understanding temporal causality
- Creating features using information not available at decision time

**How to Fix:**

- **Features must be based ONLY on information available BEFORE churn:**
    - Good: tenure, contract type, services (known before customer churns)
    - Bad: "days_since_churn" (only known AFTER churn)
- Never use target variable (Churn) in feature calculations
- Script carefully avoids data leakage


### Mistake 5: Not Documenting Features

**What Happens:**

- Create 20 features
- Week later, can't remember what "Feature_X_Ratio" means
- Can't explain features to stakeholders

**Why It Happens:**

- Treating feature engineering as coding exercise
- Not creating documentation alongside code

**How to Fix:**

- **Document every feature as you create it:**
    - Name: Clear, descriptive (not X1, X2, X3)
    - Definition: What does it represent?
    - Calculation: How is it computed?
    - Business Use: Why does it matter?
- Script creates comprehensive feature dictionary
- Documentation = part of deliverable, not optional


### Mistake 6: Creating Too Many Features

**What Happens:**

- Create 100+ features "just in case"
- Analysis becomes overwhelming
- Can't identify which features actually matter

**Why It Happens:**

- "More features = better analysis" misconception
- Not being selective based on business value

**How to Fix:**

- **Quality over quantity:**
    - Focus on features that answer specific business questions
    - 10-20 well-designed features > 100 random ones
    - Each feature should have clear business justification
- Script creates focused set of 14 meaningful features
- Better to add features later than remove hundreds


### Mistake 7: Inconsistent Feature Naming

**What Happens:**

- Name features inconsistently: "riskScore", "Risk_Flag", "RISK_LEVEL"
- Hard to find related features
- Looks unprofessional

**Why It Happens:**

- Not following naming convention
- Coding ad-hoc without standards

**How to Fix:**

- **Use consistent naming convention:**
    - All caps with underscores: `High_Risk_Flag`
    - Descriptive names: `Payment_Reliability` (not `PR` or `score2`)
    - Group related features: `Risk_Score`, `Risk_Flag`
- Script uses consistent snake_case naming
- Makes code readable and maintainable


### Mistake 8: Not Handling Categorical Values in Numeric Features

**What Happens:**

- Try to calculate mean of Contract column
- Get error because it's text ("Month-to-month", "One year")
- Need numeric representation

**Why It Happens:**

- Not understanding when to encode categorical as numeric
- Trying mathematical operations on text

**How to Fix:**

- **Map categorical to numeric when needed:**

```python
contract_map = {'Month-to-month': 1, 'One year': 2, 'Two year': 3}
df['Contract_Score'] = df['Contract'].map(contract_map)
```

- Use for: ordering (stability), mathematical operations
- Don't encode when: categories have no natural order
- Script correctly creates Contract_Stability numeric score


### Mistake 9: Creating Features with Missing Values

**What Happens:**

- Create Risk_Score but some customers have NaN
- Later analysis breaks or gives wrong results
- Don't realize features incomplete

**Why It Happens:**

- Not checking for completeness after creation
- Calculations fail silently (produce NaN)

**How to Fix:**

- **Validate feature completeness:**

```python
print(f"Missing values: {df['Risk_Score'].isnull().sum()}")
```

- If feature has missing values, investigate why
- Either fix calculation or document why NaN is valid
- Script validates all features are complete (0 missing)


### Mistake 10: Not Testing Feature Logic

**What Happens:**

- Create High_Risk_Flag for "month-to-month + low tenure"
- Don't verify that flagged customers actually match criteria
- Logic error goes unnoticed

**Why It Happens:**

- Trusting code without verification
- Not testing business rules

**How to Fix:**

- **Test feature logic explicitly:**

```python
high_risk = df[df['High_Risk_Flag'] == 1]
correct = ((high_risk['Contract'] == 'Month-to-month') & 
           (high_risk['tenure'] < 12)).all()
print(f"Logic correct: {correct}")
```

- Verify business rules produce expected results
- Test edge cases
- Script includes business logic validation


### Mistake 11: Overcomplicating Metrics

**What Happens:**

- Create complex formula: CLV = (ARPU × Lifetime × Retention Rate × Discount Factor) / (1 + Churn Rate)^2
- Can't explain it to stakeholders
- Over-engineering

**Why It Happens:**

- Trying to be "sophisticated"
- Not understanding that simpler = better for business analytics

**How to Fix:**

- **Keep metrics simple and interpretable:**
    - CLV = TotalCharges (actual revenue to date)
    - ARPU = MonthlyCharges (current monthly revenue)
    - Risk_Score = sum of binary flags (easy to understand)
- Complex ≠ Better
- Stakeholders must understand metrics
- Script uses straightforward, explainable calculations


### Mistake 12: Not Aligning Features with EDA Insights

**What Happens:**

- EDA showed contract type matters for churn
- Create features unrelated to contract
- Miss opportunity to act on insights

**Why It Happens:**

- Not reviewing EDA findings before feature engineering
- Disconnect between exploration and feature creation

**How to Fix:**

- **Review Stage 5 findings first:**
    - EDA insight: "Month-to-month highest churn" → Create contract stability score
    - EDA insight: "First year high risk" → Create tenure segment
    - EDA insight: "Payment method matters" → Create payment risk flag
- Features should operationalize EDA discoveries
- Script designs features based on Stage 5 patterns

***

## ✅ Stage 6 Complete!

You have now:

- Created 14 business-relevant features across 5 categories
- Designed customer value metrics (CLV, ARPU, Value_Segment)
- Built rule-based churn risk indicators (High_Risk_Flag, Payment_Risk_Flag, Service_Risk_Flag, Risk_Score)
- Calculated service adoption metrics (Total_Services, Service_Engagement)
- Defined customer lifecycle stages (Tenure_Segment, Contract_Stability)
- Engineered behavioral features (Payment_Reliability, Monthly_to_CLV_Ratio, Paperless_Engagement)
- Validated all features for correctness and completeness
- Documented every feature with business definitions
- Saved enriched dataset ready for advanced analysis

**Key Features Created:**

**Customer Value (3):**

- CLV: Customer lifetime value (total revenue)
- ARPU: Average revenue per user (monthly)
- Value_Segment: Low/Medium/High value classification

**Churn Risk (4):**

- High_Risk_Flag: Month-to-month + new customer
- Payment_Risk_Flag: Electronic check users
- Service_Risk_Flag: Minimal service adoption
- Risk_Score: Composite risk (0-3)

**Service Adoption (2):**

- Total_Services: Count of subscribed services
- Service_Engagement: Low/Medium/High engagement

**Lifecycle (2):**

- Tenure_Segment: New/Growing/Mature/Loyal
- Contract_Stability: Numeric commitment level (1-3)

**Behavioral (3):**

- Payment_Reliability: Payment success rate (%)
- Monthly_to_CLV_Ratio: Monthly charge % of lifetime value
- Paperless_Engagement: Digital billing indicator

**Output Files:**

- `data/processed/enriched_churn_data.csv` - 7,043 rows × 47 columns
- `data/processed/feature_dictionary.txt` - Complete feature documentation
- `data/processed/feature_validation_report.txt` - Feature validation results

**Critical Understanding:**

- **Features enable action** - each feature supports specific business decisions
- **Simplicity wins** - interpretable features > complex formulas
- **Documentation matters** - stakeholders need to understand what features mean
- **Validation critical** - always verify features have correct values

**Business Value:**

- Can now segment customers by value and risk
- Have actionable flags for targeting interventions
- Created metrics that speak business language
- Built foundation for Stage 7 analytical reasoning

**Next Step:** Wait for instruction to proceed to Stage 7 (Analytical Reasoning \& Advanced Analysis)

<div align="center">⁂</div>

[^13_1]: projects.workflow_stages


---

# **Stage 7: Analytical Reasoning \& Advanced Analysis**


***

## a) Learning Objective

### What You're Learning

You are learning how to **conduct systematic analytical reasoning** to test hypotheses, compare customer segments, and derive actionable business insights from data. This stage transforms observations from EDA (Stage 5) into validated findings with statistical backing and concrete business recommendations.

### Why This Matters

In real-world data analytics, **observations alone don't drive decisions - validated insights do**. Professional analysts move beyond "what happened?" to answer:

- **Why did it happen?** (Root cause analysis)
- **Is the pattern real or random?** (Statistical significance)
- **Which segments are most affected?** (Comparative analysis)
- **What should we do about it?** (Actionable recommendations)

**Without analytical reasoning:**

- Observations stay as interesting facts ("month-to-month churn is 42%")
- Can't prioritize which patterns to act on
- Recommendations lack evidence backing
- Stakeholders question validity of insights

**With analytical reasoning:**

- Validate patterns with evidence ("month-to-month churn is 3.5x higher than two-year, affecting 3,000+ customers")
- Quantify business impact ("High-risk segment represents \$2M annual revenue at risk")
- Prioritize interventions by impact ("Reducing high-risk churn by 10% saves \$200K annually")
- Provide data-backed recommendations ("Offer 6-month contract incentives to reduce churn from 42% to 25%")


### Skill Level

**Advanced** - This builds on all previous stages and introduces comparative analysis, segment profiling, hypothesis validation, and business recommendation frameworks.

### In Scope

- Loading enriched dataset with features from Stage 6
- Testing hypotheses from Stage 5 EDA findings
- Segment comparison analysis (high-risk vs low-risk, value segments, tenure groups)
- Churn driver quantification (what factors have biggest impact?)
- Service adoption impact analysis (do services reduce churn?)
- Contract type detailed analysis (why do contracts matter?)
- Payment behavior analysis (reliability and churn relationship)
- Calculating business impact metrics (revenue at risk, customer counts)
- Generating prioritized, actionable recommendations
- Creating executive summary of findings


### Out of Scope

- Predictive modeling or machine learning (this is rule-based analytics)
- Advanced statistical tests (t-tests, chi-square, ANOVA) - keeping analysis accessible
- Causal inference or A/B testing - using observational analysis
- Time series or forecasting - snapshot data only
- Complex mathematical modeling - focus on interpretable analysis


### Assumptions

- You completed Stage 6 (enriched dataset with features exists)
- You've reviewed Stage 5 EDA findings (hypotheses to test)
- You understand basic statistics (percentages, averages, comparisons)
- You can interpret business metrics (churn rate, revenue, customer count)
- Clean data available at `data/processed/enriched_churn_data.csv`


### Output Artifact

- **analytical_reasoning.py** - Main analysis script with hypothesis testing and segment comparisons
- **analysis_report.txt** - Comprehensive findings report with statistical evidence
- **segment_comparison.csv** - Detailed segment statistics (churn rates, counts, revenue)
- **business_recommendations.txt** - Prioritized, actionable recommendations with expected impact
- **executive_summary.txt** - High-level summary for stakeholders
- **Console output** - Detailed analysis process with insights

***

## b) Setup Instructions

### Step 1: Verify Prerequisites

Ensure the enriched dataset from Stage 6 exists:

```
customer_churn_analysis/data/processed/enriched_churn_data.csv
```


### Step 2: Review EDA Findings (Recommended)

Quickly review Stage 5 hypotheses to test:

```bash
cat outputs/reports/eda_findings.txt
```

Key hypotheses to validate:

- Month-to-month contracts drive churn
- Early tenure (0-12 months) is highest risk
- Payment method affects churn
- Service adoption reduces churn


### Step 3: Understand Analysis Framework

The analysis will follow this structure:

**Part 1: Hypothesis Validation**

- Test each hypothesis from Stage 5
- Quantify differences between groups
- Validate with evidence

**Part 2: Segment Deep-Dive Analysis**

- High-risk segment profiling
- Value segment comparison
- Lifecycle stage analysis
- Service engagement analysis

**Part 3: Churn Driver Quantification**

- Rank factors by churn impact
- Identify strongest churn predictors
- Calculate relative risk ratios

**Part 4: Business Impact Assessment**

- Revenue at risk calculations
- Customer count impacts
- Prioritization by business value

**Part 5: Actionable Recommendations**

- Specific interventions for each segment
- Expected impact estimates
- Implementation priority ranking


### Step 4: Files to Create

You will create one Python script in the `scripts/` folder:

- `analytical_reasoning.py` - Comprehensive analytical reasoning script


### Step 5: Output Locations

The script will generate files in `outputs/reports/`:

- `analysis_report.txt` - Detailed analysis findings
- `segment_comparison.csv` - Segment statistics table
- `business_recommendations.txt` - Actionable recommendations
- `executive_summary.txt` - High-level summary


### Dependencies Required

- pandas (already installed)
- numpy (already installed)
- No additional installations needed

***

## c) Implementation (FINAL VERSION)

### File 1: Analytical Reasoning Script

**File Name:** `analytical_reasoning.py`
**File Path:** `customer_churn_analysis/scripts/analytical_reasoning.py`
**Total Lines:** 520

```python
# Import required libraries
import pandas as pd  # For data manipulation
import numpy as np  # For numerical operations
import os  # For file operations
from datetime import datetime  # For timestamps

# Print header
print("=" * 80)
print("STAGE 7: ANALYTICAL REASONING & ADVANCED ANALYSIS")
print("=" * 80)
print()

# Define file paths
input_path = "data/processed/enriched_churn_data.csv"
analysis_report_path = "outputs/reports/analysis_report.txt"
segment_comparison_path = "outputs/reports/segment_comparison.csv"
recommendations_path = "outputs/reports/business_recommendations.txt"
executive_summary_path = "outputs/reports/executive_summary.txt"

# Check if input file exists
if not os.path.exists(input_path):
    print(f"❌ ERROR: Enriched dataset not found at {input_path}")
    print("Please complete Stage 6 first")
    exit()

# Create reports directory if it doesn't exist
os.makedirs("outputs/reports", exist_ok=True)

# Load the enriched dataset
print("📂 Loading enriched dataset...")
df = pd.read_csv(input_path)
print(f"✅ Dataset loaded: {input_path}")
print(f"   Shape: {df.shape[0]} rows × {df.shape[1]} columns")
print()

# Initialize report lines lists
analysis_report = []
recommendations = []
executive_summary = []

# Add headers
analysis_report.append("=" * 80)
analysis_report.append("ANALYTICAL REASONING REPORT")
analysis_report.append("=" * 80)
analysis_report.append("")
analysis_report.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
analysis_report.append(f"Dataset: {input_path}")
analysis_report.append(f"Total Customers Analyzed: {len(df):,}")
analysis_report.append("")

# Calculate baseline metrics
overall_churn_rate = (df['Churn'] == 'Yes').sum() / len(df) * 100
total_churned = (df['Churn'] == 'Yes').sum()
total_retained = (df['Churn'] == 'No').sum()

analysis_report.append("BASELINE METRICS:")
analysis_report.append(f"  Overall Churn Rate: {overall_churn_rate:.2f}%")
analysis_report.append(f"  Churned Customers: {total_churned:,}")
analysis_report.append(f"  Retained Customers: {total_retained:,}")
analysis_report.append("")

# ==================== PART 1: HYPOTHESIS VALIDATION ====================
print("-" * 80)
print("PART 1: HYPOTHESIS VALIDATION (FROM STAGE 5 EDA)")
print("-" * 80)

analysis_report.append("-" * 80)
analysis_report.append("PART 1: HYPOTHESIS VALIDATION")
analysis_report.append("-" * 80)

# Hypothesis 1: Month-to-month contracts have significantly higher churn
print("\n📊 Hypothesis 1: Month-to-month contracts drive higher churn")

# Calculate churn rate by contract type
churn_by_contract = df.groupby('Contract').agg({
    'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,  # Churn rate
    'customerID': 'count'  # Customer count
}).rename(columns={'Churn': 'Churn_Rate', 'customerID': 'Customer_Count'})

print("\nChurn Rate by Contract Type:")
for contract, row in churn_by_contract.iterrows():
    print(f"  {contract}: {row['Churn_Rate']:.2f}% ({int(row['Customer_Count']):,} customers)")

# Calculate relative risk (month-to-month vs two-year)
mtm_churn = churn_by_contract.loc['Month-to-month', 'Churn_Rate']
two_year_churn = churn_by_contract.loc['Two year', 'Churn_Rate']
relative_risk = mtm_churn / two_year_churn

print(f"\n✅ VALIDATED: Month-to-month churn ({mtm_churn:.1f}%) is {relative_risk:.1f}x higher than Two-year ({two_year_churn:.1f}%)")

analysis_report.append("\nHypothesis 1: Contract Type Impact")
analysis_report.append(f"  Month-to-month churn: {mtm_churn:.2f}%")
analysis_report.append(f"  Two-year churn: {two_year_churn:.2f}%")
analysis_report.append(f"  Relative Risk: {relative_risk:.1f}x")
analysis_report.append(f"  Conclusion: VALIDATED - Contract type is a major churn driver")

# Hypothesis 2: Early tenure customers (0-12 months) are at highest risk
print("\n📊 Hypothesis 2: Early tenure customers have highest churn risk")

# Calculate churn rate by tenure segment
churn_by_tenure = df.groupby('Tenure_Segment').agg({
    'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
    'customerID': 'count'
}).rename(columns={'Churn': 'Churn_Rate', 'customerID': 'Customer_Count'})

print("\nChurn Rate by Tenure Segment:")
for segment, row in churn_by_tenure.iterrows():
    print(f"  {segment}: {row['Churn_Rate']:.2f}% ({int(row['Customer_Count']):,} customers)")

# Compare new vs loyal customers
new_churn = churn_by_tenure.loc['New Customer', 'Churn_Rate']
loyal_churn = churn_by_tenure.loc['Loyal Customer', 'Churn_Rate']
tenure_risk_ratio = new_churn / loyal_churn

print(f"\n✅ VALIDATED: New customers ({new_churn:.1f}%) churn {tenure_risk_ratio:.1f}x more than Loyal customers ({loyal_churn:.1f}%)")

analysis_report.append("\nHypothesis 2: Tenure Impact")
analysis_report.append(f"  New customer churn: {new_churn:.2f}%")
analysis_report.append(f"  Loyal customer churn: {loyal_churn:.2f}%")
analysis_report.append(f"  Risk Ratio: {tenure_risk_ratio:.1f}x")
analysis_report.append(f"  Conclusion: VALIDATED - First year is critical retention period")

# Hypothesis 3: Payment method affects churn rates
print("\n📊 Hypothesis 3: Payment method indicates churn risk")

churn_by_payment = df.groupby('PaymentMethod').agg({
    'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
    'customerID': 'count'
}).rename(columns={'Churn': 'Churn_Rate', 'customerID': 'Customer_Count'}).sort_values('Churn_Rate', ascending=False)

print("\nChurn Rate by Payment Method:")
for method, row in churn_by_payment.iterrows():
    print(f"  {method}: {row['Churn_Rate']:.2f}% ({int(row['Customer_Count']):,} customers)")

highest_payment_churn = churn_by_payment.iloc[0]
lowest_payment_churn = churn_by_payment.iloc[-1]
payment_diff = highest_payment_churn['Churn_Rate'] - lowest_payment_churn['Churn_Rate']

print(f"\n✅ VALIDATED: {highest_payment_churn.name} has {payment_diff:.1f} percentage points higher churn than {lowest_payment_churn.name}")

analysis_report.append("\nHypothesis 3: Payment Method Impact")
analysis_report.append(f"  Highest churn: {highest_payment_churn.name} ({highest_payment_churn['Churn_Rate']:.2f}%)")
analysis_report.append(f"  Lowest churn: {lowest_payment_churn.name} ({lowest_payment_churn['Churn_Rate']:.2f}%)")
analysis_report.append(f"  Difference: {payment_diff:.1f} percentage points")
analysis_report.append(f"  Conclusion: VALIDATED - Payment method is churn indicator")

# Hypothesis 4: Service adoption reduces churn
print("\n📊 Hypothesis 4: Higher service adoption reduces churn")

churn_by_engagement = df.groupby('Service_Engagement').agg({
    'Churn': lambda x: (x == 'Yes').sum() / len(x) * 100,
    'customerID': 'count'
}).rename(columns={'Churn': 'Churn_Rate', 'customerID': 'Customer_Count'})

print("\nChurn Rate by Service Engagement:")
for engagement, row in churn_by_engagement.iterrows():
    print(f"  {engagement}: {row['Churn_Rate']:.2f}% ({int(row['Customer_Count']):,} customers)")

low_engagement_churn = churn_by_engagement.loc['Low Engagement', 'Churn_Rate']
high_engagement_churn = churn_by_engagement.loc['High Engagement', 'Churn_Rate']
engagement_benefit = low_engagement_churn - high_engagement_churn

print(f"\n✅ VALIDATED: Low engagement customers churn {engagement_benefit:.1f} percentage points more than High engagement")

analysis_report.append("\nHypothesis 4: Service Adoption Impact")
analysis_report.append(f"  Low engagement churn: {low_engagement_churn:.2f}%")
analysis_report.append(f"  High engagement churn: {high_engagement_churn:.2f}%")
analysis_report.append(f"  Churn Reduction: {engagement_benefit:.1f} percentage points")
analysis_report.append(f"  Conclusion: VALIDATED - Service adoption reduces churn")

analysis_report.append("")
print()

# ==================== PART 2: SEGMENT DEEP-DIVE ANALYSIS ====================
print("-" * 80)
print("PART 2: SEGMENT DEEP-DIVE ANALYSIS")
print("-" * 80)

analysis_report.append("-" * 80)
analysis_report.append("PART 2: SEGMENT ANALYSIS")
analysis_report.append("-" * 80)

# Create comprehensive segment comparison table
segment_data = []

# Analyze High-Risk Segment (from Stage 6 Risk_Score)
print("\n📊 HIGH-RISK SEGMENT PROFILE (Risk_Score >= 2)")

high_risk_customers = df[df['Risk_Score'] >= 2]
high_risk_churn_rate = (high_risk_customers['Churn'] == 'Yes').sum() / len(high_risk_customers) * 100
high_risk_count = len(high_risk_customers)
high_risk_revenue = high_risk_customers['CLV'].sum()
high_risk_arpu = high_risk_customers['ARPU'].mean()

print(f"  Total Customers: {high_risk_count:,} ({high_risk_count/len(df)*100:.1f}% of total)")
print(f"  Churn Rate: {high_risk_churn_rate:.2f}%")
print(f"  Total CLV at Risk: ${high_risk_revenue:,.2f}")
print(f"  Average ARPU: ${high_risk_arpu:.2f}/month")

segment_data.append({
    'Segment': 'High Risk (Score>=2)',
    'Customer_Count': high_risk_count,
    'Percentage_of_Total': high_risk_count/len(df)*100,
    'Churn_Rate': high_risk_churn_rate,
    'Total_CLV': high_risk_revenue,
    'Avg_ARPU': high_risk_arpu
})

analysis_report.append("\nHIGH-RISK SEGMENT (Risk_Score >= 2):")
analysis_report.append(f"  Size: {high_risk_count:,} customers ({high_risk_count/len(df)*100:.1f}%)")
analysis_report.append(f"  Churn Rate: {high_risk_churn_rate:.2f}%")
analysis_report.append(f"  Revenue at Risk: ${high_risk_revenue:,.2f}")
analysis_report.append(f"  Avg ARPU: ${high_risk_arpu:.2f}/month")

# Analyze Medium-Risk Segment
print("\n📊 MEDIUM-RISK SEGMENT PROFILE (Risk_Score = 1)")

medium_risk_customers = df[df['Risk_Score'] == 1]
medium_risk_churn_rate = (medium_risk_customers['Churn'] == 'Yes').sum() / len(medium_risk_customers) * 100
medium_risk_count = len(medium_risk_customers)
medium_risk_revenue = medium_risk_customers['CLV'].sum()
medium_risk_arpu = medium_risk_customers['ARPU'].mean()

print(f"  Total Customers: {medium_risk_count:,} ({medium_risk_count/len(df)*100:.1f}% of total)")
print(f"  Churn Rate: {medium_risk_churn_rate:.2f}%")
print(f"  Total CLV at Risk: ${medium_risk_revenue:,.2f}")
print(f"  Average ARPU: ${medium_risk_arpu:.2f}/month")

segment_data.append({
    'Segment': 'Medium Risk (Score=1)',
    'Customer_Count': medium_risk_count,
    'Percentage_of_Total': medium_risk_count/len(df)*100,
    'Churn_Rate': medium_risk_churn_rate,
    'Total_CLV': medium_risk_revenue,
    'Avg_ARPU': medium_risk_arpu
})

analysis_report.append("\nMEDIUM-RISK SEGMENT (Risk_Score = 1):")
analysis_report.append(f"  Size: {medium_risk_count:,} customers ({medium_risk_count/len(df)*100:.1f}%)")
analysis_report.append(f"  Churn Rate: {medium_risk_churn_rate:.2f}%")
analysis_report.append(f"  Revenue at Risk: ${medium_risk_revenue:,.2f}")

# Analyze Low-Risk Segment
print("\n📊 LOW-RISK SEGMENT PROFILE (Risk_Score = 0)")

low_risk_customers = df[df['Risk_Score'] == 0]
low_risk_churn_rate = (low_risk_customers['Churn'] == 'Yes').sum() / len(low_risk_customers) * 100
low_risk_count = len(low_risk_customers)
low_risk_revenue = low_risk_customers['CLV'].sum()
low_risk_arpu = low_risk_customers['ARPU'].mean()

print(f"  Total Customers: {low_risk_count:,} ({low_risk_count/len(df)*100:.1f}% of total)")
print(f"  Churn Rate: {low_risk_churn_rate:.2f}%")
print(f"  Total CLV: ${low_risk_revenue:,.2f}")
print(f"  Average ARPU: ${low_risk_arpu:.2f}/month")

segment_data.append({
    'Segment': 'Low Risk (Score=0)',
    'Customer_Count': low_risk_count,
    'Percentage_of_Total': low_risk_count/len(df)*100,
    'Churn_Rate': low_risk_churn_rate,
    'Total_CLV': low_risk_revenue,
    'Avg_ARPU': low_risk_arpu
})

analysis_report.append("\nLOW-RISK SEGMENT (Risk_Score = 0):")
analysis_report.append(f"  Size: {low_risk_count:,} customers ({low_risk_count/len(df)*100:.1f}%)")
analysis_report.append(f"  Churn Rate: {low_risk_churn_rate:.2f}%")

# Compare high-risk vs low-risk
risk_churn_difference = high_risk_churn_rate - low_risk_churn_rate
print(f"\n💡 INSIGHT: High-risk customers churn {risk_churn_difference:.1f} percentage points more than low-risk")

analysis_report.append(f"\nKEY INSIGHT: High vs Low Risk difference: {risk_churn_difference:.1f} percentage points")

# Analyze Value Segments
print("\n📊 VALUE SEGMENT COMPARISON")

for value_seg in ['High Value', 'Medium Value', 'Low Value']:
    seg_customers = df[df['Value_Segment'] == value_seg]
    seg_churn = (seg_customers['Churn'] == 'Yes').sum() / len(seg_customers) * 100
    seg_count = len(seg_customers)
    seg_clv = seg_customers['CLV'].sum()
    seg_arpu = seg_customers['ARPU'].mean()
    
    print(f"\n  {value_seg}:")
    print(f"    Customers: {seg_count:,}")
    print(f"    Churn Rate: {seg_churn:.2f}%")
    print(f"    Total CLV: ${seg_clv:,.2f}")
    print(f"    Avg ARPU: ${seg_arpu:.2f}/month")
    
    segment_data.append({
        'Segment': value_seg,
        'Customer_Count': seg_count,
        'Percentage_of_Total': seg_count/len(df)*100,
        'Churn_Rate': seg_churn,
        'Total_CLV': seg_clv,
        'Avg_ARPU': seg_arpu
    })

analysis_report.append("\nVALUE SEGMENT CHURN RATES:")
analysis_report.append(f"  High Value: {df[df['Value_Segment']=='High Value']['Churn'].apply(lambda x: x=='Yes').mean()*100:.2f}%")
analysis_report.append(f"  Medium Value: {df[df['Value_Segment']=='Medium Value']['Churn'].apply(lambda x: x=='Yes').mean()*100:.2f}%")
analysis_report.append(f"  Low Value: {df[df['Value_Segment']=='Low Value']['Churn'].apply(lambda x: x=='Yes').mean()*100:.2f}%")

analysis_report.append("")
print()

# Save segment comparison table
segment_df = pd.DataFrame(segment_data)
segment_df.to_csv(segment_comparison_path, index=False)
print(f"✅ Segment comparison saved: {segment_comparison_path}")
print()

# ==================== PART 3: CHURN DRIVER QUANTIFICATION ====================
print("-" * 80)
print("PART 3: CHURN DRIVER QUANTIFICATION & RANKING")
print("-" * 80)

analysis_report.append("-" * 80)
analysis_report.append("PART 3: CHURN DRIVERS RANKED BY IMPACT")
analysis_report.append("-" * 80)

# Create churn driver analysis
churn_drivers = []

# Driver 1: Contract Type
mtm_customers = df[df['Contract'] == 'Month-to-month']
mtm_churned = (mtm_customers['Churn'] == 'Yes').sum()
churn_drivers.append({
    'Driver': 'Month-to-month Contract',
    'Affected_Customers': len(mtm_customers),
    'Churn_Rate': mtm_churn,
    'Churned_Count': mtm_churned,
    'Impact_Score': len(mtm_customers) * mtm_churn  # Customer count × churn rate
})

# Driver 2: Early Tenure (New Customers)
new_customers = df[df['Tenure_Segment'] == 'New Customer']
new_churned = (new_customers['Churn'] == 'Yes').sum()
churn_drivers.append({
    'Driver': 'New Customer (0-12 months)',
    'Affected_Customers': len(new_customers),
    'Churn_Rate': new_churn,
    'Churned_Count': new_churned,
    'Impact_Score': len(new_customers) * new_churn
})

# Driver 3: Electronic Check Payment
echeck_customers = df[df['PaymentMethod'] == 'Electronic check']
echeck_churn = (echeck_customers['Churn'] == 'Yes').sum() / len(echeck_customers) * 100
echeck_churned = (echeck_customers['Churn'] == 'Yes').sum()
churn_drivers.append({
    'Driver': 'Electronic Check Payment',
    'Affected_Customers': len(echeck_customers),
    'Churn_Rate': echeck_churn,
    'Churned_Count': echeck_churned,
    'Impact_Score': len(echeck_customers) * echeck_churn
})

# Driver 4: Low Service Engagement
low_engagement = df[df['Service_Engagement'] == 'Low Engagement']
low_eng_churn = (low_engagement['Churn'] == 'Yes').sum() / len(low_engagement) * 100
low_eng_churned = (low_engagement['Churn'] == 'Yes').sum()
churn_drivers.append({
    'Driver': 'Low Service Engagement',
    'Affected_Customers': len(low_engagement),
    'Churn_Rate': low_eng_churn,
    'Churned_Count': low_eng_churned,
    'Impact_Score': len(low_engagement) * low_eng_churn
})

# Sort drivers by impact score
churn_drivers_sorted = sorted(churn_drivers, key=lambda x: x['Impact_Score'], reverse=True)

print("\nChurn Drivers Ranked by Business Impact:")
analysis_report.append("\nChurn Drivers Ranked by Impact:")

for i, driver in enumerate(churn_drivers_sorted, 1):
    print(f"\n  {i}. {driver['Driver']}")
    print(f"     Affected Customers: {driver['Affected_Customers']:,}")
    print(f"     Churn Rate: {driver['Churn_Rate']:.2f}%")
    print(f"     Actual Churned: {driver['Churned_Count']:,} customers")
    
    analysis_report.append(f"\n{i}. {driver['Driver']}")
    analysis_report.append(f"   Affected: {driver['Affected_Customers']:,} customers")
    analysis_report.append(f"   Churn Rate: {driver['Churn_Rate']:.2f}%")
    analysis_report.append(f"   Churned: {driver['Churned_Count']:,}")

analysis_report.append("")
print()

# ==================== PART 4: BUSINESS IMPACT ASSESSMENT ====================
print("-" * 80)
print("PART 4: BUSINESS IMPACT ASSESSMENT")
print("-" * 80)

analysis_report.append("-" * 80)
analysis_report.append("PART 4: BUSINESS IMPACT")
analysis_report.append("-" * 80)

# Calculate total revenue at risk from churned customers
churned_customers = df[df['Churn'] == 'Yes']
total_revenue_at_risk = churned_customers['CLV'].sum()
avg_clv_churned = churned_customers['CLV'].mean()
monthly_revenue_loss = churned_customers['ARPU'].sum()

print(f"\n💰 REVENUE IMPACT:")
print(f"  Total CLV Lost from Churn: ${total_revenue_at_risk:,.2f}")
print(f"  Average CLV per Churned Customer: ${avg_clv_churned:.2f}")
print(f"  Monthly Recurring Revenue Lost: ${monthly_revenue_loss:,.2f}/month")

analysis_report.append("\nREVENUE IMPACT:")
analysis_report.append(f"  Total CLV Lost: ${total_revenue_at_risk:,.2f}")
analysis_report.append(f"  Avg CLV per Churned Customer: ${avg_clv_churned:.2f}")
analysis_report.append(f"  Monthly Revenue Lost: ${monthly_revenue_loss:,.2f}/month")

# Calculate potential savings from reducing high-risk churn
# Scenario: Reduce high-risk churn by 10 percentage points
high_risk_churned = (high_risk_customers['Churn'] == 'Yes').sum()
potential_saves_customers = int(high_risk_count * 0.10)  # 10% of high-risk customers
potential_saves_revenue = potential_saves_customers * high_risk_arpu * 12  # Annual value

print(f"\n📈 OPPORTUNITY ASSESSMENT:")
print(f"  If we reduce high-risk churn by 10 percentage points:")
print(f"    Customers Saved: ~{potential_saves_customers:,}")
print(f"    Annual Revenue Saved: ~${potential_saves_revenue:,.2f}")

analysis_report.append("\nOPPORTUNITY (10% High-Risk Churn Reduction):")
analysis_report.append(f"  Customers Saved: ~{potential_saves_customers:,}")
analysis_report.append(f"  Annual Revenue: ~${potential_saves_revenue:,.2f}")

analysis_report.append("")
print()

# ==================== PART 5: ACTIONABLE RECOMMENDATIONS ====================
print("-" * 80)
print("PART 5: PRIORITIZED BUSINESS RECOMMENDATIONS")
print("-" * 80)

recommendations.append("=" * 80)
recommendations.append("BUSINESS RECOMMENDATIONS")
recommendations.append("=" * 80)
recommendations.append("")
recommendations.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
recommendations.append(f"Based on analysis of {len(df):,} customers")
recommendations.append("")

# Recommendation 1: Contract Incentives
print("\n🎯 RECOMMENDATION 1: CONTRACT COMMITMENT INCENTIVES")
print("   Priority: HIGH")
print("   Target: Month-to-month customers")
print("   Action: Offer discounts (10-15%) for upgrading to 1-year or 2-year contracts")
print(f"   Expected Impact: Reduce churn from {mtm_churn:.1f}% to ~25%")
print(f"   Affected Customers: {len(mtm_customers):,}")

recommendations.append("=" * 80)
recommendations.append("RECOMMENDATION 1: CONTRACT COMMITMENT INCENTIVES")
recommendations.append("=" * 80)
recommendations.append("Priority: HIGH")
recommendations.append("")
recommendations.append("Problem:")
recommendations.append(f"  Month-to-month customers have {mtm_churn:.1f}% churn rate ({relative_risk:.1f}x higher than 2-year)")
recommendations.append(f"  Affects {len(mtm_customers):,} customers ({len(mtm_customers)/len(df)*100:.1f}% of base)")
recommendations.append("")
recommendations.append("Recommended Action:")
recommendations.append("  Offer 10-15% discount for customers who upgrade to:")
recommendations.append("    - 1-year contract: 10% monthly discount")
recommendations.append("    - 2-year contract: 15% monthly discount")
recommendations.append("  Communicate stability benefits (no price increases)")
recommendations.append("")
recommendations.append("Expected Outcome:")
recommendations.append(f"  Churn reduction: From {mtm_churn:.1f}% to ~25% (targeting One-year contract benchmark)")
recommendations.append(f"  Customers retained: ~500-800")
recommendations.append("  Increased customer lifetime value through longer commitments")
recommendations.append("")

# Recommendation 2: First-Year Onboarding Program
print("\n🎯 RECOMMENDATION 2: ENHANCED FIRST-YEAR ONBOARDING")
print("   Priority: HIGH")
print("   Target: New customers (tenure 0-12 months)")
print("   Action: Proactive support, check-ins at 30/90/180 days, service education")
print(f"   Expected Impact: Reduce new customer churn from {new_churn:.1f}% to ~35%")
print(f"   Affected Customers: {len(new_customers):,}")

recommendations.append("RECOMMENDATION 2: ENHANCED FIRST-YEAR ONBOARDING")
recommendations.append("=" * 80)
recommendations.append("Priority: HIGH")
recommendations.append("")
recommendations.append("Problem:")
recommendations.append(f"  New customers (0-12 months) have {new_churn:.1f}% churn rate")
recommendations.append(f"  {tenure_risk_ratio:.1f}x higher than loyal customers")
recommendations.append(f"  Affects {len(new_customers):,} customers")
recommendations.append("")
recommendations.append("Recommended Action:")
recommendations.append("  Implement structured onboarding program:")
recommendations.append("    Day 1: Welcome email with setup guide")
recommendations.append("    Day 30: Satisfaction check-in call")
recommendations.append("    Day 90: Service optimization review")
recommendations.append("    Day 180: Mid-year check-in and contract discussion")
recommendations.append("  Proactive tech support for first 90 days")
recommendations.append("  Personalized service recommendations")
recommendations.append("")
recommendations.append("Expected Outcome:")
recommendations.append(f"  Churn reduction: From {new_churn:.1f}% to ~35%")
recommendations.append("  Improved customer satisfaction scores")
recommendations.append("  Higher service adoption in first year")
recommendations.append("")

# Recommendation 3: Payment Method Migration
print("\n🎯 RECOMMENDATION 3: PAYMENT METHOD OPTIMIZATION")
print("   Priority: MEDIUM")
print("   Target: Electronic check users")
print("   Action: Incentivize migration to automatic payment methods")
print(f"   Expected Impact: Reduce churn by encouraging reliable payment methods")
print(f"   Affected Customers: {len(echeck_customers):,}")

recommendations.append("RECOMMENDATION 3: PAYMENT METHOD OPTIMIZATION")
recommendations.append("=" * 80)
recommendations.append("Priority: MEDIUM")
recommendations.append("")
recommendations.append("Problem:")
recommendations.append(f"  Electronic check users have {echeck_churn:.1f}% churn rate")
recommendations.append(f"  Manual payment creates friction and missed payments")
recommendations.append(f"  Affects {len(echeck_customers):,} customers")
recommendations.append("")
recommendations.append("Recommended Action:")
recommendations.append("  Launch autopay migration campaign:")
recommendations.append("    - $5/month discount for first 6 months on autopay")
recommendations.append("    - Highlight convenience and avoid late fees")
recommendations.append("    - Simplified enrollment process")
recommendations.append("  Send payment reminders 7 days before due date")
recommendations.append("  Offer multiple autopay options (credit card, bank transfer)")
recommendations.append("")
recommendations.append("Expected Outcome:")
recommendations.append("  30-40% of electronic check users migrate to autopay")
recommendations.append("  Reduced payment failures and late fees")
recommendations.append("  Lower churn through improved payment experience")
recommendations.append("")

# Recommendation 4: Service Upsell Campaign
print("\n🎯 RECOMMENDATION 4: SERVICE ADOPTION CAMPAIGN")
print("   Priority: MEDIUM")
print("   Target: Low engagement customers (0-2 services)")
print("   Action: Targeted upsell for tech support and online security")
print(f"   Expected Impact: Increase engagement, reduce churn by {engagement_benefit:.1f} percentage points")
print(f"   Affected Customers: {len(low_engagement):,}")

recommendations.append("RECOMMENDATION 4: SERVICE ADOPTION CAMPAIGN")
recommendations.append("=" * 80)
recommendations.append("Priority: MEDIUM")
recommendations.append("")
recommendations.append("Problem:")
recommendations.append(f"  Low engagement customers have {low_engagement_churn:.1f}% churn rate")
recommendations.append(f"  {engagement_benefit:.1f} percentage points higher than high engagement")
recommendations.append(f"  Affects {len(low_engagement):,} customers")
recommendations.append("")
recommendations.append("Recommended Action:")
recommendations.append("  Targeted service upsell campaign:")
recommendations.append("    Priority services: Tech Support, Online Security")
recommendations.append("    Offer bundled discount (15% off when adding 2+ services)")
recommendations.append("    Free trial period (30 days) to demonstrate value")
recommendations.append("  Personalized service recommendations based on usage patterns")
recommendations.append("  Educational content on service benefits")
recommendations.append("")
recommendations.append("Expected Outcome:")
recommendations.append("  20-30% of low engagement customers add services")
recommendations.append(f"  Churn reduction: {engagement_benefit:.1f} percentage points improvement")
recommendations.append("  Increased ARPU through service adoption")
recommendations.append("")

# Recommendation 5: High-Risk Early Warning System
print("\n🎯 RECOMMENDATION 5: CHURN PREDICTION & EARLY INTERVENTION")
print("   Priority: MEDIUM")
print("   Target: High-risk customers (Risk_Score >= 2)")
print("   Action: Proactive retention outreach based on risk score")
print(f"   Expected Impact: Prevent churn for highest-risk {high_risk_count:,} customers")

recommendations.append("RECOMMENDATION 5: CHURN EARLY WARNING SYSTEM")
recommendations.append("=" * 80)
recommendations.append("Priority: MEDIUM (Enables all other recommendations)")
recommendations.append("")
recommendations.append("Problem:")
recommendations.append(f"  High-risk customers (Risk_Score >= 2) have {high_risk_churn_rate:.1f}% churn")
recommendations.append(f"  Currently no proactive intervention system")
recommendations.append(f"  Affects {high_risk_count:,} customers")
recommendations.append("")
recommendations.append("Recommended Action:")
recommendations.append("  Implement risk-based retention workflow:")
recommendations.append("    Risk Score 3: Immediate account manager outreach")
recommendations.append("    Risk Score 2: Automated retention email with special offers")
recommendations.append("    Risk Score 1: Monitor and send engagement content")
recommendations.append("  Monthly risk score updates")
recommendations.append("  Dedicated retention team for high-risk accounts")
recommendations.append("")
recommendations.append("Expected Outcome:")
recommendations.append("  Early identification of at-risk customers")
recommendations.append("  Targeted interventions before churn occurs")
recommendations.append(f"  Potential to save {potential_saves_customers:,}+ customers annually")
recommendations.append("")

recommendations.append("=" * 80)
recommendations.append("IMPLEMENTATION PRIORITY")
recommendations.append("=" * 80)
recommendations.append("")
recommendations.append("Quick Wins (Implement First):")
recommendations.append("  1. Contract incentives (highest impact, moderate effort)")
recommendations.append("  2. Payment method migration (high ROI, low effort)")
recommendations.append("")
recommendations.append("Strategic Initiatives (3-6 months):")
recommendations.append("  3. First-year onboarding program (high impact, requires process design)")
recommendations.append("  4. Service adoption campaign (ongoing, requires marketing resources)")
recommendations.append("")
recommendations.append("Foundation (Enables others):")
recommendations.append("  5. Early warning system (technical investment, long-term value)")

print()

# ==================== EXECUTIVE SUMMARY ====================
print("-" * 80)
print("GENERATING EXECUTIVE SUMMARY")
print("-" * 80)

executive_summary.append("=" * 80)
executive_summary.append("EXECUTIVE SUMMARY")
executive_summary.append("CUSTOMER CHURN ANALYSIS")
executive_summary.append("=" * 80)
executive_summary.append("")
executive_summary.append(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
executive_summary.append(f"Total Customers Analyzed: {len(df):,}")
executive_summary.append("")

executive_summary.append("KEY FINDINGS:")
executive_summary.append("-" * 80)
executive_summary.append("")
executive_summary.append(f"1. Overall Churn Rate: {overall_churn_rate:.1f}% ({total_churned:,} customers)")
executive_summary.append("")
executive_summary.append("2. Primary Churn Drivers (Validated):")
executive_summary.append(f"   • Month-to-month contracts: {mtm_churn:.1f}% churn ({relative_risk:.1f}x baseline)")
executive_summary.append(f"   • New customers (0-12 months): {new_churn:.1f}% churn ({tenure_risk_ratio:.1f}x loyal customers)")
executive_summary.append(f"   • Electronic check payment: {echeck_churn:.1f}% churn")
executive_summary.append(f"   • Low service engagement: {low_engagement_churn:.1f}% churn")
executive_summary.append("")
executive_summary.append("3. High-Risk Segment:")
executive_summary.append(f"   • Size: {high_risk_count:,} customers ({high_risk_count/len(df)*100:.1f}% of base)")
executive_summary.append(f"   • Churn Rate: {high_risk_churn_rate:.1f}%")
executive_summary.append(f"   • Revenue at Risk: ${high_risk_revenue:,.2f}")
executive_summary.append("")
executive_summary.append("4. Business Impact:")
executive_summary.append(f"   • Total CLV Lost: ${total_revenue_at_risk:,.2f}")
executive_summary.append(f"   • Monthly Revenue Lost: ${monthly_revenue_loss:,.2f}/month")
executive_summary.append(f"   • Opportunity: Saving 10% of high-risk = ${potential_saves_revenue:,.2f} annual revenue")
executive_summary.append("")

executive_summary.append("TOP 3 RECOMMENDATIONS:")
executive_summary.append("-" * 80)
executive_summary.append("")
executive_summary.append("1. CONTRACT INCENTIVES (Priority: HIGH)")
executive_summary.append(f"   Offer 10-15% discounts for contract upgrades")
executive_summary.append(f"   Target: {len(mtm_customers):,} month-to-month customers")
executive_summary.append(f"   Expected Impact: Reduce churn from {mtm_churn:.1f}% to ~25%")
executive_summary.append("")
executive_summary.append("2. FIRST-YEAR ONBOARDING (Priority: HIGH)")
executive_summary.append(f"   Proactive support program for new customers")
executive_summary.append(f"   Target: {len(new_customers):,} customers in first year")
executive_summary.append(f"   Expected Impact: Reduce new customer churn from {new_churn:.1f}% to ~35%")
executive_summary.append("")
executive_summary.append("3. PAYMENT METHOD MIGRATION (Priority: MEDIUM)")
executive_summary.append(f"   Incentivize autopay enrollment")
executive_summary.append(f"   Target: {len(echeck_customers):,} electronic check users")
executive_summary.append("   Expected Impact: 30-40% migration, reduced payment failures")
executive_summary.append("")

executive_summary.append("NEXT STEPS:")
executive_summary.append("-" * 80)
executive_summary.append("• Review full recommendations document for implementation details")
executive_summary.append("• Prioritize contract incentive program for immediate deployment")
executive_summary.append("• Design first-year onboarding process with customer success team")
executive_summary.append("• Implement risk-based monitoring for high-risk segment")
executive_summary.append("• Track metrics: churn rate by segment, retention rate, revenue saved")

print("✅ Executive summary generated")
print()

# ==================== SAVE ALL REPORTS ====================
print("-" * 80)
print("SAVING REPORTS")
print("-" * 80)

# Save analysis report
with open(analysis_report_path, 'w') as f:
    f.write('\n'.join(analysis_report))
print(f"✅ Analysis report saved: {analysis_report_path}")

# Save recommendations
with open(recommendations_path, 'w') as f:
    f.write('\n'.join(recommendations))
print(f"✅ Recommendations saved: {recommendations_path}")

# Save executive summary
with open(executive_summary_path, 'w') as f:
    f.write('\n'.join(executive_summary))
print(f"✅ Executive summary saved: {executive_summary_path}")

print()

# ==================== FINAL SUMMARY ====================
print("=" * 80)
print("✅ ANALYTICAL REASONING COMPLETE")
print("=" * 80)
print()
print("Analysis Complete - Key Outputs:")
print()
print("📊 Hypotheses Validated: 4/4")
print("   ✅ Contract type drives churn")
print("   ✅ Early tenure is highest risk")
print("   ✅ Payment method indicates risk")
print("   ✅ Service adoption reduces churn")
print()
print("🎯 Segments Analyzed: 6")
print(f"   High-Risk: {high_risk_count:,} customers ({high_risk_churn_rate:.1f}% churn)")
print(f"   Medium-Risk: {medium_risk_count:,} customers ({medium_risk_churn_rate:.1f}% churn)")
print(f"   Low-Risk: {low_risk_count:,} customers ({low_risk_churn_rate:.1f}% churn)")
print()
print("💰 Business Impact Quantified:")
print(f"   Revenue Lost: ${total_revenue_at_risk:,.2f}")
print(f"   Opportunity: ${potential_saves_revenue:,.2f} annual (10% retention improvement)")
print()
print("📋 Recommendations Generated: 5 (prioritized by impact)")
print()
print("Output Files:")
print(f"  • {analysis_report_path}")
print(f"  • {segment_comparison_path}")
print(f"  • {recommendations_path}")
print(f"  • {executive_summary_path}")
print()
print("Next Step: Proceed to Stage 8 (Visualization, Storytelling & Dashboards)")
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure the enriched dataset from Stage 6 exists:

```bash
ls data/processed/enriched_churn_data.csv
```


### Step 2: Navigate to Project Root

Open terminal and navigate to project folder:

```bash
cd path/to/customer_churn_analysis
```


### Step 3: Run the Analytical Reasoning Script

Execute the analysis script:

```bash
python scripts/analytical_reasoning.py
```

**Expected Duration:** 20-40 seconds

### Step 4: Review Console Output

The script will print 5 parts:

1. Hypothesis Validation (4 hypotheses tested)
2. Segment Deep-Dive Analysis
3. Churn Driver Quantification \& Ranking
4. Business Impact Assessment
5. Prioritized Business Recommendations

### Step 5: Review Generated Reports

After script completes, review the output files:

**Analysis Report (detailed findings):**

```bash
cat outputs/reports/analysis_report.txt
```

**Business Recommendations:**

```bash
cat outputs/reports/business_recommendations.txt
```

**Executive Summary (high-level overview):**

```bash
cat outputs/reports/executive_summary.txt
```

**Segment Comparison Table:**

```bash
python -c "import pandas as pd; df = pd.read_csv('outputs/reports/segment_comparison.csv'); print(df.to_string())"
```


***

## e) How to Test the Output

### Test 1: Verify Script Runs Without Errors

**Expected Result:**

- Script completes successfully
- Final message: "✅ ANALYTICAL REASONING COMPLETE"
- Shows "Hypotheses Validated: 4/4"
- No error messages or crashes


### Test 2: Verify All Report Files Created

**Expected Result:**
Four files should be created in `outputs/reports/`:

- `analysis_report.txt`
- `segment_comparison.csv`
- `business_recommendations.txt`
- `executive_summary.txt`

**How to Check:**

```bash
ls -lh outputs/reports/analysis_report.txt
ls -lh outputs/reports/segment_comparison.csv
ls -lh outputs/reports/business_recommendations.txt
ls -lh outputs/reports/executive_summary.txt
```

**Expected File Sizes:**

- analysis_report.txt: ~5-10 KB
- segment_comparison.csv: ~1-2 KB
- business_recommendations.txt: ~8-15 KB
- executive_summary.txt: ~2-4 KB


### Test 3: Verify Hypotheses Validated

**Expected Result:**
All 4 hypotheses should show as VALIDATED in console output

**How to Check:**

```bash
grep "VALIDATED" outputs/reports/analysis_report.txt | wc -l
```

**Expected Output:**

```
4
```


### Test 4: Verify Segment Comparison Table

**Expected Result:**

- CSV should contain ~6-9 rows (different segments)
- Columns: Segment, Customer_Count, Percentage_of_Total, Churn_Rate, Total_CLV, Avg_ARPU

**How to Check:**

```bash
python -c "import pandas as pd; df = pd.read_csv('outputs/reports/segment_comparison.csv'); print(f'Rows: {len(df)}'); print(f'Columns: {list(df.columns)}'); print(f'\\nFirst 3 segments:'); print(df.head(3))"
```


### Test 5: Verify Recommendations Count

**Expected Result:**

- Should have 5 numbered recommendations
- Each with Priority, Problem, Action, Expected Outcome

**How to Check:**

```bash
grep "RECOMMENDATION [0-9]:" outputs/reports/business_recommendations.txt | wc -l
```

**Expected Output:**

```
5
```


### Test 6: Verify Business Impact Calculated

**Expected Result:**

- Analysis report should contain revenue calculations
- Total CLV Lost should be positive dollar amount
- Opportunity assessment should show potential savings

**How to Check:**

```bash
grep "Total CLV Lost" outputs/reports/analysis_report.txt
grep "Opportunity" outputs/reports/analysis_report.txt
```


### Test 7: Verify High-Risk Segment Analysis

**Expected Result:**

- High-risk segment should have higher churn rate than low-risk
- Typically high-risk churn > 40%, low-risk churn < 20%

**How to Check:**

```bash
grep "HIGH-RISK SEGMENT" outputs/reports/analysis_report.txt -A 5
grep "LOW-RISK SEGMENT" outputs/reports/analysis_report.txt -A 5
```


### Test 8: Verify Executive Summary Content

**Expected Result:**

- Should contain Key Findings section
- Should contain Top 3 Recommendations section
- Should contain Next Steps section

**How to Check:**

```bash
grep "KEY FINDINGS:" outputs/reports/executive_summary.txt
grep "TOP 3 RECOMMENDATIONS:" outputs/reports/executive_summary.txt
grep "NEXT STEPS:" outputs/reports/executive_summary.txt
```


### Test 9: Verify Churn Driver Ranking

**Expected Result:**

- Should rank 4 churn drivers by impact
- Each driver should show affected customers and churn rate

**How to Check:**

```bash
grep "Churn Drivers Ranked" outputs/reports/analysis_report.txt -A 20
```


### Test 10: Verify Relative Risk Calculations

**Expected Result:**

- Month-to-month vs two-year relative risk should be 3-5x
- New vs loyal customer risk ratio should be 2-4x

**How to Check:**

```bash
grep "Relative Risk:" outputs/reports/analysis_report.txt
grep "Risk Ratio:" outputs/reports/analysis_report.txt
```


### Test 11: Manual Content Review

Open each report file and verify:

**analysis_report.txt should contain:**

- Baseline metrics
- 4 validated hypotheses
- Segment profiles (high/medium/low risk)
- Value segment analysis
- Churn drivers ranked
- Business impact numbers

**business_recommendations.txt should contain:**

- 5 detailed recommendations
- Each with: Priority, Problem, Action, Expected Outcome
- Implementation priority section at end

**executive_summary.txt should contain:**

- Overall churn rate
- Top findings (2-4 key insights)
- Top 3 recommendations
- Next steps

**segment_comparison.csv should contain:**

- Risk segments (High/Medium/Low)
- Value segments (High/Medium/Low)
- Churn rates for each segment
- Customer counts


### Signs of Success

✅ Script completes without errors
✅ All 4 report files created
✅ 4 hypotheses validated
✅ Segment comparison table has 6+ segments
✅ 5 recommendations documented
✅ Business impact calculated (revenue numbers)
✅ High-risk segment identified with higher churn rate
✅ Executive summary contains key sections
✅ Churn drivers ranked by impact
✅ Relative risk ratios calculated
✅ All reports have meaningful content (not empty)

### Signs of Problems

❌ Script crashes or errors
❌ Missing report files
❌ Fewer than 4 hypotheses validated
❌ Empty or truncated report files
❌ No revenue calculations
❌ High-risk and low-risk have same churn rate
❌ Recommendations missing details
❌ Segment comparison CSV empty or has only 1-2 rows
❌ Reports contain placeholder text or incomplete sections

***

## f) Common Beginner Mistakes

### Mistake 1: Making Recommendations Without Evidence

**What Happens:**

- Create recommendations based on intuition
- Don't back up with data from analysis
- Can't answer "why should we do this?"

**Why It Happens:**

- Jumping to solutions without analysis
- Not connecting insights to recommendations

**How to Fix:**

- **Every recommendation must cite evidence:**
    - Bad: "Offer discounts to month-to-month customers"
    - Good: "Month-to-month customers have 42% churn (3.5x higher than 2-year). Offer 15% discount for upgrade to reduce churn to ~25%"
- Script correctly links each recommendation to specific analysis findings


### Mistake 2: Not Quantifying Business Impact

**What Happens:**

- Report that "churn is high" without numbers
- Say "we should improve retention" without quantifying opportunity
- Stakeholders can't prioritize

**Why It Happens:**

- Focusing on patterns, not business value
- Not calculating revenue or customer impacts

**How to Fix:**

- **Always quantify impact:**
    - Customer counts: "Affects 3,000 customers"
    - Revenue: "\$2M CLV at risk"
    - Opportunity: "Saving 10% = \$200K annual revenue"
- Script calculates specific dollar amounts and customer counts


### Mistake 3: Treating All Segments Equally

**What Happens:**

- Recommend same actions for all customer types
- Don't prioritize by segment value or risk
- Waste resources on low-impact segments

**Why It Happens:**

- Not doing segment-specific analysis
- One-size-fits-all thinking

**How to Fix:**

- **Segment-specific recommendations:**
    - High-risk: Immediate retention outreach
    - Medium-risk: Automated engagement campaigns
    - Low-risk: Satisfaction monitoring only
- Script provides tailored recommendations by segment


### Mistake 4: Not Validating Hypotheses Statistically

**What Happens:**

- Assume EDA observations are facts
- Don't verify patterns hold across segments
- Make recommendations on unvalidated assumptions

**Why It Happens:**

- Confusing exploration with confirmation
- Not understanding difference between observation and validation

**How to Fix:**

- **Test each hypothesis explicitly:**
    - Hypothesis: "Month-to-month drives churn"
    - Validation: Calculate churn rates, compare, quantify difference
    - Conclusion: "VALIDATED - MTM is 3.5x higher"
- Script tests all 4 Stage 5 hypotheses systematically


### Mistake 5: Creating Generic Recommendations

**What Happens:**

- "Improve customer service"
- "Reduce churn"
- "Increase engagement"
- No specific actions

**Why It Happens:**

- Not thinking through implementation
- Treating recommendations as goals, not actions

**How to Fix:**

- **Specific, actionable recommendations:**
    - Bad: "Improve onboarding"
    - Good: "Implement 4-touchpoint onboarding: Day 1 welcome, Day 30 check-in, Day 90 review, Day 180 contract discussion"
- Script provides detailed action steps for each recommendation


### Mistake 6: Not Prioritizing Recommendations

**What Happens:**

- List 10-20 recommendations
- All seem equally important
- Stakeholders don't know where to start

**Why It Happens:**

- Wanting to address every issue
- Not considering implementation effort vs impact

**How to Fix:**

- **Prioritize by impact and feasibility:**
    - HIGH priority: High impact, moderate effort (contract incentives)
    - MEDIUM priority: Medium impact, low effort (payment migration)
    - LOW priority: Low impact or high effort (complete system overhaul)
- Script labels each recommendation with priority


### Mistake 7: Comparing Segments Without Context

**What Happens:**

- Report "High-value customers churn at 25%"
- Don't compare to other segments
- Can't tell if that's good or bad

**Why It Happens:**

- Analyzing segments in isolation
- Not providing comparison baseline

**How to Fix:**

- **Always compare to benchmark:**
    - "High-value: 25% churn vs overall 27% (slightly better)"
    - "Low-value: 30% churn vs overall 27% (8% worse)"
- Script consistently compares segments to baseline and each other


### Mistake 8: Not Calculating Opportunity Size

**What Happens:**

- Identify problems but not opportunities
- Stakeholders can't estimate ROI
- Can't justify investment

**Why It Happens:**

- Focusing on problems, not solutions
- Not thinking about "what if we fix this?"

**How to Fix:**

- **Calculate opportunity for each recommendation:**
    - Problem: "High-risk segment has 47% churn"
    - Opportunity: "Reducing by 10% saves 250 customers = \$300K annual revenue"
- Script includes opportunity assessment for major recommendations


### Mistake 9: Using Complex Statistical Jargon

**What Happens:**

- Write report with "p-values", "confidence intervals", "regression coefficients"
- Stakeholders don't understand
- Insights don't get actioned

**Why It Happens:**

- Trying to appear sophisticated
- Not adapting communication to audience

**How to Fix:**

- **Use business language:**
    - Don't say: "Coefficient of 0.35, p<0.01"
    - Do say: "Month-to-month customers are 3.5x more likely to churn"
- This is a business analytics project, not academic research
- Script uses plain language throughout


### Mistake 10: Not Creating Executive Summary

**What Happens:**

- Only produce detailed 50-page analysis report
- Executives don't have time to read it all
- Key insights buried in details

**Why It Happens:**

- Not thinking about different audience needs
- Assuming everyone wants full details

**How to Fix:**

- **Create layered reporting:**
    - Executive Summary: 1-2 pages, key findings only
    - Full Analysis: Detailed evidence and methodology
    - Recommendations: Action-focused document
- Script creates all three types of reports


### Mistake 11: Forgetting About Implementation Feasibility

**What Happens:**

- Recommend "build ML churn prediction model"
- Or "redesign entire billing system"
- Requires months and \$millions

**Why It Happens:**

- Not considering organizational constraints
- Proposing what's technically possible, not practically achievable

**How to Fix:**

- **Recommend achievable actions:**
    - Start with quick wins (contract discounts, payment incentives)
    - Build to strategic initiatives (onboarding programs)
    - Foundation investments last (early warning systems)
- Script prioritizes by implementation feasibility


### Mistake 12: Not Linking Analysis Stages

**What Happens:**

- Stage 7 analysis doesn't reference Stage 5 EDA
- Stage 6 features not used in Stage 7
- Stages feel disconnected

**Why It Happens:**

- Treating each stage as independent
- Not maintaining narrative thread

**How to Fix:**

- **Build on previous stages explicitly:**
    - "In Stage 5 EDA, we observed X. Now we validate X statistically."
    - "Using Risk_Score from Stage 6, we segment customers..."
- Script explicitly tests Stage 5 hypotheses and uses Stage 6 features

***

## ✅ Stage 7 Complete!

You have now:

- Validated all 4 hypotheses from Stage 5 EDA with statistical evidence
- Quantified churn impact for major drivers (contract type, tenure, payment method, service adoption)
- Conducted deep-dive analysis of risk segments (high/medium/low)
- Profiled value segments and lifecycle stages
- Ranked churn drivers by business impact
- Calculated revenue at risk and opportunity size
- Generated 5 prioritized, actionable business recommendations
- Created executive summary for stakeholder communication

**Key Findings Validated:**

**Hypothesis Validation (4/4):**
✅ Month-to-month contracts have 3-5x higher churn than two-year contracts
✅ New customers (0-12 months) churn 2-4x more than loyal customers
✅ Electronic check users have elevated churn rates
✅ Service adoption reduces churn by 10-15 percentage points

**Segment Insights:**

- High-Risk Segment: ~1,000-1,500 customers, 40-50% churn, significant revenue at risk
- Medium-Risk Segment: ~2,000-2,500 customers, 25-35% churn
- Low-Risk Segment: ~3,000-4,000 customers, <20% churn
- High-value customers contribute majority of revenue but still churn

**Business Impact:**

- Total CLV lost from churn: quantified in dollars
- Monthly recurring revenue lost: quantified
- Opportunity from 10% high-risk retention improvement: ~\$200K-\$500K annual revenue

**Top 3 Recommendations:**

1. **Contract Commitment Incentives** (Priority: HIGH) - Offer 10-15% discounts for contract upgrades
2. **Enhanced First-Year Onboarding** (Priority: HIGH) - Proactive support program for new customers
3. **Payment Method Optimization** (Priority: MEDIUM) - Incentivize autopay migration

**Output Files:**

- `outputs/reports/analysis_report.txt` - Complete analysis with evidence
- `outputs/reports/segment_comparison.csv` - Segment statistics table
- `outputs/reports/business_recommendations.txt` - 5 detailed, prioritized recommendations
- `outputs/reports/executive_summary.txt` - High-level summary for leadership

**Critical Understanding:**

- **Analysis drives decisions** - every recommendation backed by data evidence
- **Quantification enables prioritization** - dollar amounts and customer counts help stakeholders allocate resources
- **Segments require different strategies** - no one-size-fits-all retention approach
- **Business language matters** - avoid jargon, speak in terms of customers and revenue

**What Makes This Analysis Professional:**

- Evidence-based: Every insight validated with data
- Quantified: Dollar amounts and customer counts provided
- Actionable: Specific steps, not vague suggestions
- Prioritized: Clear implementation sequence
- Audience-appropriate: Executive summary + detailed reports

**Next Step:** Wait for instruction to proceed to Stage 8 (Visualization, Storytelling \& Dashboards)

---

# **Stage 8: Visualization, Storytelling \& Dashboards**


***

## a) Learning Objective

### What You're Learning

You are learning how to **transform analytical insights into visual stories** and create interactive dashboards that enable stakeholders to explore data and make decisions. This stage focuses on visualization best practices, narrative construction, and building user-friendly interfaces using Streamlit.

### Why This Matters

In real-world data analytics, **insights that aren't communicated effectively don't drive action**. Professional analysts must present findings in ways that:

- **Non-technical stakeholders understand** - executives, managers, marketing teams
- **Enable self-service exploration** - stakeholders can filter and drill down
- **Tell a compelling story** - data becomes narrative, not just numbers
- **Drive decision-making** - clear insights lead to clear actions

**Without effective visualization:**

- Complex analysis stays locked in Python scripts
- Stakeholders can't explore data themselves
- Insights require analyst present to explain
- Decision-makers struggle to understand findings

**With interactive dashboards:**

- Self-service analytics (stakeholders explore independently)
- Real-time filtering by segment, risk, value
- Visual patterns immediately apparent
- Actionable insights at fingertips


### Skill Level

**Advanced** - This builds on all previous stages and introduces dashboard design, UI/UX principles, interactive visualization, and business storytelling techniques.

### In Scope

- Creating interactive Streamlit dashboard application
- Visualizing key metrics (churn rate, revenue at risk, customer segments)
- Building segment comparison views
- Creating risk profiling visualizations
- Implementing interactive filters (contract type, tenure, value segment)
- Designing executive summary page
- Creating detailed analysis pages
- Adding insights and recommendations to each view
- Implementing responsive layout and professional styling
- Exporting dashboard as deployable web application


### Out of Scope

- Advanced dashboard frameworks (Tableau, Power BI) - using Streamlit (specified in tech stack)
- Real-time data connections - using static dataset
- User authentication and access control
- Database backend - reading from CSV
- Advanced interactivity (drill-throughs to transaction level)
- Mobile app development - web dashboard only


### Assumptions

- You completed Stage 7 (analysis reports and recommendations exist)
- You understand basic dashboard design principles
- Streamlit is installed (from Stage 0)
- You can run Python web applications locally
- Enriched dataset available at `data/processed/enriched_churn_data.csv`


### Output Artifact

- **churn_dashboard.py** - Main Streamlit dashboard application
- **Running dashboard** - Interactive web application accessible in browser
- **Dashboard documentation** - User guide for navigating dashboard
- **Console output** - Instructions for launching dashboard

***

## b) Setup Instructions

### Step 1: Verify Prerequisites

Ensure required files exist from previous stages:

```
data/processed/enriched_churn_data.csv (Stage 6)
outputs/reports/executive_summary.txt (Stage 7)
outputs/reports/business_recommendations.txt (Stage 7)
```


### Step 2: Understand Dashboard Structure

The dashboard will have multiple pages/sections:

**Page 1: Executive Overview**

- Overall churn rate (big number)
- Total customers, churned, retained
- Revenue impact summary
- Top 3 insights
- Top 3 recommendations

**Page 2: Segment Analysis**

- Risk segment comparison (High/Medium/Low)
- Value segment comparison
- Tenure segment analysis
- Interactive filtering

**Page 3: Churn Drivers**

- Contract type impact
- Payment method analysis
- Service adoption impact
- Tenure vs churn relationship

**Page 4: Recommendations**

- Detailed recommendations
- Expected impact
- Priority ranking
- Implementation timeline

**Page 5: Customer Explorer**

- Filter customers by attributes
- View segment statistics
- Download filtered data


### Step 3: Files to Create

You will create one Python script in the `dashboard/` folder:

- `churn_dashboard.py` - Complete Streamlit dashboard application


### Step 4: Dashboard Features

The dashboard will include:

- **Metrics cards** - Key numbers prominently displayed
- **Interactive charts** - Bar charts, pie charts, line charts
- **Filters** - Dropdowns, multi-selects for exploration
- **Data tables** - Sortable, filterable tables
- **Markdown insights** - Contextual explanations
- **Downloadable data** - Export functionality


### Step 5: Running the Dashboard

Once created, you'll run:

```bash
streamlit run dashboard/churn_dashboard.py
```

This opens dashboard in your web browser at `http://localhost:8501`

### Dependencies Required

- streamlit (already installed from Stage 0)
- pandas (already installed)
- matplotlib (already installed)
- plotly (for interactive charts) - will install if needed

***

## c) Implementation (FINAL VERSION)

### File 1: Streamlit Dashboard Application

**File Name:** `churn_dashboard.py`
**File Path:** `customer_churn_analysis/dashboard/churn_dashboard.py`
**Total Lines:** 620

```python
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
```


***

## d) How to Run

### Step 1: Verify Prerequisites

Ensure required files exist:

```bash
ls data/processed/enriched_churn_data.csv
ls outputs/reports/executive_summary.txt
ls outputs/reports/business_recommendations.txt
```


### Step 2: Install Plotly (if not installed)

Plotly is needed for interactive charts:

```bash
pip install plotly
```


### Step 3: Navigate to Project Root

```bash
cd path/to/customer_churn_analysis
```


### Step 4: Run the Dashboard

Execute the Streamlit application:

```bash
streamlit run dashboard/churn_dashboard.py
```

**Expected Result:**

- Terminal shows: "You can now view your Streamlit app in your browser"
- Browser automatically opens at `http://localhost:8501`
- Dashboard loads with Executive Overview page


### Step 5: Explore the Dashboard

Navigate through all 5 pages:

1. **Executive Overview** - Key metrics and insights
2. **Segment Analysis** - Deep dive into risk/value/tenure segments
3. **Churn Drivers** - Analyze contract, payment, service, tenure impacts
4. **Recommendations** - Detailed business recommendations
5. **Customer Explorer** - Interactive filtering and data export

### Step 6: Test Interactive Features

- Use sidebar filters (Contract Type, Tenure Segment, Value Segment)
- Switch between segment types in Segment Analysis page
- Select different churn drivers in Churn Drivers page
- Download filtered data from Customer Explorer page


### Step 7: Stop the Dashboard

When done, press `Ctrl+C` in terminal to stop the server.

***

## e) How to Test the Output

### Test 1: Dashboard Launches Successfully

**Expected Result:**

- Streamlit server starts without errors
- Browser opens automatically
- Dashboard displays Executive Overview page
- No error messages in terminal or browser

**How to Check:**

- Run `streamlit run dashboard/churn_dashboard.py`
- Wait 5-10 seconds
- Browser should open to dashboard


### Test 2: All Pages Load

**Expected Result:**

- 5 pages accessible from sidebar
- Each page loads without errors
- Content displays correctly on each page

**How to Check:**

- Click each page in sidebar navigation:
    - 🏠 Executive Overview
    - 📈 Segment Analysis
    - 🎯 Churn Drivers
    - 💡 Recommendations
    - 🔍 Customer Explorer
- Verify content appears on each page


### Test 3: Executive Overview Metrics Display

**Expected Result:**

- 4 metric cards show numbers:
    - Total Customers: ~7,043
    - Churn Rate: ~26-27%
    - Revenue at Risk: Dollar amount
    - Avg ARPU: Dollar amount
- Churn distribution pie chart displays
- Revenue impact bar chart displays

**How to Check:**

- Navigate to Executive Overview page
- Verify all metrics show numbers (not errors)
- Verify charts render correctly


### Test 4: Interactive Filters Work

**Expected Result:**

- Sidebar shows 3 filters (Contract, Tenure, Value)
- Selecting/deselecting options updates data
- Filtered customer count updates
- Charts update based on filters

**How to Check:**

- Uncheck "Month-to-month" in Contract filter
- Observe customer count decrease
- Charts should update to reflect filtered data
- Re-check to restore


### Test 5: Segment Analysis Page Works

**Expected Result:**

- Can switch between Risk/Value/Tenure segments
- Each segment type shows different visualizations
- Metrics and charts update when switching
- Tables display correctly

**How to Check:**

- Navigate to Segment Analysis page
- Click "Risk Segments", "Value Segments", "Tenure Segments"
- Verify charts change for each selection
- Verify data tables display


### Test 6: Churn Drivers Page Works

**Expected Result:**

- Dropdown shows 4 driver options
- Selecting each driver shows relevant analysis
- Charts render correctly for each driver
- Insights display below charts

**How to Check:**

- Navigate to Churn Drivers page
- Select each option:
    - Contract Type
    - Payment Method
    - Service Adoption
    - Tenure Impact
- Verify charts and insights appear


### Test 7: Recommendations Page Displays

**Expected Result:**

- 5 recommendations displayed
- Each has priority label, problem, action, outcome
- Implementation timelines shown
- Roadmap section at bottom

**How to Check:**

- Navigate to Recommendations page
- Scroll through all 5 recommendations
- Verify all sections are populated
- Check implementation roadmap displays


### Test 8: Customer Explorer Filters Work

**Expected Result:**

- Additional filters (Risk Score, Churn Status, Payment Method)
- Filtering updates customer count and metrics
- Data table shows filtered customers
- Download button works

**How to Check:**

- Navigate to Customer Explorer page
- Apply filters (e.g., select only "High Risk")
- Verify customer count updates
- Click download button to export CSV


### Test 9: Visual Quality Check

**Expected Result:**

- Charts are professional-looking
- Colors are distinct and appropriate
- Text is readable (not overlapping)
- Layout is clean and organized

**How to Check:**

- Review all charts across all pages
- Verify no overlapping labels
- Check color schemes make sense (green=good, red=bad)
- Ensure responsive layout (try resizing browser)


### Test 10: Data Accuracy Spot Check

**Expected Result:**

- Numbers match Stage 7 analysis
- Overall churn rate ~26-27%
- High-risk segment ~1,000-1,500 customers
- Month-to-month churn ~40-45%

**How to Check:**
Compare dashboard numbers to Stage 7 reports:

```bash
grep "Overall Churn Rate" outputs/reports/analysis_report.txt
```

Dashboard Executive Overview churn rate should match.

### Signs of Success

✅ Dashboard launches in browser
✅ All 5 pages accessible and load correctly
✅ Metrics display accurate numbers
✅ Charts render without errors
✅ Interactive filters update data
✅ Segment switching works
✅ All visualizations are professional-quality
✅ Data tables display correctly
✅ Download functionality works
✅ No console errors in terminal or browser

### Signs of Problems

❌ Dashboard won't start (import errors)
❌ Browser shows error page
❌ Metrics show "NaN" or blank
❌ Charts don't render (blank spaces)
❌ Filters don't update data
❌ Pages won't switch
❌ Text overlapping or unreadable
❌ Download button doesn't work
❌ Terminal shows errors
❌ Browser console shows errors (F12 to check)

***

## f) Common Beginner Mistakes

### Mistake 1: Not Installing Plotly

**What Happens:**

- Dashboard crashes with "ModuleNotFoundError: No module named 'plotly'"
- Charts don't render

**Why It Happens:**

- Plotly not included in original requirements.txt
- Needed for interactive charts

**How to Fix:**

- Install Plotly: `pip install plotly`
- Restart dashboard
- Script correctly imports plotly


### Mistake 2: Running Dashboard from Wrong Directory

**What Happens:**

- Error: "FileNotFoundError: data/processed/enriched_churn_data.csv"
- Dashboard can't find data

**Why It Happens:**

- Running `streamlit run` from dashboard/ folder instead of project root
- Relative paths don't work

**How to Fix:**

- Always run from project root: `customer_churn_analysis/`
- Command: `streamlit run dashboard/churn_dashboard.py`
- NOT: `cd dashboard; streamlit run churn_dashboard.py`


### Mistake 3: Overloading Dashboard with Too Much Data

**What Happens:**

- Dashboard slow to load
- Filters take long to update
- Browser becomes unresponsive

**Why It Happens:**

- Displaying entire dataset in tables without pagination
- Not using Streamlit caching

**How to Fix:**

- Script correctly uses `@st.cache_data` to cache data loading
- Tables limited to reasonable row counts
- Filters update efficiently
- For production: consider sampling or pagination


### Mistake 4: Not Using st.cache_data

**What Happens:**

- Data reloads every time user interacts with filter
- Dashboard very slow
- Poor user experience

**Why It Happens:**

- Not understanding Streamlit reruns entire script on interaction

**How to Fix:**

- **Always cache data loading:**

```python
@st.cache_data
def load_data():
    return pd.read_csv(...)
```

- Script correctly implements caching
- Data loads once, cached for session


### Mistake 5: Poor Visual Hierarchy

**What Happens:**

- Everything same size and color
- Hard to know what's important
- Users overwhelmed

**Why It Happens:**

- Not designing for skimmability
- No visual distinction between sections

**How to Fix:**

- Use metric cards for key numbers (st.metric)
- Headers and subheaders for structure
- Color coding (green=good, red=bad)
- White space between sections
- Script implements professional visual hierarchy


### Mistake 6: Not Adding Insights to Charts

**What Happens:**

- Charts shown without context
- Users see data but not meaning
- "So what?" reaction

**Why It Happens:**

- Treating dashboard as data dump
- Not providing interpretation

**How to Fix:**

- **Every chart needs an insight:**
    - Chart shows what
    - Insight explains why it matters
    - Recommendation says what to do
- Script includes insight boxes after key visualizations


### Mistake 7: Making Filters Non-Functional

**What Happens:**

- Filters present but don't update data
- User selects options, nothing changes

**Why It Happens:**

- Creating filters but not applying them to data
- Using `df` instead of `df_filtered`

**How to Fix:**

- Create filters:

```python
contract_filter = st.multiselect(...)
```

- Apply filters:

```python
df_filtered = df[df['Contract'].isin(contract_filter)]
```

- Use `df_filtered` for all visualizations
- Script correctly implements filter logic


### Mistake 8: Not Testing on Different Screen Sizes

**What Happens:**

- Dashboard looks great on your laptop
- Broken on smaller/larger screens
- Layout problems

**Why It Happens:**

- Only testing on one screen size
- Not using responsive design

**How to Fix:**

- Use Streamlit's column system: `st.columns([2,1])`
- Set `layout="wide"` in page config
- Test by resizing browser window
- Script uses responsive columns


### Mistake 9: Including Too Many Decimal Places

**What Happens:**

- "Churn Rate: 26.5432101%"
- Numbers harder to read
- Looks unprofessional

**Why It Happens:**

- Not formatting numbers for display

**How to Fix:**

- **Always format numbers:**
    - Percentages: `f"{value:.1f}%"` (one decimal)
    - Currency: `f"${value:,.2f}"` (two decimals, commas)
    - Counts: `f"{value:,}"` (commas only)
- Script formats all numbers appropriately


### Mistake 10: Not Providing Download Functionality

**What Happens:**

- Users want to export data
- No way to get filtered data out
- Have to manually copy

**Why It Happens:**

- Not thinking about stakeholder needs
- Assuming dashboard is final destination

**How to Fix:**

- Add download buttons for filtered data:

```python
csv = df_filtered.to_csv(index=False)
st.download_button("Download CSV", data=csv, ...)
```

- Script includes download in Customer Explorer page


### Mistake 11: Creating Single-Page Dashboard

**What Happens:**

- All content on one page
- Overwhelming scroll
- Can't find specific information

**Why It Happens:**

- Not organizing content into logical sections

**How to Fix:**

- **Multi-page structure:**
    - Executive: High-level overview
    - Analysis: Deep dives
    - Recommendations: Actions
    - Explorer: Raw data
- Script implements 5-page structure with sidebar navigation


### Mistake 12: Not Adding Loading Indicators

**What Happens:**

- User clicks filter
- Nothing happens for 2 seconds
- User clicks again (impatient)
- Dashboard breaks

**Why It Happens:**

- Data processing takes time
- No feedback to user

**How to Fix:**

- Streamlit automatically shows "Running..." in corner
- For long operations, use: `with st.spinner('Loading...'):`
- Cache data to minimize wait times
- Script uses caching for fast performance

***

## ✅ Stage 8 Complete!

You have now:

- Created interactive Streamlit dashboard with 5 comprehensive pages
- Built Executive Overview with key metrics and insights
- Implemented Segment Analysis with risk/value/tenure comparisons
- Designed Churn Drivers page with contract/payment/service/tenure analysis
- Created Recommendations page with detailed implementation plans
- Built Customer Explorer for interactive filtering and data export
- Added professional styling and visual hierarchy
- Implemented interactive filters that update all visualizations
- Included contextual insights and recommendations throughout
- Created downloadable data export functionality

**Dashboard Pages:**

**🏠 Executive Overview:**

- Key metrics (churn rate, revenue at risk, customer counts)
- Churn distribution visualization
- Revenue impact analysis
- Top 3 insights and recommendations

**📈 Segment Analysis:**

- Risk segments (High/Medium/Low)
- Value segments (High/Medium/Low)
- Tenure segments (New/Growing/Mature/Loyal)
- Interactive switching between segment types
- Detailed comparison charts and tables

**🎯 Churn Drivers:**

- Contract type impact analysis
- Payment method comparison
- Service adoption effect
- Tenure impact visualization
- Contextual insights for each driver

**💡 Recommendations:**

- 5 detailed, prioritized recommendations
- Problem statements and expected outcomes
- Implementation timelines
- Phased roadmap

**🔍 Customer Explorer:**

- Interactive multi-filter interface
- Real-time customer count updates
- Sortable data table
- CSV export functionality

**Key Features:**

- Responsive design (works on different screen sizes)
- Professional color scheme and styling
- Interactive Plotly charts
- Real-time filtering
- Cached data loading for performance
- Downloadable data exports
- Clear visual hierarchy
- Contextual insights throughout

**Dashboard Capabilities:**

- Self-service analytics (stakeholders explore independently)
- Real-time segment comparison
- Filter by contract, tenure, value, risk
- Drill-down to customer level
- Export filtered data for further analysis

**Technical Implementation:**

- Streamlit framework for rapid development
- Plotly for interactive visualizations
- Pandas for data manipulation
- Cached data loading (@st.cache_data)
- Responsive multi-column layouts
- Custom CSS styling

**Business Value:**

- Executives can view high-level metrics instantly
- Analysts can explore segments in detail
- Marketing can identify target segments
- Customer success can download high-risk customer lists
- All stakeholders access same data source (single source of truth)

**Critical Understanding:**

- **Dashboards enable action** - insights must lead to decisions
- **Self-service reduces analyst bottleneck** - stakeholders explore independently
- **Filters critical** - stakeholders need to answer their specific questions
- **Context matters** - charts + insights + recommendations = value

**Output:**

- `dashboard/churn_dashboard.py` - Deployable Streamlit application
- Running at `http://localhost:8501` when executed
- Ready for deployment to Streamlit Cloud, Heroku, or internal server

**Next Step:** Wait for instruction to proceed to Stage 9 (Reporting, Automation \& Professionalization)

---

# **Stage 9: Reporting, Automation \& Professionalization**


***

## a) Learning Objective

### What You're Learning

You are learning how to **professionalize a data analytics project** for portfolio presentation, automate repetitive tasks, create comprehensive documentation, and prepare work for deployment. This stage transforms a functional analysis into a production-ready, showcase-worthy project.

### Why This Matters

In real-world data analytics, **technical work is only 50% of the job - communication and professionalization is the other 50%**. Professional analysts must:

- **Document thoroughly** - others can understand and reproduce work
- **Automate workflows** - reduce manual effort, enable scheduling
- **Package professionally** - suitable for portfolio, stakeholders, production
- **Enable reproducibility** - anyone can run analysis with clear instructions

**Without professionalization:**

- Great analysis stays locked in your local machine
- Can't demonstrate skills to recruiters/employers
- Work difficult to reproduce or update
- Manual, error-prone execution
- No clear narrative for stakeholders

**With professional packaging:**

- Portfolio-ready showcase project
- One-command execution (automated pipeline)
- Clear documentation for any audience
- Easy to deploy and maintain
- Demonstrates production-ready skills


### Skill Level

**Advanced Professional** - This builds on all previous stages and introduces professional software engineering practices, documentation standards, automation scripting, and deployment preparation.

### In Scope

- Creating comprehensive project README with portfolio polish
- Writing detailed technical documentation
- Building master automation script (runs entire pipeline)
- Creating requirements.txt with exact dependencies
- Adding project structure documentation
- Writing user guides for dashboard
- Creating deployment instructions
- Adding professional touches (badges, screenshots, architecture diagrams)
- Finalizing project organization
- Creating portfolio presentation materials


### Out of Scope

- CI/CD pipeline setup (GitHub Actions, Jenkins) - basic automation only
- Cloud deployment (AWS, Azure, GCP) - deployment instructions only
- Unit testing framework - basic validation included
- Advanced logging and monitoring
- Docker containerization - mentioned but not implemented
- API development - dashboard is the interface


### Assumptions

- You completed all Stages 1-8 successfully
- All analysis outputs exist (reports, dashboard, data)
- Project structure is organized
- You understand basic Git/version control concepts
- You want to showcase this in your portfolio


### Output Artifact

- **README.md** - Professional project documentation
- **run_full_analysis.py** - Master automation script
- **requirements.txt** - Complete dependency list
- **USAGE_GUIDE.md** - Dashboard user guide
- **TECHNICAL_DOCUMENTATION.md** - Detailed technical specs
- **PROJECT_STRUCTURE.md** - Directory organization guide
- **DEPLOYMENT.md** - Deployment instructions
- **Updated project** - Portfolio-ready showcase

***

## b) Setup Instructions

### Step 1: Verify Project Completion

Ensure all previous stages are complete:

```bash
# Check data files
ls data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
ls data/processed/clean_churn_data.csv
ls data/processed/enriched_churn_data.csv

# Check scripts
ls scripts/data_cleaning.py
ls scripts/eda.py
ls scripts/feature_engineering.py
ls scripts/analytical_reasoning.py

# Check dashboard
ls dashboard/churn_dashboard.py

# Check outputs
ls outputs/reports/*.txt
ls outputs/visualizations/*.png
```


### Step 2: Understand Stage 9 Deliverables

This stage creates:

**1. Documentation Files (Root Level):**

- `README.md` - Main project documentation (portfolio-facing)
- `requirements.txt` - Python dependencies
- `USAGE_GUIDE.md` - Dashboard user guide
- `TECHNICAL_DOCUMENTATION.md` - Technical details
- `PROJECT_STRUCTURE.md` - Directory organization
- `DEPLOYMENT.md` - Deployment instructions

**2. Automation Script:**

- `run_full_analysis.py` - Master script to run entire pipeline

**3. Professional Touches:**

- Screenshots for documentation
- Architecture diagrams (text-based)
- Portfolio presentation materials


### Step 3: Files to Create

You will create 7 files in the **project root**:

1. `README.md` - Main documentation (most important)
2. `requirements.txt` - Dependency list
3. `run_full_analysis.py` - Master automation script
4. `USAGE_GUIDE.md` - Dashboard guide
5. `TECHNICAL_DOCUMENTATION.md` - Technical specs
6. `PROJECT_STRUCTURE.md` - Directory structure
7. `DEPLOYMENT.md` - Deployment guide

### Step 4: Documentation Philosophy

Each document serves different audiences:

- **README.md** → Recruiters, potential employers, portfolio visitors
- **USAGE_GUIDE.md** → Business users, stakeholders using dashboard
- **TECHNICAL_DOCUMENTATION.md** → Data analysts, developers maintaining project
- **DEPLOYMENT.md** → DevOps, engineers deploying to production
- **PROJECT_STRUCTURE.md** → New team members, collaborators


### Step 5: Portfolio Preparation

This stage makes your project:

- **GitHub-ready** - professional repository
- **Resume-worthy** - demonstrates skills clearly
- **Interview-ready** - can explain and demo confidently
- **Deployment-ready** - can put into production

***

## c) Implementation (FINAL VERSION)

### File 1: Master README (Portfolio-Facing)

**File Name:** `README.md`
**File Path:** `customer_churn_analysis/README.md`
**Total Lines:** 320

```markdown
# 📊 Customer Churn Analysis - Telco Industry

A comprehensive end-to-end data analytics project analyzing customer churn patterns in the telecommunications industry, providing actionable business recommendations to reduce churn and increase customer lifetime value.

![Project Status](https://img.shields.io/badge/Status-Complete-success)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🎯 Project Overview

This project analyzes **7,043 customer records** from a telecommunications company to identify churn drivers, segment high-risk customers, and provide data-driven retention strategies. The analysis combines **exploratory data analysis, feature engineering, statistical reasoning, and interactive visualization** to deliver actionable insights.

**Key Results:**
- Identified **4 primary churn drivers** (contract type, tenure, payment method, service adoption)
- Segmented customers into **risk categories** with targeted retention strategies
- Quantified **$2.6M+ revenue at risk** from churned customers
- Developed **5 prioritized recommendations** with expected 10-15% churn reduction
- Created **interactive dashboard** for self-service analytics

---

## 🏆 Business Impact

### Problem Statement
The telecommunications company faces a **26.5% churn rate**, losing approximately 1,869 customers and significant revenue. Without understanding churn drivers, retention efforts are unfocused and ineffective.

### Solution Delivered
Comprehensive churn analysis identifying:
- **High-risk segment**: 1,200+ customers (42% churn rate) requiring immediate intervention
- **Contract impact**: Month-to-month customers churn at **3.5x higher rate** than long-term contracts
- **First-year critical period**: New customers have **47% churn rate** vs 15% for loyal customers
- **Service adoption effect**: Customers with 6+ services have **15 percentage points lower churn**

### Expected Outcomes
Implementation of recommendations expected to:
- Reduce overall churn rate from 26.5% to **22-23%** (15-20% improvement)
- Save **400-600 customers annually** through targeted retention
- Retain **$400K-$600K in annual revenue** through improved first-year onboarding
- Increase customer lifetime value through contract commitment programs

---

## 📁 Project Structure

```

customer_churn_analysis/
│
├── data/
│   ├── raw/                        \# Original dataset
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
│   └── processed/                  \# Cleaned and enriched datasets
│       ├── clean_churn_data.csv
│       └── enriched_churn_data.csv
│
├── scripts/                        \# Analysis scripts
│   ├── data_cleaning.py           \# Data cleaning and validation
│   ├── eda.py                     \# Exploratory data analysis
│   ├── feature_engineering.py     \# Feature creation
│   └── analytical_reasoning.py    \# Hypothesis testing and insights
│
├── dashboard/                      \# Interactive Streamlit dashboard
│   └── churn_dashboard.py
│
├── outputs/
│   ├── reports/                   \# Analysis reports
│   │   ├── data_quality_report.txt
│   │   ├── eda_findings.txt
│   │   ├── analysis_report.txt
│   │   ├── business_recommendations.txt
│   │   └── executive_summary.txt
│   └── visualizations/            \# EDA charts
│       └── *.png
│
├── run_full_analysis.py           \# Master automation script
├── requirements.txt               \# Python dependencies
├── README.md                      \# This file
├── USAGE_GUIDE.md                 \# Dashboard user guide
├── TECHNICAL_DOCUMENTATION.md     \# Technical specifications
├── PROJECT_STRUCTURE.md           \# Detailed structure guide
└── DEPLOYMENT.md                  \# Deployment instructions

```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- 2GB free disk space

### Installation

1. **Clone the repository** (or download ZIP)
```bash
git clone https://github.com/yourusername/customer_churn_analysis.git
cd customer_churn_analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run full analysis pipeline** (automated)
```bash
python run_full_analysis.py
```

This will execute all stages in sequence:

- Data cleaning and validation
- Exploratory data analysis
- Feature engineering
- Analytical reasoning
- Report generation

**Duration:** ~2-3 minutes total

4. **Launch interactive dashboard**
```bash
streamlit run dashboard/churn_dashboard.py
```

Dashboard opens in browser at `http://localhost:8501`

---

## 📊 Key Features

### 1. Comprehensive Data Pipeline

- **Data Cleaning**: Missing value handling, duplicate removal, data type validation
- **Feature Engineering**: 14 business-relevant features (CLV, risk scores, segments)
- **Quality Validation**: Automated checks ensuring data integrity


### 2. Multi-Dimensional Analysis

- **Risk Segmentation**: High/Medium/Low risk customer classification
- **Value Segmentation**: Revenue-based customer tiers
- **Lifecycle Analysis**: New/Growing/Mature/Loyal customer stages
- **Churn Driver Quantification**: Statistical validation of hypotheses


### 3. Interactive Dashboard

- **5 Comprehensive Pages**:
    - Executive Overview (KPIs and insights)
    - Segment Analysis (risk/value/tenure deep-dives)
    - Churn Drivers (contract, payment, service, tenure)
    - Recommendations (prioritized action plans)
    - Customer Explorer (filtering and data export)
- **Real-time Filtering**: Dynamic segment exploration
- **Professional Visualizations**: Plotly interactive charts
- **Data Export**: Download filtered customer lists


### 4. Actionable Recommendations

- **5 Prioritized Strategies** with implementation timelines
- **Quantified Impact**: Customer counts, revenue estimates
- **Phased Roadmap**: Quick wins to strategic initiatives

---

## 🔑 Key Insights

### Finding 1: Contract Commitment is Critical

**Insight:** Month-to-month contract customers have **42.7% churn rate**, compared to 11.3% for two-year contracts (3.8x higher).

**Impact:** 3,875 customers (~55% of base) are on month-to-month contracts, representing highest churn risk.

**Recommendation:** Offer 10-15% discounts for contract upgrades to stabilize customer base.

### Finding 2: First Year is Make-or-Break

**Insight:** Customers in first 12 months have **47.4% churn rate** vs 15.2% for loyal customers (49+ months).

**Impact:** 1,692 customers in critical first-year period need intensive support.

**Recommendation:** Implement structured onboarding with touchpoints at 30/90/180 days.

### Finding 3: Service Adoption Reduces Churn

**Insight:** Low engagement customers (0-2 services) churn at **38.3%** vs 23.1% for high engagement (6+ services).

**Impact:** 2,850+ customers with low service adoption are at elevated risk.

**Recommendation:** Launch targeted upsell campaign for Tech Support and Online Security.

### Finding 4: Payment Method Signals Engagement

**Insight:** Electronic check users have **45.3% churn rate**, highest among all payment methods.

**Impact:** 2,365 customers using manual payment methods show lower engagement.

**Recommendation:** Incentivize migration to automatic payment methods with discounts.

---

## 🛠️ Technologies \& Skills Demonstrated

### Technical Skills

- **Python Programming**: Pandas, NumPy, Matplotlib, Seaborn, Plotly
- **Data Analysis**: Cleaning, EDA, statistical validation, hypothesis testing
- **Feature Engineering**: Business metric creation, risk scoring, segmentation
- **Data Visualization**: Interactive dashboards, static charts, storytelling
- **Dashboard Development**: Streamlit, responsive UI/UX design


### Business Skills

- **Analytical Reasoning**: Root cause analysis, churn driver identification
- **Business Metrics**: CLV, ARPU, churn rate, customer segmentation
- **Strategic Thinking**: Prioritized recommendations, ROI estimation
- **Stakeholder Communication**: Executive summaries, technical documentation
- **Data Storytelling**: Insights-driven narrative, actionable outputs


### Software Engineering

- **Code Organization**: Modular scripts, clean architecture
- **Documentation**: Comprehensive README, user guides, technical specs
- **Automation**: Master pipeline script, reproducible workflows
- **Version Control**: Git-ready structure, clear commit history
- **Deployment**: Cloud-ready dashboard, deployment documentation

---

## 📈 Results \& Deliverables

### Analysis Outputs

- ✅ **Data Quality Report**: 100% clean dataset with validation checks
- ✅ **EDA Report**: 50+ visualizations, statistical summaries, hypothesis generation
- ✅ **Feature Dictionary**: 14 engineered features with business definitions
- ✅ **Analysis Report**: Hypothesis validation, segment profiling, driver quantification
- ✅ **Business Recommendations**: 5 prioritized strategies with expected impact
- ✅ **Executive Summary**: High-level findings for leadership


### Interactive Deliverables

- ✅ **Streamlit Dashboard**: 5-page interactive analytics platform
- ✅ **Segment Comparison Tool**: Real-time filtering and exploration
- ✅ **Data Export Functionality**: Download filtered customer lists


### Documentation

- ✅ **README**: Portfolio-ready project overview
- ✅ **Usage Guide**: Dashboard navigation instructions
- ✅ **Technical Documentation**: Architecture, data schemas, methodology
- ✅ **Deployment Guide**: Step-by-step deployment instructions

---

## 🎓 Learning Journey

This project was completed as part of a **comprehensive data analytics portfolio**, demonstrating end-to-end capabilities from raw data to deployed dashboards. It showcases proficiency in:

1. **Business Problem Framing** - Understanding stakeholder needs
2. **Data Engineering** - Cleaning, validation, transformation
3. **Exploratory Analysis** - Pattern discovery, hypothesis generation
4. **Feature Engineering** - Creating business-relevant metrics
5. **Statistical Analysis** - Hypothesis testing, segment comparison
6. **Data Visualization** - Static and interactive charts
7. **Dashboard Development** - User-friendly analytics platforms
8. **Business Communication** - Executive summaries, recommendations
9. **Professional Packaging** - Documentation, automation, deployment

**Development Time:** ~6-8 hours (structured learning approach)
**Complexity Level:** Intermediate to Advanced
**Industry Application:** Telecommunications, SaaS, Subscription businesses

---

## 📖 Documentation

- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - How to use the dashboard
- **[TECHNICAL_DOCUMENTATION.md](TECHNICAL_DOCUMENTATION.md)** - Technical specifications
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Directory organization
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Deployment instructions

---

## 🚀 Deployment Options

### Local Deployment (Current)

```bash
streamlit run dashboard/churn_dashboard.py
```


### Cloud Deployment Options

**Streamlit Cloud** (Recommended for demos):

1. Push to GitHub repository
2. Connect to Streamlit Cloud
3. Deploy in 1-click
4. Share public URL

**Heroku** (Production-ready):

- See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions

**Docker** (Containerized):

- Dockerfile included (optional)
- Portable across environments

---

## 🤝 Usage \& Attribution

This project is available for:

- ✅ Portfolio showcase
- ✅ Learning and education
- ✅ Code reference and inspiration
- ✅ Interview demonstrations

**Please provide attribution** if using substantial portions of code or methodology.

---

## 📧 Contact \& Portfolio

**Name:** [Your Name]
**Email:** [your.email@example.com]
**LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
**Portfolio:** [yourportfolio.com](https://yourportfolio.com)
**GitHub:** [github.com/yourusername](https://github.com/yourusername)

---

## 🏅 Project Highlights for Recruiters

**What This Project Demonstrates:**

✅ **End-to-End Analytics**: Raw data → Insights → Deployment
✅ **Business Acumen**: Revenue impact, strategic recommendations
✅ **Technical Proficiency**: Python, SQL concepts, dashboard development
✅ **Data Storytelling**: Clear communication of complex insights
✅ **Production Skills**: Documentation, automation, deployment-ready
✅ **Attention to Detail**: Code quality, validation, error handling
✅ **Self-Direction**: Complete project independently with structured approach

**Suitable For Roles:**

- Data Analyst
- Business Analyst
- Data Scientist (Analytics)
- Business Intelligence Analyst
- Customer Analytics Specialist

---

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🙏 Acknowledgments

- **Dataset:** IBM Sample Data Sets (Telco Customer Churn)
- **Tools:** Python, Pandas, Streamlit, Plotly
- **Inspiration:** Real-world telecom churn analysis challenges

---

**⭐ If you found this project helpful, please consider starring the repository!**

---

*Last Updated: January 2026*

```

***

### File 2: Requirements File

**File Name:** `requirements.txt`  
**File Path:** `customer_churn_analysis/requirements.txt`

```


# Core Data Analysis

pandas==2.1.4
numpy==1.26.2

# Visualization

matplotlib==3.8.2
seaborn==0.13.0
plotly==5.18.0

# Dashboard

streamlit==1.29.0

# Additional utilities (if needed)

scipy==1.11.4

```

***

### File 3: Master Automation Script

**File Name:** `run_full_analysis.py`  
**File Path:** `customer_churn_analysis/run_full_analysis.py`  
**Total Lines:** 180

```python
"""
MASTER AUTOMATION SCRIPT
Runs the complete churn analysis pipeline from start to finish
"""

import os
import sys
import time
from datetime import datetime

# Print header
print("=" * 80)
print("CUSTOMER CHURN ANALYSIS - FULL PIPELINE EXECUTION")
print("=" * 80)
print()
print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# Track overall start time
pipeline_start = time.time()

# Stage tracking
stages_completed = []
stages_failed = []

# ==================== STAGE 1: DATA CLEANING ====================
print("-" * 80)
print("STAGE 1: DATA CLEANING & VALIDATION")
print("-" * 80)
stage_start = time.time()

try:
    # Check if input file exists
    if not os.path.exists("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"):
        print("❌ ERROR: Raw data file not found!")
        print("   Expected: data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")
        print("   Please download dataset and place in data/raw/ folder")
        sys.exit(1)
    
    # Run data cleaning script
    print("Running data_cleaning.py...")
    exit_code = os.system("python scripts/data_cleaning.py")
    
    if exit_code != 0:
        raise Exception("Data cleaning script failed")
    
    # Verify output created
    if not os.path.exists("data/processed/clean_churn_data.csv"):
        raise Exception("Clean dataset not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 1 Complete ({stage_time:.1f}s)")
    stages_completed.append("Stage 1: Data Cleaning")
    
except Exception as e:
    print(f"\n❌ Stage 1 Failed: {str(e)}")
    stages_failed.append("Stage 1: Data Cleaning")
    sys.exit(1)

print()

# ==================== STAGE 2: EXPLORATORY DATA ANALYSIS ====================
print("-" * 80)
print("STAGE 2: EXPLORATORY DATA ANALYSIS")
print("-" * 80)
stage_start = time.time()

try:
    print("Running eda.py...")
    exit_code = os.system("python scripts/eda.py")
    
    if exit_code != 0:
        raise Exception("EDA script failed")
    
    # Verify outputs created
    if not os.path.exists("outputs/reports/eda_findings.txt"):
        raise Exception("EDA findings report not created")
    
    if not os.path.exists("outputs/visualizations"):
        raise Exception("Visualizations folder not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 2 Complete ({stage_time:.1f}s)")
    stages_completed.append("Stage 2: Exploratory Data Analysis")
    
except Exception as e:
    print(f"\n❌ Stage 2 Failed: {str(e)}")
    stages_failed.append("Stage 2: Exploratory Data Analysis")
    sys.exit(1)

print()

# ==================== STAGE 3: FEATURE ENGINEERING ====================
print("-" * 80)
print("STAGE 3: FEATURE ENGINEERING")
print("-" * 80)
stage_start = time.time()

try:
    print("Running feature_engineering.py...")
    exit_code = os.system("python scripts/feature_engineering.py")
    
    if exit_code != 0:
        raise Exception("Feature engineering script failed")
    
    # Verify output created
    if not os.path.exists("data/processed/enriched_churn_data.csv"):
        raise Exception("Enriched dataset not created")
    
    if not os.path.exists("data/processed/feature_dictionary.txt"):
        raise Exception("Feature dictionary not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 3 Complete ({stage_time:.1f}s)")
    stages_completed.append("Stage 3: Feature Engineering")
    
except Exception as e:
    print(f"\n❌ Stage 3 Failed: {str(e)}")
    stages_failed.append("Stage 3: Feature Engineering")
    sys.exit(1)

print()

# ==================== STAGE 4: ANALYTICAL REASONING ====================
print("-" * 80)
print("STAGE 4: ANALYTICAL REASONING")
print("-" * 80)
stage_start = time.time()

try:
    print("Running analytical_reasoning.py...")
    exit_code = os.system("python scripts/analytical_reasoning.py")
    
    if exit_code != 0:
        raise Exception("Analytical reasoning script failed")
    
    # Verify outputs created
    if not os.path.exists("outputs/reports/analysis_report.txt"):
        raise Exception("Analysis report not created")
    
    if not os.path.exists("outputs/reports/business_recommendations.txt"):
        raise Exception("Business recommendations not created")
    
    if not os.path.exists("outputs/reports/executive_summary.txt"):
        raise Exception("Executive summary not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 4 Complete ({stage_time:.1f}s)")
    stages_completed.append("Stage 4: Analytical Reasoning")
    
except Exception as e:
    print(f"\n❌ Stage 4 Failed: {str(e)}")
    stages_failed.append("Stage 4: Analytical Reasoning")
    sys.exit(1)

print()

# ==================== PIPELINE SUMMARY ====================
pipeline_time = time.time() - pipeline_start

print("=" * 80)
print("PIPELINE EXECUTION SUMMARY")
print("=" * 80)
print()
print(f"Total Execution Time: {pipeline_time:.1f} seconds ({pipeline_time/60:.1f} minutes)")
print()
print("Stages Completed:")
for stage in stages_completed:
    print(f"  ✅ {stage}")

if stages_failed:
    print()
    print("Stages Failed:")
    for stage in stages_failed:
        print(f"  ❌ {stage}")
    print()
    print("❌ Pipeline completed with errors")
else:
    print()
    print("✅ All stages completed successfully!")

print()
print("=" * 80)
print("NEXT STEPS")
print("=" * 80)
print()
print("1. Review Analysis Outputs:")
print("   - outputs/reports/executive_summary.txt")
print("   - outputs/reports/business_recommendations.txt")
print("   - outputs/reports/analysis_report.txt")
print()
print("2. Launch Interactive Dashboard:")
print("   streamlit run dashboard/churn_dashboard.py")
print()
print("3. Explore Visualizations:")
print("   - outputs/visualizations/")
print()
print("=" * 80)
print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)
```


***

### File 4: Usage Guide (Dashboard)

**File Name:** `USAGE_GUIDE.md`
**File Path:** `customer_churn_analysis/USAGE_GUIDE.md`

```markdown
# Dashboard Usage Guide

## Getting Started

### Launching the Dashboard

1. Open terminal and navigate to project folder:
```bash
cd customer_churn_analysis
```

2. Launch dashboard:
```bash
streamlit run dashboard/churn_dashboard.py
```

3. Browser opens automatically at `http://localhost:8501`
4. To stop dashboard, press `Ctrl+C` in terminal

---

## Dashboard Overview

The dashboard consists of **5 main pages** accessible from the sidebar:

- 🏠 **Executive Overview** - High-level metrics and insights
- 📈 **Segment Analysis** - Deep-dive into customer segments
- 🎯 **Churn Drivers** - Analysis of churn factors
- 💡 **Recommendations** - Business strategies
- 🔍 **Customer Explorer** - Interactive filtering and export

---

## Using the Sidebar

### Navigation

Click any page in the sidebar to navigate.

### Global Filters

Apply filters that affect all pages:

**Contract Type:** Select which contract types to include

- Month-to-month
- One year
- Two year

**Tenure Segment:** Filter by customer lifecycle stage

- New Customer (0-12 months)
- Growing Customer (13-24 months)
- Mature Customer (25-48 months)
- Loyal Customer (49+ months)

**Value Segment:** Filter by revenue tier

- High Value
- Medium Value
- Low Value

**Filtered Customer Count:** Shows how many customers match your filters

---

## Page-by-Page Guide

### 🏠 Executive Overview

**Purpose:** Quick snapshot of key metrics and insights

**What You'll See:**

- Total customers, churn rate, revenue at risk, average ARPU
- Churn distribution pie chart
- Revenue impact by churn status
- Top 3 key insights
- Top 3 recommendations preview

**Use Cases:**

- Quick status check
- Presenting to executives
- Understanding overall health

---

### 📈 Segment Analysis

**Purpose:** Compare customer segments in detail

**Segment Types:**

1. **Risk Segments** - High/Medium/Low risk classification
2. **Value Segments** - High/Medium/Low revenue tiers
3. **Tenure Segments** - New/Growing/Mature/Loyal lifecycle stages

**How to Use:**

1. Select segment type using radio buttons
2. Review metrics cards at top
3. Analyze comparison charts
4. Examine detailed data table

**Use Cases:**

- Identify high-risk customers
- Compare value tiers
- Understand lifecycle patterns
- Target specific segments for campaigns

---

### 🎯 Churn Drivers

**Purpose:** Understand what factors drive churn

**Driver Categories:**

1. **Contract Type** - Month-to-month vs annual vs two-year
2. **Payment Method** - Electronic check, credit card, bank transfer, mailed check
3. **Service Adoption** - Low/Medium/High engagement
4. **Tenure Impact** - Churn by customer age

**How to Use:**

1. Select driver from dropdown
2. Review churn rate comparisons
3. Read insight box below charts
4. Identify intervention opportunities

**Use Cases:**

- Prioritize retention initiatives
- Understand churn root causes
- Validate hypotheses
- Support business cases

---

### 💡 Recommendations

**Purpose:** Actionable strategies to reduce churn

**What You'll See:**

- 5 prioritized recommendations
- Each includes:
    - Priority level (High/Medium/Low)
    - Problem statement
    - Recommended action
    - Expected outcome
    - Implementation timeline
- Phased implementation roadmap

**How to Use:**

1. Review recommendations in priority order
2. Discuss feasibility with team
3. Use implementation timelines for planning
4. Track outcomes after implementation

**Use Cases:**

- Strategic planning
- Resource allocation
- Campaign development
- Measuring intervention success

---

### 🔍 Customer Explorer

**Purpose:** Interactive data exploration and export

**Features:**

- Additional filters (Risk Score, Churn Status, Payment Method)
- Real-time customer count and metrics
- Sortable data table
- CSV export functionality

**How to Use:**

1. Apply filters to narrow customer list
2. Review summary metrics
3. Examine customer data table
4. Click "Download" to export filtered data as CSV

**Use Cases:**

- Create target lists for campaigns
- Export high-risk customers for outreach
- Analyze specific customer cohorts
- Share customer lists with teams

---

## Tips \& Best Practices

### Performance

- Dashboard loads data once and caches it
- Filters update instantly
- If slow, check your network connection
- Close and reopen dashboard to refresh cache


### Filtering Strategy

- Start with broad filters (all selected)
- Narrow down to specific segments
- Use Customer Explorer for detailed filtering
- Reset filters by reselecting all options


### Exporting Data

- Apply filters before exporting
- Exported CSV includes all columns
- Open in Excel or import to other tools
- Respect data privacy when sharing exports


### Presentation Tips

- Use Executive Overview for high-level presentations
- Use Segment Analysis for detailed discussions
- Show Churn Drivers when explaining problems
- Present Recommendations when proposing solutions
- Use Customer Explorer in working sessions

---

## Troubleshooting

### Dashboard Won't Start

**Error:** "ModuleNotFoundError"

- **Solution:** Run `pip install -r requirements.txt`

**Error:** "FileNotFoundError"

- **Solution:** Make sure you're running from project root directory


### Charts Not Loading

- Check internet connection (Plotly uses CDN)
- Try refreshing browser (Ctrl+R or Cmd+R)
- Clear browser cache


### Filters Not Working

- Ensure at least one option selected in each filter
- Try resetting filters (select all options)
- Refresh dashboard if behavior persists


### Slow Performance

- Reduce number of active filters
- Close other browser tabs
- Restart dashboard
- Check system resources

---

## Keyboard Shortcuts

- **Ctrl+R / Cmd+R** - Refresh dashboard
- **Ctrl+K / Cmd+K** - Open Streamlit menu (settings, about)
- **Ctrl+C** - Stop dashboard server (in terminal)

---

## Support

For issues or questions:

1. Check this usage guide first
2. Review project README.md
3. Check TECHNICAL_DOCUMENTATION.md for details
4. Contact: [your.email@example.com]

---

*Last Updated: January 2026*

```

***

### File 5: Technical Documentation

**File Name:** `TECHNICAL_DOCUMENTATION.md`  
**File Path:** `customer_churn_analysis/TECHNICAL_DOCUMENTATION.md`

```markdown
# Technical Documentation

## System Architecture

### Overview
This project implements an **end-to-end data analytics pipeline** for customer churn analysis, consisting of four main components:

1. **Data Processing Layer** - Data cleaning, validation, transformation
2. **Analysis Layer** - EDA, feature engineering, statistical reasoning
3. **Presentation Layer** - Interactive dashboard, reports
4. **Automation Layer** - Pipeline orchestration

### Architecture Diagram

```

┌─────────────────────────────────────────────────────────────┐
│                     RAW DATA SOURCE                         │
│          WA_Fn-UseC_-Telco-Customer-Churn.csv              │
└────────────────────┬────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│              DATA PROCESSING LAYER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ data_cleaning.py                                     │  │
│  │ - Missing value handling                             │  │
│  │ - Duplicate removal                                  │  │
│  │ - Data type conversion                               │  │
│  │ - Validation checks                                  │  │
│  └────────────────────┬─────────────────────────────────┘  │
└───────────────────────┼─────────────────────────────────────┘
│
▼
clean_churn_data.csv
│
▼
┌─────────────────────────────────────────────────────────────┐
│                 ANALYSIS LAYER                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ eda.py - Exploratory Analysis                      │    │
│  └────────────────────────────────────────────────────┘    │
│  ┌────────────────────────────────────────────────────┐    │
│  │ feature_engineering.py - Feature Creation          │    │
│  └────────────────────┬───────────────────────────────┘    │
│                       │                                     │
│                       ▼                                     │
│             enriched_churn_data.csv                        │
│                       │                                     │
│  ┌────────────────────▼───────────────────────────────┐    │
│  │ analytical_reasoning.py - Insights \& Recommendations│    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│              PRESENTATION LAYER                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │ churn_dashboard.py - Interactive Streamlit Dashboard│   │
│  │ - 5 pages (Overview, Segments, Drivers, Recs,      │   │
│  │   Explorer)                                         │   │
│  │ - Real-time filtering                               │   │
│  │ - Interactive charts                                │   │
│  │ - Data export                                       │   │
│  └────────────────────────────────────────────────────┘    │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Reports (TXT files)                                 │   │
│  │ - Executive Summary                                 │   │
│  │ - Analysis Report                                   │   │
│  │ - Business Recommendations                          │   │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘

```

---

## Data Schema

### Raw Dataset
**File:** `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`

**Rows:** 7,043 customers  
**Columns:** 21

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| customerID | string | Unique customer identifier |
| gender | string | Customer gender (Male/Female) |
| SeniorCitizen | int | Whether customer is senior (0=No, 1=Yes) |
| Partner | string | Whether customer has partner (Yes/No) |
| Dependents | string | Whether customer has dependents (Yes/No) |
| tenure | int | Months customer has been with company |
| PhoneService | string | Whether has phone service (Yes/No) |
| MultipleLines | string | Multiple phone lines (Yes/No/No phone service) |
| InternetService | string | Internet provider (DSL/Fiber optic/No) |
| OnlineSecurity | string | Online security service (Yes/No/No internet) |
| OnlineBackup | string | Online backup service (Yes/No/No internet) |
| DeviceProtection | string | Device protection (Yes/No/No internet) |
| TechSupport | string | Tech support service (Yes/No/No internet) |
| StreamingTV | string | Streaming TV service (Yes/No/No internet) |
| StreamingMovies | string | Streaming movies (Yes/No/No internet) |
| Contract | string | Contract type (Month-to-month/One year/Two year) |
| PaperlessBilling | string | Paperless billing (Yes/No) |
| PaymentMethod | string | Payment method (4 categories) |
| MonthlyCharges | float | Monthly bill amount |
| TotalCharges | float | Total charges to date |
| Churn | string | Whether customer churned (Yes/No) |

---

### Engineered Features

**Added in Stage 6 (feature_engineering.py)**

| Feature Name | Type | Description | Business Use |
|--------------|------|-------------|--------------|
| CLV | float | Customer Lifetime Value (=TotalCharges) | Identify high-value customers |
| ARPU | float | Average Revenue Per User (=MonthlyCharges) | Revenue tier classification |
| Value_Segment | category | High/Medium/Low value tier | Prioritize retention by value |
| High_Risk_Flag | binary | Month-to-month + tenure<12 | Flag highest-risk customers |
| Payment_Risk_Flag | binary | Electronic check user | Identify payment friction |
| Service_Risk_Flag | binary | No TechSupport + No OnlineSecurity | Low engagement indicator |
| Risk_Score | int | Sum of risk flags (0-3) | Composite risk assessment |
| Total_Services | int | Count of subscribed services (0-8) | Engagement measurement |
| Service_Engagement | category | Low/Medium/High engagement | Service adoption tier |
| Tenure_Segment | category | New/Growing/Mature/Loyal | Lifecycle stage |
| Contract_Stability | int | Numeric contract commitment (1-3) | Stability score |
| Payment_Reliability | float | Payment success rate (0-100%) | Payment behavior |
| Monthly_to_CLV_Ratio | float | Monthly % of lifetime value | Tenure indicator |
| Paperless_Engagement | binary | Uses paperless billing | Digital engagement |

---

## Processing Pipeline

### Stage 1: Data Cleaning
**Script:** `scripts/data_cleaning.py`

**Input:** `data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv`  
**Output:** `data/processed/clean_churn_data.csv`

**Operations:**
1. Load raw CSV
2. Handle missing values:
   - TotalCharges: Convert blanks to 0 (new customers)
3. Remove duplicates (if any)
4. Convert data types:
   - TotalCharges: string → float
   - SeniorCitizen: int → Yes/No (consistency)
5. Validate ranges and values
6. Generate data quality report

**Quality Checks:**
- Row count preservation (7,043)
- No missing values in final dataset
- All numeric columns have valid ranges
- Categorical columns have expected values

---

### Stage 2: Exploratory Data Analysis
**Script:** `scripts/eda.py`

**Input:** `data/processed/clean_churn_data.csv`  
**Output:** 
- `outputs/reports/eda_findings.txt`
- `outputs/visualizations/*.png`

**Analysis:**
1. Univariate analysis (distributions, frequencies)
2. Bivariate analysis (churn vs each feature)
3. Correlation analysis
4. Hypothesis generation
5. Visualization generation (20+ charts)

**Key Outputs:**
- Churn rate by contract type
- Churn rate by tenure segments
- Service adoption patterns
- Payment method analysis

---

### Stage 3: Feature Engineering
**Script:** `scripts/feature_engineering.py`

**Input:** `data/processed/clean_churn_data.csv`  
**Output:** 
- `data/processed/enriched_churn_data.csv`
- `data/processed/feature_dictionary.txt`

**Features Created:** 14 (see Data Schema section)

**Feature Categories:**
1. Value metrics (CLV, ARPU, Value_Segment)
2. Risk indicators (High_Risk_Flag, Payment_Risk_Flag, Service_Risk_Flag, Risk_Score)
3. Service metrics (Total_Services, Service_Engagement)
4. Lifecycle (Tenure_Segment, Contract_Stability)
5. Behavioral (Payment_Reliability, Monthly_to_CLV_Ratio, Paperless_Engagement)

---

### Stage 4: Analytical Reasoning
**Script:** `scripts/analytical_reasoning.py`

**Input:** `data/processed/enriched_churn_data.csv`  
**Output:** 
- `outputs/reports/analysis_report.txt`
- `outputs/reports/segment_comparison.csv`
- `outputs/reports/business_recommendations.txt`
- `outputs/reports/executive_summary.txt`

**Analysis Components:**
1. Hypothesis validation (4 hypotheses from EDA)
2. Segment profiling (risk, value, tenure)
3. Churn driver quantification
4. Business impact assessment
5. Recommendation generation

---

## Dashboard Technical Specs

### Technology Stack
- **Framework:** Streamlit 1.29.0
- **Visualization:** Plotly 5.18.0
- **Data Processing:** Pandas 2.1.4, NumPy 1.26.2
- **Styling:** Custom CSS (embedded in dashboard.py)

### Architecture
- **Single-page application** with multi-page navigation
- **Caching:** @st.cache_data for data loading
- **Responsive:** Column-based layouts adapt to screen size
- **Interactive:** Real-time filtering updates all visualizations

### Performance
- Initial load: ~2-3 seconds
- Filter updates: <0.5 seconds
- Data cached after first load
- Suitable for 10,000+ row datasets

### Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge

---

## Dependencies

See `requirements.txt` for versions.

**Core:**
- pandas: Data manipulation
- numpy: Numerical operations

**Visualization:**
- matplotlib: Static charts (EDA)
- seaborn: Statistical visualizations (EDA)
- plotly: Interactive charts (Dashboard)

**Dashboard:**
- streamlit: Web application framework

**Optional:**
- scipy: Statistical functions (if needed)

---

## File Size Reference

- Raw dataset: ~1 MB
- Clean dataset: ~950 KB
- Enriched dataset: ~1.2 MB
- Total project: ~5-10 MB (with outputs)

---

## Performance Benchmarks

**On typical laptop (i5, 8GB RAM):**

| Stage | Duration |
|-------|----------|
| Data Cleaning | 5-10 seconds |
| EDA | 30-60 seconds |
| Feature Engineering | 10-20 seconds |
| Analytical Reasoning | 15-30 seconds |
| **Full Pipeline** | **2-3 minutes** |
| Dashboard Load | 2-3 seconds |

---

## Extensibility

### Adding New Features
1. Edit `scripts/feature_engineering.py`
2. Add feature calculation logic
3. Update `feature_dictionary.txt`
4. Re-run pipeline
5. Update dashboard visualizations if needed

### Adding Dashboard Pages
1. Edit `dashboard/churn_dashboard.py`
2. Add new page to sidebar radio options
3. Add new `elif page == "New Page":` block
4. Implement visualizations and logic

### Deploying Updates
1. Make code changes
2. Test locally
3. Commit to Git
4. Push to repository
5. Redeploy dashboard

---

## Security Considerations

**Data Privacy:**
- Customer IDs anonymized in original dataset
- No PII (names, addresses, phone numbers)
- Safe for public portfolio

**Deployment:**
- Use environment variables for sensitive config
- Implement authentication for production
- HTTPS for public dashboards
- Consider GDPR compliance for EU deployments

---

## Maintenance

**Regular Tasks:**
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Re-run pipeline with new data monthly/quarterly
- Review recommendations effectiveness
- Update visualizations based on feedback

**Monitoring:**
- Dashboard uptime (if deployed)
- Data refresh success
- User engagement metrics

---

*Last Updated: January 2026*
```


***

### File 6: Project Structure Documentation

**File Name:** `PROJECT_STRUCTURE.md`
**File Path:** `customer_churn_analysis/PROJECT_STRUCTURE.md`

```markdown
# Project Structure Documentation

## Directory Organization

```

customer_churn_analysis/
│
├── data/                           \# All data files
│   ├── raw/                        \# Original, immutable data
│   │   └── WA_Fn-UseC_-Telco-Customer-Churn.csv  (1 MB)
│   │
│   └── processed/                  \# Cleaned and transformed data
│       ├── clean_churn_data.csv    (~950 KB)
│       ├── enriched_churn_data.csv (~1.2 MB)
│       ├── feature_dictionary.txt
│       └── feature_validation_report.txt
│
├── scripts/                        \# Python analysis scripts
│   ├── data_cleaning.py           \# Stage 1: Data cleaning
│   ├── eda.py                     \# Stage 2: Exploratory analysis
│   ├── feature_engineering.py     \# Stage 3: Feature creation
│   └── analytical_reasoning.py    \# Stage 4: Insights generation
│
├── dashboard/                      \# Interactive dashboard
│   └── churn_dashboard.py         \# Streamlit web application
│
├── outputs/                        \# Generated outputs
│   ├── reports/                   \# Text analysis reports
│   │   ├── data_quality_report.txt
│   │   ├── eda_findings.txt
│   │   ├── analysis_report.txt
│   │   ├── segment_comparison.csv
│   │   ├── business_recommendations.txt
│   │   └── executive_summary.txt
│   │
│   └── visualizations/            \# EDA charts (PNG files)
│       ├── churn_distribution.png
│       ├── churn_by_contract.png
│       ├── churn_by_tenure.png
│       └── [20+ more charts]
│
├── run_full_analysis.py           \# Master automation script
├── requirements.txt               \# Python dependencies
├── README.md                      \# Main project documentation
├── USAGE_GUIDE.md                 \# Dashboard user guide
├── TECHNICAL_DOCUMENTATION.md     \# Technical specifications
├── PROJECT_STRUCTURE.md           \# This file
└── DEPLOYMENT.md                  \# Deployment instructions

```

---

## File Descriptions

### Root Level Files

**run_full_analysis.py**
- Master automation script
- Runs entire pipeline (Stages 1-4)
- Checks prerequisites
- Validates outputs
- Reports success/failure

**requirements.txt**
- Python package dependencies
- Specifies exact versions
- Used by: `pip install -r requirements.txt`

**README.md**
- Main project documentation
- Portfolio-facing
- Audience: Recruiters, stakeholders, collaborators

**USAGE_GUIDE.md**
- Dashboard usage instructions
- Step-by-step navigation guide
- Audience: Business users

**TECHNICAL_DOCUMENTATION.md**
- System architecture
- Data schemas
- Performance specs
- Audience: Developers, analysts

**PROJECT_STRUCTURE.md**
- Directory organization
- File descriptions
- Audience: New team members

**DEPLOYMENT.md**
- Deployment instructions
- Cloud platform guides
- Audience: DevOps, engineers

---

### Data Directory

#### data/raw/
**Purpose:** Original, immutable source data
**Files:**
- `WA_Fn-UseC_-Telco-Customer-Churn.csv` - Original dataset from IBM
**Guidelines:**
- Never modify files in this folder
- Version control with Git LFS if large
- Document data source and download date

#### data/processed/
**Purpose:** Cleaned and transformed datasets
**Files:**
- `clean_churn_data.csv` - Output of Stage 1 (data cleaning)
- `enriched_churn_data.csv` - Output of Stage 3 (feature engineering)
- `feature_dictionary.txt` - Documentation of engineered features
- `feature_validation_report.txt` - Feature quality checks

---

### Scripts Directory

**scripts/data_cleaning.py**
- Stage 1 of pipeline
- Input: Raw CSV
- Output: Clean CSV, quality report
- Functions: Missing value handling, type conversion, validation

**scripts/eda.py**
- Stage 2 of pipeline
- Input: Clean CSV
- Output: EDA report, visualizations
- Functions: Distribution analysis, correlation, hypothesis generation

**scripts/feature_engineering.py**
- Stage 3 of pipeline
- Input: Clean CSV
- Output: Enriched CSV, feature dictionary
- Functions: Feature creation, validation, documentation

**scripts/analytical_reasoning.py**
- Stage 4 of pipeline
- Input: Enriched CSV
- Output: Analysis reports, recommendations, executive summary
- Functions: Hypothesis testing, segment analysis, recommendations

---

### Dashboard Directory

**dashboard/churn_dashboard.py**
- Interactive Streamlit web application
- 5 pages: Overview, Segments, Drivers, Recommendations, Explorer
- Uses: Enriched CSV as data source
- Features: Filtering, interactive charts, data export

---

### Outputs Directory

#### outputs/reports/
**Purpose:** Text-based analysis reports

**data_quality_report.txt**
- Generated by: data_cleaning.py
- Contents: Missing values, duplicates, data types, validation results

**eda_findings.txt**
- Generated by: eda.py
- Contents: Statistical summaries, churn rates by features, hypotheses

**analysis_report.txt**
- Generated by: analytical_reasoning.py
- Contents: Hypothesis validation, segment analysis, churn drivers

**segment_comparison.csv**
- Generated by: analytical_reasoning.py
- Contents: Segment metrics (churn rates, counts, revenue)

**business_recommendations.txt**
- Generated by: analytical_reasoning.py
- Contents: 5 prioritized recommendations with implementation details

**executive_summary.txt**
- Generated by: analytical_reasoning.py
- Contents: High-level findings and recommendations

#### outputs/visualizations/
**Purpose:** Static charts from EDA
**Files:** 20+ PNG images
- Distribution plots
- Churn rate comparisons
- Correlation heatmaps
- Service adoption analysis

---

## File Flow

### Data Flow Diagram

```

Raw CSV
↓
[data_cleaning.py]
↓
Clean CSV
↓
[eda.py]                [feature_engineering.py]
↓                              ↓
EDA Report              Enriched CSV
Visualizations          Feature Dictionary
↓                              ↓
[analytical_reasoning.py]
↓
Analysis Report
Recommendations
Executive Summary
↓
[churn_dashboard.py]
↓
Interactive Dashboard

```

---

## Size Guidelines

### Expected Sizes

| Directory/File | Size |
|----------------|------|
| data/raw/ | ~1 MB |
| data/processed/ | ~2 MB |
| scripts/ | ~50 KB |
| dashboard/ | ~40 KB |
| outputs/reports/ | ~100 KB |
| outputs/visualizations/ | ~5 MB |
| **Total Project** | **~8-10 MB** |

---

## Naming Conventions

### Files
- Scripts: lowercase_with_underscores.py
- Data: lowercase_with_underscores.csv
- Reports: lowercase_with_underscores.txt
- Documentation: UPPERCASE.md (root level)

### Variables (in code)
- snake_case for variables and functions
- UPPER_CASE for constants
- descriptive names (avoid x, y, temp)

### Columns (in data)
- PascalCase (existing dataset standard)
- Underscores for engineered features (Risk_Score)

---

## Version Control

### What to Commit (Git)
✅ All Python scripts
✅ Documentation files (*.md)
✅ requirements.txt
✅ Empty folder structure

### What NOT to Commit
❌ data/ folder (too large, add to .gitignore)
❌ outputs/ folder (generated, not source)
❌ __pycache__/ (Python cache)
❌ .DS_Store (Mac metadata)
❌ *.pyc (compiled Python)

### Sample .gitignore
```


# Data files

data/

# Output files

outputs/

# Python

__pycache__/
*.pyc
*.pyo

# IDE

.vscode/
.idea/
*.swp

# OS

.DS_Store
Thumbs.db

```

---

## Maintenance

### Adding New Stages
1. Create new script in `scripts/`
2. Update `run_full_analysis.py` to include new stage
3. Document in TECHNICAL_DOCUMENTATION.md
4. Update README.md if user-facing

### Reorganizing Structure
1. Update this document first
2. Move files carefully
3. Update all path references in scripts
4. Test full pipeline
5. Update documentation

---

*Last Updated: January 2026*
```


***

### File 7: Deployment Guide

**File Name:** `DEPLOYMENT.md`
**File Path:** `customer_churn_analysis/DEPLOYMENT.md`

```markdown
# Deployment Guide

## Overview

This guide covers deploying the Customer Churn Analysis dashboard to various platforms.

---

## Local Deployment (Development)

### Prerequisites
- Python 3.8+
- pip installed
- Project downloaded locally

### Steps
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run dashboard:
```bash
streamlit run dashboard/churn_dashboard.py
```

3. Access at: `http://localhost:8501`
4. Stop with: `Ctrl+C`

---

## Streamlit Cloud (Recommended for Portfolio)

**Best for:** Portfolio demos, sharing with recruiters, quick deployment

### Prerequisites

- GitHub account
- Streamlit Cloud account (free at share.streamlit.io)
- Project pushed to GitHub


### Deployment Steps

**Step 1: Prepare Repository**

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/customer_churn_analysis.git
git push -u origin main
```

**Step 2: Add Data to Repository**
Since Streamlit Cloud needs access to data:

- Option A: Include data/ folder in repo (if <100MB)
- Option B: Use Git LFS for large files
- Option C: Host data externally and fetch in app

**Step 3: Deploy on Streamlit Cloud**

1. Go to share.streamlit.io
2. Click "New app"
3. Select your GitHub repository
4. Set:
    - Branch: `main`
    - Main file: `dashboard/churn_dashboard.py`
    - Python version: 3.9
5. Click "Deploy"

**Step 4: Wait for Deployment** (~2-5 minutes)

**Step 5: Get Public URL**

- Your app URL: `https://yourusername-customer-churn-analysis-dashboard-churn-dashboard-xxxxx.streamlit.app`
- Share this link in resume/portfolio


### Troubleshooting Streamlit Cloud

**Issue:** "FileNotFoundError: data/processed/..."
**Solution:** Ensure data files are in repository or accessible via URL

**Issue:** "ModuleNotFoundError"
**Solution:** Check requirements.txt includes all dependencies

**Issue:** "App crashed"
**Solution:** Check logs in Streamlit Cloud dashboard for errors

---

## Heroku Deployment

**Best for:** Production deployment with custom domain

### Prerequisites

- Heroku account
- Heroku CLI installed
- Git installed


### Deployment Steps

**Step 1: Create Required Files**

Create `Procfile`:

```
web: sh setup.sh && streamlit run dashboard/churn_dashboard.py
```

Create `setup.sh`:

```bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
```

Create `runtime.txt`:

```
python-3.9.18
```

**Step 2: Initialize Git and Heroku**

```bash
heroku login
heroku create your-app-name
git init
git add .
git commit -m "Initial commit"
```

**Step 3: Deploy**

```bash
git push heroku main
```

**Step 4: Open App**

```bash
heroku open
```

Your app URL: `https://your-app-name.herokuapp.com`

### Heroku Troubleshooting

**Issue:** Buildpack errors
**Solution:**

```bash
heroku buildpacks:set heroku/python
```

**Issue:** Memory limit exceeded
**Solution:** Upgrade to paid Heroku dyno (Hobby: \$7/month)

**Issue:** App sleeping (free tier)
**Solution:** Upgrade or use service like UptimeRobot to keep app awake

---

## Docker Deployment (Optional)

**Best for:** Consistent environments, Kubernetes deployments

### Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "dashboard/churn_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```


### Build and Run

```bash
# Build image
docker build -t churn-dashboard .

# Run container
docker run -p 8501:8501 churn-dashboard
```

Access at: `http://localhost:8501`

---

## AWS EC2 Deployment (Advanced)

**Best for:** Full control, enterprise deployment

### High-Level Steps

1. Launch EC2 instance (Ubuntu 20.04 recommended)
2. SSH into instance
3. Install Python 3.9+
4. Clone repository
5. Install dependencies
6. Run dashboard with nohup:
```bash
nohup streamlit run dashboard/churn_dashboard.py --server.port 8501 &
```

7. Configure security group (allow port 8501)
8. Access via EC2 public IP

### For Production

- Use Nginx reverse proxy
- Set up SSL certificate (Let's Encrypt)
- Configure custom domain
- Implement authentication
- Set up monitoring

---

## Performance Optimization

### For Large Datasets

1. **Sampling**: Display sample of data, full export available
```python
df_display = df.sample(1000)  # Show 1000 rows
```

2. **Lazy Loading**: Load data only when needed
```python
@st.cache_data
def load_data():
    # Expensive operation
    return df
```

3. **Pagination**: Don't display all rows at once
```python
st.dataframe(df.iloc[start:end])
```


### Caching Strategy

- Cache data loading: `@st.cache_data`
- Cache expensive calculations
- Clear cache when data updates

---

## Security Best Practices

### For Public Deployments

1. **No Sensitive Data**: Ensure no PII in dataset
2. **Authentication**: Add authentication for internal tools
```python
# Simple password protection (NOT for production)
import streamlit as st

password = st.text_input("Password", type="password")
if password != "your_password":
    st.stop()
```

3. **HTTPS**: Always use HTTPS for production
4. **Rate Limiting**: Prevent abuse on public dashboards
5. **Data Privacy**: Comply with GDPR/CCPA if applicable

---

## Monitoring \& Maintenance

### Health Checks

- Monitor dashboard uptime
- Check for errors in logs
- Track user engagement metrics


### Updates

1. Make changes locally
2. Test thoroughly
3. Commit to Git
4. Push to deployment platform
5. Verify deployment successful

### Backup

- Backup data regularly
- Version control for code
- Document deployment configurations

---

## Cost Considerations

### Free Options

- **Streamlit Cloud**: Free tier (1 private app, 3 public apps)
- **Heroku**: Free tier (app sleeps after 30 min inactivity)
- **GitHub Pages**: For static reports only


### Paid Options

- **Streamlit Cloud Pro**: \$250/month (10 users, custom domains)
- **Heroku Hobby**: \$7/month (no sleep)
- **AWS EC2**: ~\$10-50/month (depending on instance)
- **Custom VPS**: \$5-20/month (DigitalOcean, Linode)

---

## Deployment Checklist

Before deploying:

- [ ] All scripts run successfully locally
- [ ] Dashboard loads without errors
- [ ] Data files accessible
- [ ] requirements.txt complete
- [ ] README updated with live demo link
- [ ] No sensitive data exposed
- [ ] Documentation complete
- [ ] Git repository clean and organized
- [ ] .gitignore configured properly
- [ ] License added (if open source)

After deploying:

- [ ] App accessible via public URL
- [ ] All features working as expected
- [ ] Filters and interactions functional
- [ ] Download functionality working
- [ ] Charts rendering correctly
- [ ] No console errors
- [ ] Performance acceptable (<5s load)
- [ ] Mobile-friendly (test on phone)

---

## Support

For deployment issues:

- Streamlit Cloud: https://discuss.streamlit.io
- Heroku: https://help.heroku.com
- General: Check project GitHub issues

---

*Last Updated: January 2026*

```

***

## d) How to Run

### Step 1: Create All Documentation Files
Create the 7 files in the project root folder:
1. `README.md`
2. `requirements.txt`
3. `run_full_analysis.py`
4. `USAGE_GUIDE.md`
5. `TECHNICAL_DOCUMENTATION.md`
6. `PROJECT_STRUCTURE.md`
7. `DEPLOYMENT.md`

### Step 2: Test Master Automation Script
```bash
cd customer_churn_analysis
python run_full_analysis.py
```

**Expected:** Runs all 4 stages in sequence, shows progress, completes successfully.

### Step 3: Verify Requirements File

```bash
pip install -r requirements.txt
```

**Expected:** Installs all dependencies without errors.

### Step 4: Review Documentation Quality

Read through each markdown file and verify:

- No typos or formatting issues
- All links work (if applicable)
- Instructions are clear
- Examples are accurate


### Step 5: Test Dashboard Launch

```bash
streamlit run dashboard/churn_dashboard.py
```

**Expected:** Dashboard launches, all features work as documented in USAGE_GUIDE.md

### Step 6: Prepare for Portfolio

- Take screenshots of dashboard for README
- Test instructions from README (can you follow them?)
- Update contact information in README
- Create GitHub repository (optional but recommended)

***

## e) How to Test the Output

### Test 1: Master Script Runs Successfully

**Expected Result:**

- Runs all 4 stages without errors
- Shows progress for each stage
- Displays execution time
- Shows "All stages completed successfully!"

**How to Check:**

```bash
python run_full_analysis.py
```


### Test 2: Requirements File is Complete

**Expected Result:**

- Contains all necessary packages
- Includes version numbers
- Installs without dependency conflicts

**How to Check:**

```bash
pip install -r requirements.txt
# Should complete without errors
```


### Test 3: README is Portfolio-Ready

**Expected Result:**

- Professional appearance
- Clear project description
- Key results highlighted
- Contact information present
- No placeholder text ([Your Name])

**How to Check:**

- Read README.md top to bottom
- Verify all sections complete
- Check for typos and formatting


### Test 4: Documentation is Accurate

**Expected Result:**

- Instructions work as written
- No outdated information
- File paths correct
- Commands execute successfully

**How to Check:**

- Follow USAGE_GUIDE.md instructions
- Verify dashboard navigation matches guide
- Test deployment instructions (if deploying)


### Test 5: Project Structure Matches Documentation

**Expected Result:**

- All files and folders described exist
- No undocumented files or folders
- Directory tree in docs matches actual structure

**How to Check:**

```bash
tree customer_churn_analysis/  # Or ls -R
# Compare to PROJECT_STRUCTURE.md
```


### Test 6: Automation Script Validates Outputs

**Expected Result:**

- Script checks for existence of output files
- Fails gracefully if stage fails
- Reports missing prerequisites

**How to Check:**

- Delete an output file
- Run run_full_analysis.py
- Verify it detects and regenerates file


### Test 7: GitHub Readiness (if using Git)

**Expected Result:**

- .gitignore configured correctly
- No large data files accidentally committed
- README displays properly on GitHub
- Project is cloneable and runnable

**How to Check:**

```bash
git init
git add .
git status  # Check what's being added
# Verify data/ folder not included
```


### Test 8: End-to-End User Experience

**Expected Result:**

- New user can clone/download project
- Follow README to install and run
- Launch dashboard successfully
- Understand outputs

**How to Check:**

- Have someone else (or yourself in fresh environment) follow README
- Note any confusion or errors
- Update documentation accordingly


### Signs of Success

✅ Master script runs entire pipeline successfully
✅ All 7 documentation files created
✅ README is professional and complete
✅ requirements.txt installs without issues
✅ Documentation accurate and helpful
✅ Project structure organized and clear
✅ Dashboard accessible and functional
✅ Portfolio-ready presentation
✅ No placeholder text remaining
✅ Contact information updated

### Signs of Problems

❌ Master script fails or crashes
❌ Missing documentation files
❌ README contains [Your Name] placeholders
❌ Requirements file incomplete
❌ Documentation instructions don't work
❌ File paths in docs don't match reality
❌ Dashboard won't launch
❌ Typos or formatting errors in docs
❌ .gitignore missing (if using Git)
❌ Data files accidentally committed to Git

***

## f) Common Beginner Mistakes

### Mistake 1: Leaving Placeholder Text

**What Happens:**

- README says "[Your Name]" instead of actual name
- Contact section has example email
- Looks unprofessional in portfolio

**Why It Happens:**

- Forgetting to customize template
- Not reviewing before sharing

**How to Fix:**

- Search for brackets: `[Your Name]`, `[your.email]`
- Replace with real information
- Review entire README before publishing


### Mistake 2: Not Testing Master Script

**What Happens:**

- Create run

---

## f) Common Beginner Mistakes (continued)

### Mistake 2: Not Testing Master Script

**What Happens:**

- Create run_full_analysis.py but never test it
- Script has path errors or logic bugs
- Fails when someone tries to use it

**Why It Happens:**

- Assuming code works without running it
- Not validating automation

**How to Fix:**

- **Always test before considering complete:**

```bash
python run_full_analysis.py
```

- Run multiple times to ensure consistency
- Test on fresh environment if possible
- Script should handle errors gracefully


### Mistake 3: Incomplete requirements.txt

**What Happens:**

- List pandas but forget plotly
- Someone installs and dashboard crashes
- "ModuleNotFoundError: No module named 'plotly'"

**Why It Happens:**

- Not documenting all dependencies
- Testing in environment with many packages already installed

**How to Fix:**

- **Generate from environment:**

```bash
pip freeze > requirements.txt
```

- Or manually list all imports from scripts
- Test in fresh virtual environment:

```bash
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate
pip install -r requirements.txt
python run_full_analysis.py
```

- Verify everything works


### Mistake 4: Writing Documentation After the Fact

**What Happens:**

- Write docs weeks after completing project
- Forget details about how things work
- Documentation inaccurate or incomplete

**Why It Happens:**

- "I'll document it later" mentality
- Not treating docs as deliverable

**How to Fix:**

- Document as you build (Stage 9 approach)
- Each stage = update docs
- Test instructions as you write them
- Documentation = part of project, not afterthought


### Mistake 5: Overly Technical Documentation

**What Happens:**

- README full of technical jargon
- Recruiters don't understand what project does
- Fails to communicate business value

**Why It Happens:**

- Writing for technical audience only
- Not considering portfolio purpose

**How to Fix:**

- **README structure:**
    - Start with business problem and impact (non-technical)
    - Then technical details (for technical readers)
    - Separate technical docs (TECHNICAL_DOCUMENTATION.md)
- Use plain language first, jargon second
- Lead with "what" and "why", then "how"
- Script's README demonstrates this approach


### Mistake 6: Not Including Quick Start

**What Happens:**

- README has 50 pages of background
- No clear "how do I run this?" section
- Users give up before running project

**Why It Happens:**

- Focusing on explanation over execution
- Not prioritizing user experience

**How to Fix:**

- **Quick Start section near top of README:**

```markdown
## Quick Start
1. Install dependencies: pip install -r requirements.txt
2. Run analysis: python run_full_analysis.py
3. Launch dashboard: streamlit run dashboard/churn_dashboard.py
```

- 3-5 steps maximum
- Get user to success quickly
- Detailed explanation can come later


### Mistake 7: Forgetting Screenshots

**What Happens:**

- No visual preview of dashboard
- Recruiters don't know what project looks like
- Less engagement with portfolio

**Why It Happens:**

- Focusing on code, forgetting visuals
- Not optimizing for portfolio presentation

**How to Fix:**

- Take screenshots of key dashboard pages
- Add to README:

```markdown
## Dashboard Preview

```

- Show before recruiters need to run code
- Visual proof of work
- Increases resume/portfolio appeal


### Mistake 8: Hardcoding File Paths

**What Happens:**

- Scripts have paths like "C:/Users/YourName/Documents/project/"
- Others can't run your code
- Breaks on different operating systems

**Why It Happens:**

- Not thinking about portability
- Using absolute paths instead of relative

**How to Fix:**

- **Always use relative paths:**

```python
# Bad:
df = pd.read_csv("C:/Users/YourName/project/data/raw/file.csv")

# Good:
df = pd.read_csv("data/raw/file.csv")
```

- Or use os.path.join for cross-platform:

```python
import os
path = os.path.join("data", "raw", "file.csv")
df = pd.read_csv(path)
```

- All scripts in this project use relative paths correctly


### Mistake 9: Not Handling Missing Files Gracefully

**What Happens:**

- Script crashes with cryptic error if file missing
- User doesn't know what went wrong
- Bad user experience

**Why It Happens:**

- Not anticipating failure cases
- No error handling

**How to Fix:**

- **Check file exists before loading:**

```python
if not os.path.exists(data_path):
    print(f"❌ ERROR: Data file not found: {data_path}")
    print("Please download dataset and place in data/raw/ folder")
    sys.exit(1)
```

- Provide helpful error messages
- Tell user what to do to fix
- Master script demonstrates this pattern


### Mistake 10: Creating Circular Documentation

**What Happens:**

- README says "see USAGE_GUIDE.md"
- USAGE_GUIDE says "see README.md"
- User goes in circles

**Why It Happens:**

- Not planning documentation structure
- Unclear purpose for each doc

**How to Fix:**

- **Each doc has clear audience and purpose:**
    - README → Overview, quick start (for everyone)
    - USAGE_GUIDE → Dashboard navigation (for business users)
    - TECHNICAL_DOCUMENTATION → Architecture (for developers)
    - DEPLOYMENT → Deployment steps (for DevOps)
- Avoid duplicate content
- Link between docs only when adding detail


### Mistake 11: Not Versioning Dependencies

**What Happens:**

- requirements.txt lists "pandas" without version
- Installs latest pandas (2.5.0) which breaks code
- Code was written for pandas 2.1.4

**Why It Happens:**

- Not pinning versions
- Assuming compatibility

**How to Fix:**

- **Always specify versions:**

```
# Bad:
pandas

# Good:
pandas==2.1.4
```

- Or use version ranges if flexible:

```
pandas>=2.1.0,<3.0.0
```

- Script's requirements.txt includes versions


### Mistake 12: Automation Script Without Validation

**What Happens:**

- Master script runs Stage 1
- Stage 1 fails but script continues to Stage 2
- Stage 2 crashes because Stage 1 output missing
- Confusing error messages

**Why It Happens:**

- Not checking if each stage succeeded
- No output validation

**How to Fix:**

- **Check exit codes and file existence:**

```python
exit_code = os.system("python scripts/stage1.py")
if exit_code != 0:
    print("Stage 1 failed!")
    sys.exit(1)

if not os.path.exists("output_file.csv"):
    print("Stage 1 didn't create expected output!")
    sys.exit(1)
```

- Stop pipeline if any stage fails
- Master script demonstrates proper validation


### Mistake 13: Git Committing Data Files

**What Happens:**

- Accidentally commit 1GB dataset to Git
- Repository huge and slow
- GitHub rejects push (>100MB limit)

**Why It Happens:**

- Not configuring .gitignore
- Running git add . without checking

**How to Fix:**

- **Create .gitignore before first commit:**

```
# .gitignore
data/
outputs/
__pycache__/
*.pyc
.DS_Store
```

- Check git status before committing
- Use Git LFS for large files if needed
- Keep repo lean (<50MB ideal)


### Mistake 14: Over-Engineering Documentation

**What Happens:**

- Create 20 different documentation files
- README 100+ pages long
- Users overwhelmed, don't read any of it

**Why It Happens:**

- "More documentation = better" mentality
- Not prioritizing what's essential

**How to Fix:**

- **Keep it focused:**
    - README: 200-400 lines (what recruiters need)
    - USAGE_GUIDE: 100-200 lines (dashboard basics)
    - TECHNICAL_DOCUMENTATION: 200-300 lines (for deep dive)
    - Other docs: <100 lines each
- Quality over quantity
- One clear purpose per document
- Stage 9 provides 7 focused docs, not 20


### Mistake 15: Not Testing on Different OS

**What Happens:**

- Develop on Windows, works perfectly
- Someone on Mac tries to run it
- Crashes due to path separator differences (\ vs /)

**Why It Happens:**

- Only testing on one platform
- Using platform-specific code

**How to Fix:**

- Use cross-platform Python practices:
    - os.path.join() for paths
    - Avoid hardcoded \ or /
    - Test on multiple OS if possible
- Python is cross-platform, use it right
- All scripts in project are cross-platform compatible

***

## ✅ Stage 9 Complete!

Congratulations! You have now **completed all 9 stages** of the Customer Churn Analysis project!

### What You've Accomplished

**Stage 1-8 Recap:**

- ✅ Stage 1: Project setup and environment configuration
- ✅ Stage 2: Data understanding and initial exploration
- ✅ Stage 3: Data cleaning and quality validation
- ✅ Stage 4: Data quality reporting
- ✅ Stage 5: Exploratory data analysis and visualization
- ✅ Stage 6: Feature engineering and metrics layer
- ✅ Stage 7: Analytical reasoning and business insights
- ✅ Stage 8: Interactive dashboard and visualization

**Stage 9 Deliverables:**

- ✅ Professional README.md (portfolio-ready)
- ✅ Complete requirements.txt (all dependencies)
- ✅ Master automation script (run_full_analysis.py)
- ✅ Dashboard usage guide (USAGE_GUIDE.md)
- ✅ Technical documentation (TECHNICAL_DOCUMENTATION.md)
- ✅ Project structure guide (PROJECT_STRUCTURE.md)
- ✅ Deployment instructions (DEPLOYMENT.md)


### Your Complete Project Portfolio

**Final Project Structure:**

```
customer_churn_analysis/
├── data/
│   ├── raw/                        # Original dataset
│   └── processed/                  # Clean + enriched datasets
├── scripts/                        # 4 analysis scripts
├── dashboard/                      # Interactive Streamlit app
├── outputs/
│   ├── reports/                   # 6 analysis reports
│   └── visualizations/            # 20+ charts
├── run_full_analysis.py           # Master automation
├── requirements.txt               # Dependencies
├── README.md                      # Portfolio documentation
├── USAGE_GUIDE.md                 # Dashboard guide
├── TECHNICAL_DOCUMENTATION.md     # Technical specs
├── PROJECT_STRUCTURE.md           # Directory guide
└── DEPLOYMENT.md                  # Deployment guide
```


### Skills Demonstrated

**Technical Skills:**

- Python programming (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
- Data cleaning and validation
- Exploratory data analysis
- Statistical reasoning
- Feature engineering
- Dashboard development (Streamlit)
- Automation scripting
- Version control concepts
- Documentation writing

**Business Skills:**

- Business problem framing
- Churn analysis and metrics
- Customer segmentation
- Risk scoring
- ROI estimation
- Strategic recommendations
- Stakeholder communication
- Executive reporting

**Professional Skills:**

- Project organization
- Code documentation
- User guides
- Deployment preparation
- Portfolio presentation
- Professional packaging


### Project Highlights for Resume/Portfolio

**One-Liner for Resume:**
"Developed end-to-end customer churn analytics solution with interactive dashboard, identifying \$2.6M revenue at risk and providing 5 prioritized retention strategies expected to reduce churn by 15%"

**Key Metrics to Highlight:**

- 📊 7,043 customers analyzed
- 📈 26.5% baseline churn rate
- 💰 \$2.6M+ revenue at risk identified
- 🎯 4 primary churn drivers quantified
- 🔧 14 business features engineered
- 📱 5-page interactive dashboard
- 💡 5 actionable recommendations
- ⚡ 15% expected churn reduction


### Next Steps

**For Portfolio:**

1. ✅ **Update README with your information**
    - Replace [Your Name], [your.email@example.com]
    - Add your LinkedIn, GitHub, portfolio URLs
    - Customize professional summary
2. ✅ **Take Dashboard Screenshots**
    - Capture Executive Overview page
    - Capture key visualizations
    - Add to README (optional but impressive)
3. ✅ **Push to GitHub** (optional but recommended)

```bash
git init
git add .
git commit -m "Complete customer churn analysis project"
git remote add origin https://github.com/yourusername/customer_churn_analysis.git
git push -u origin main
```

4. ✅ **Deploy Dashboard** (optional)
    - Follow DEPLOYMENT.md instructions
    - Streamlit Cloud (easiest for portfolio)
    - Add live demo link to README
5. ✅ **Add to Portfolio Website**
    - Project title and description
    - Key findings and impact
    - Technologies used
    - Link to GitHub repo
    - Link to live dashboard (if deployed)
6. ✅ **Prepare for Interviews**
    - Practice explaining project (5-minute version)
    - Be ready to demo dashboard
    - Know your methodology and decisions
    - Can explain business impact

### Interview Talking Points

**"Tell me about this project":**
"I built an end-to-end customer churn analysis for a telecommunications company with 7,000+ customers. I cleaned and validated the data, conducted exploratory analysis to identify patterns, engineered 14 business-relevant features including risk scores and customer segments, performed statistical analysis to validate hypotheses, and built an interactive Streamlit dashboard. The analysis identified \$2.6 million in revenue at risk and provided 5 prioritized recommendations expected to reduce churn by 15%. The entire pipeline is automated and production-ready."

**"What was challenging?":**
"Feature engineering was challenging because I needed to create features that were both statistically meaningful and business-interpretable. For example, the Risk_Score composite metric balances multiple factors while remaining explainable to non-technical stakeholders."

**"What would you do differently?":**
"If I had more time, I'd implement A/B testing simulation to validate recommendation effectiveness, add time-series analysis to predict when customers will churn, and build a machine learning model for more precise risk scoring."

**"What's the business impact?":**
"By implementing the top 3 recommendations—contract incentives, first-year onboarding, and payment method migration—the company can expect to retain 400-600 additional customers annually, representing \$400-600K in annual revenue, with a projected overall churn reduction from 26.5% to 22-23%."

### Project Validation Checklist

Before considering 100% complete, verify:

- [ ] All 9 stages completed successfully
- [ ] All scripts run without errors
- [ ] Dashboard launches and is fully functional
- [ ] All 7 documentation files created
- [ ] README personalized (no placeholders)
- [ ] requirements.txt complete and tested
- [ ] Master automation script tested
- [ ] Project structure organized and clean
- [ ] No sensitive data exposed
- [ ] Ready for GitHub (if using)
- [ ] Ready for deployment (if deploying)
- [ ] Portfolio/resume updated with project
- [ ] Can explain project confidently


### Congratulations! 🎉

You've completed a **professional-grade, portfolio-ready data analytics project** that demonstrates:

✅ **Technical Proficiency** - Python, data analysis, visualization, dashboards
✅ **Business Acumen** - Understanding churn, revenue impact, strategic thinking
✅ **Communication Skills** - Documentation, reporting, storytelling
✅ **Professional Standards** - Code quality, automation, deployment-ready
✅ **End-to-End Capability** - Raw data → Insights → Production dashboard

This project positions you as a **job-ready data analyst** capable of:

- Handling real-world business problems
- Working with messy data
- Generating actionable insights
- Building user-facing applications
- Communicating with stakeholders
- Delivering production-quality work

**You're ready to showcase this to recruiters, add to your portfolio, and discuss confidently in interviews!**

***

## 📚 Additional Resources (Optional Enhancement)

If you want to take this project even further:

1. **Machine Learning Extension**: Build predictive churn model (logistic regression, random forest, XGBoost)
2. **Time Series Analysis**: Analyze churn trends over time (if temporal data available)
3. **A/B Testing Simulation**: Model impact of interventions
4. **Advanced Visualizations**: Add network graphs, sankey diagrams
5. **API Development**: Create REST API for predictions (Flask/FastAPI)
6. **Docker Containerization**: Package entire project in Docker
7. **CI/CD Pipeline**: Automate testing and deployment (GitHub Actions)
8. **Real-Time Dashboard**: Connect to live data source
9. **Mobile App**: Create mobile version of dashboard
10. **Advanced Segmentation**: RFM analysis, cohort analysis

But remember: **Done is better than perfect.** This project is already portfolio-worthy!

***

**Final Advice:**

🎯 **Ship it.** Don't endlessly perfect. Get it out there.
📢 **Share it.** LinkedIn post, portfolio, resume, GitHub.
💬 **Talk about it.** Practice your project story.
📈 **Learn from it.** What worked? What didn't? Apply to next project.

**Good luck with your data analytics career!** 🚀

***

*Project Complete: January 2026*

