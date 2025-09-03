import pandas as pd

file_path = r"C:\Users\tamil\Downloads\tata ai\task 1\Delinquency_prediction_dataset.xlsx"

# List and print all sheet names in the Excel file
xls = pd.ExcelFile(file_path)
print("✅ Available sheet names:")
print(xls.sheet_names)
