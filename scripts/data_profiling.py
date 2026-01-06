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
with open(report_path, 'w', encoding='utf-8') as f:
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
