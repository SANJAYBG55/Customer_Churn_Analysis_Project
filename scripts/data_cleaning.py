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

# Write report to file with UTF-8 encoding to handle special characters
with open(report_path, 'w', encoding='utf-8') as f:
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
