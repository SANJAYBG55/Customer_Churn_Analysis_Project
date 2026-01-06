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
    if not os.path.exists("data/raw/telco_churn.csv"):
        raise FileNotFoundError("Input data file not found: data/raw/telco_churn.csv")
    
    print("Running data_cleaning.py...")
    exit_code = os.system("python scripts/data_cleaning.py")
    
    if exit_code != 0:
        raise Exception("Data cleaning script failed")
    
    # Verify output
    if not os.path.exists("data/processed/clean_churn_data.csv"):
        raise Exception("Clean data file not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 1 Complete - Time: {stage_time:.1f}s")
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
    print("Running eda_analysis.py...")
    exit_code = os.system("python scripts/eda_analysis.py")
    
    if exit_code != 0:
        raise Exception("EDA script failed")
    
    # Verify output
    if not os.path.exists("outputs/reports/eda_findings.txt"):
        raise Exception("EDA report not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 2 Complete - Time: {stage_time:.1f}s")
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
    
    # Verify output
    if not os.path.exists("data/processed/enriched_churn_data.csv"):
        raise Exception("Enriched data file not created")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 3 Complete - Time: {stage_time:.1f}s")
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
    
    # Verify outputs
    required_reports = [
        "outputs/reports/analysis_report.txt",
        "outputs/reports/business_recommendations.txt",
        "outputs/reports/executive_summary.txt"
    ]
    
    for report in required_reports:
        if not os.path.exists(report):
            raise Exception(f"Required report not created: {report}")
    
    stage_time = time.time() - stage_start
    print(f"\n✅ Stage 4 Complete - Time: {stage_time:.1f}s")
    stages_completed.append("Stage 4: Analytical Reasoning")
    
except Exception as e:
    print(f"\n❌ Stage 4 Failed: {str(e)}")
    stages_failed.append("Stage 4: Analytical Reasoning")
    sys.exit(1)

print()

# ==================== PIPELINE SUMMARY ====================
print("=" * 80)
print("PIPELINE EXECUTION SUMMARY")
print("=" * 80)
print()

pipeline_time = time.time() - pipeline_start
print(f"Total Execution Time: {pipeline_time:.1f}s ({pipeline_time/60:.1f} minutes)")
print()

print("✅ Stages Completed:")
for stage in stages_completed:
    print(f"   • {stage}")
print()

if stages_failed:
    print("❌ Stages Failed:")
    for stage in stages_failed:
        print(f"   • {stage}")
    print()
    sys.exit(1)
else:
    print("🎉 ALL STAGES COMPLETED SUCCESSFULLY!")
    print()
    print("Next Steps:")
    print("   1. Review analysis reports in outputs/reports/")
    print("   2. Launch dashboard: streamlit run dashboard/churn_dashboard.py")
    print()
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
