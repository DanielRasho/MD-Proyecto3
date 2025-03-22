import pandas as pd

# Define the file path
file_path = "./data/2014.CSV"  # Change this to your actual file path

# Read the CSV file
df = pd.read_csv(file_path)

# Add a new column with value 2013
df["AÑOOCU"] = 2014

# Save the modified data back to the same file
df.to_csv(file_path, index=False)

print("Column 'Year' added with value 2013 and file saved successfully.")