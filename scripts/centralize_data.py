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
