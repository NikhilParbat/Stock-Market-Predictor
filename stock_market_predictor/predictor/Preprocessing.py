# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: .venv
#     language: python
#     name: python3
# ---

# Stock Market Predictor Preprocessing

import pandas as pd
import os

# +

working_dir = os.getcwd()

# Construct the path to the 'data' directory relative to the working directory
folder_path = os.path.join(working_dir, "data")

csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]

for file in csv_files:
    # Read the CSV file
    file_path = os.path.join(folder_path, file)
    df = pd.read_csv(file_path)
    
    # Get the Ticker name from cell B2 (row index 1, column index 1)
    ticker_name = df.iloc[0, 1]  # Adjust index to your data structure
    
    # Add the Ticker column and populate it with the ticker name
    df['Ticker'] = ticker_name

    # Rename the 'Price' column to 'Date'
    df.rename(columns={'Price': 'Date'}, inplace=True)

    # Convert the 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'][2:])  # Assuming dates start from row 3

    # Define the date range
    start_date = '2020-01-01'
    end_date = '2025-01-22'

    # Filter rows based on the date range
    df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

    # Reorder columns to make 'Ticker' the first column
    columns = ['Ticker'] + [col for col in df.columns if col != 'Ticker']
    df = df[columns]

    # Save the updated file (overwrite or create a new one)
    updated_file_path = os.path.join(folder_path, f"updated_{file}")
    df.to_csv(updated_file_path, index=False)
    
    print(f"Updated {file} with Ticker: {ticker_name}")

# -

df = pd.read_csv(r"C:\Project\Python Datasets\Stock-Market-Predictor\data\updated_ADANIENT.csv")
df.head()

df.describe()

df.isna().sum()
