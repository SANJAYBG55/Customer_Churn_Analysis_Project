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
