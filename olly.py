# %% [Cell 1: Import Polars and define file path]

import polars as pl
import io

# Define the file path
FILE_PATH = 'data/BRES2023_practice.csv' 

# %% [Cell 2: Robust data loading and preparation]
# Define the columns that contain the employment COUNT data (these MUST be strings first)
# These are the even-numbered columns starting from column_2
SCHEMA_OVERRIDES = {
    "column_2": pl.Utf8, 
    "column_4": pl.Utf8, 
    "column_6": pl.Utf8, 
    "column_8": pl.Utf8,
    "column_10": pl.Utf8
}

print(f"Attempting to read file: {FILE_PATH} with explicit string schema.")

try:
    df = pl.read_csv(
        FILE_PATH,
        separator=',',   
        quote_char='"',  
        skip_rows=9, 
        has_header=False,
        truncate_ragged_lines=True,
        ignore_errors=True,
        # FIX: Explicitly tell Polars to read the count columns as strings
        schema_overrides=SCHEMA_OVERRIDES
    )
    
    print("CSV loaded successfully! Polars DataFrame head:")
    print(df.head(5))

    print("\nPolars Column Names (Default):")
    print(df.columns) 
    
    print("\nPolars DataFrame Schema (Check Dtypes!):")
    print(df.schema)

except Exception as e:
    print(f"\nERROR: Final attempt failed.")
    print(f"Details: {e}")

# %% [cell 3: Cleaning and Formatting]

# Map the default Polars column names (based on index) to the final clean names.
# NOTE: The column indices are shifted by one because Polars dropped column_0.
EXPLICIT_RENAME_MAP = {
    'column_1': 'Industry',            
    'column_2': 'West_of_England',     
    'column_4': 'Bath_and_NES',        
    'column_6': 'Bristol',             
    'column_8': 'North_Somerset',      
    'column_10': 'South_Gloucestershire', 
}
# %% [cell 4:Renaming and polars chaning cleaning data]
COLS_TO_KEEP = list(EXPLICIT_RENAME_MAP.values())


# 1. Rename the main data columns
# df comes from Cell 1, which now has string types for the count columns
# rename, define which columns and data to drop with null values
df_cleaned = (df.rename(EXPLICIT_RENAME_MAP)
                .select(COLS_TO_KEEP)
                .drop_nulls(subset=["Industry"]))

# %% [cell 5: Clean numeric columns]

# 3. Clean numeric columns (remove commas/non-numeric characters and cast to Int32)
COUNT_COLS = COLS_TO_KEEP[1:] 

#%% [cell 6: Display results and show successful data clean so far]

# Display the results
print("DataFrame after cleaning steps:")
print(df_cleaned.head(10))
print("\nNew Polars DataFrame Schema:")
print(df_cleaned.schema)


# %% [Cell 7: Final Robust Casting and Cleaning]

# NOTE: This cell uses df_cleaned from Cell 4

# Identify the employment count columns for cleaning
COUNT_COLS = df_cleaned.columns[1:] 

# Apply the final, fully robust cleaning expression
df_final = df_cleaned.with_columns(
    [
        pl.col(col)
          # 1. Aggressive Regex: Remove ALL non-digit characters (commas, spaces, etc.)
          .str.replace_all(r"[^0-9]", "") 
          
          # 2. Handle Empties: If the result is an empty string (from a null or clean-up), 
          # replace it with "0" to ensure casting works.
          .replace("", "0") 
          
          # 3. Final Cast: Convert the clean string of digits to an integer.
          .cast(pl.Int32)
        for col in COUNT_COLS
    ]
)

# Display the results
print("DataFrame after final data cleaning:")
print(df_final.head(10))

# Check the final schema—the crucial test!
print("\nFinal Polars DataFrame Schema:")
print(df_final.schema)

# %%
