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
