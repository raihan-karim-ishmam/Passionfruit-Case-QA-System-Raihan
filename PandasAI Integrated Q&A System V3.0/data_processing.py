import pandas as pd

# This is the data preprocessing script curated after sound number of test runs to ensure the best set of minimal processing to the 
# files that makes them ready for the llms and let them work most efficiently. 


# Define input and output file paths
input_file_path = 'NEVO2023_8.0.csv'  # Path to your original file
output_file_path = 'processed_NEVO2023_with_headers.csv'  # Path to save the processed file

def process_bar_separated_file(file_path, output_path):
    # Read the file line by line
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Split each line by the bar ('|') separator
    rows = [line.strip().split('|') for line in lines]
    
    # Find the maximum number of columns in any row
    max_columns = max(len(row) for row in rows)
    
    # Ensure all rows have the same number of columns by padding with None
    normalized_rows = [row + [None] * (max_columns - len(row)) for row in rows]
    
    # Convert to a DataFrame, using the first row as column names
    df = pd.DataFrame(normalized_rows[1:], columns=normalized_rows[0])
    
    # Save to a new CSV file
    df.to_csv(output_path, index=False)
    return df

# Process the file and display the DataFrame
processed_df = process_bar_separated_file(input_file_path, output_file_path)

# Display the processed DataFrame
from IPython.display import display
display(processed_df)

print(f"Processed file with headers saved to {output_file_path}")
