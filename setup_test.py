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
