import pandas as pd

PATH = "data/bronze/[FILENAME].csv" # Replace [FILENAME] with the actual filename of your CSV file.

# Opens the CSV file and reads it into a pandas DataFrame
df = pd.read_csv(PATH)

print(df.shape)


# Prints the names of the columns in the DataFrame
for column in df.columns:
    print(f'"{column}"')



# Checks if the expected columns exists in the DataFrame
EXPECTED_COLUMNS = ["[COLUMN0]", "[COLUMN1]", "[COLUMN2]"] # Replace [COLUMN0], [COLUMN1], [COLUMN2] with the actual expected column names of your CSV file.

MISSING_COLUMNS = [c for c in EXPECTED_COLUMNS if c not in df.columns]

print("Not found columns:", MISSING_COLUMNS)

# Organizes the DataFrame in functions
def load():
    return pd.read_csv(PATH)

def check_structure(df):
    print(df.shape)
    print(df.dtypes)

if __name__ == "__main__":
    check_structure(load())