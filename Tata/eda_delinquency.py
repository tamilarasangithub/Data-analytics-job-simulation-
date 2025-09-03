import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set your corrected file path and sheet name
file_path = r"C:\Users\tamil\Downloads\tata ai\task 1\fixed_file.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")  # Or "DelinquencyData" if that's your sheet name

# Preview the data
print("🔹 First 5 rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Missing Values:")
print(df.isnull().sum())

#  Summary statistics
print("\n🔹 Summary Statistics:")
print(df.describe())

#  Correlation heatmap (numerical only)
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Numerical Features")
plt.tight_layout()
plt.show()

#Inga Na step 2  add handle missing data if missing data

df['Income'].fillna(df['Income'].median(), inplace=True)
df['Credit_Score'].fillna(df['Credit_Score'].mean(), inplace=True)
df['Loan_Balance'].fillna(df['Loan_Balance'].median(), inplace=True)

print("\n Missing data imputed successfully.")


