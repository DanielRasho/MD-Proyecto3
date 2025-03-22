import pandas as pd

# Define the file path
file_path = "./data/2013.CSV"  # Change this to your actual file path

# Read the CSV file
df = pd.read_csv(file_path)

# Replace "IGNORADO" with 99 in the CIUOUMUJ column
df["CIUOMUJ"] = df["CIUOMUJ"].replace("IGNORADO", "99")
df["CIUOHOM"] = df["CIUOHOM"].replace("IGNORADO", "99")
df["CIUOMUJ"] = df["CIUOMUJ"].replace("NEOG", "99")
df["CIUOHOM"] = df["CIUOHOM"].replace("NEOG", "99")

# Save the modified data back to the same file
df.to_csv(file_path, index=False)

print("Replaced 'IGNORADO' with '99' in column 'CIUOUMUJ' and saved the file.")