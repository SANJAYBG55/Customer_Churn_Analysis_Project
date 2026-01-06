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
