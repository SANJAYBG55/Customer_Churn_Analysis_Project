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
