import pandas as pd

def process_bar_separated_file(input_file_path, output_file_path):
    """
    Args:
        input_file_path (str): Path to the input file.
        output_file_path (str): Path to save the processed file.

    Returns:
        pd.DataFrame: The processed DataFrame.
    """
    try:
        # Read the file line by line
        with open(input_file_path, 'r', encoding='utf-8') as f:
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
        df.to_csv(output_file_path, index=False)

        print(f"Processed file with headers saved to {output_file_path}")
        return df

    except Exception as e:
        print(f"Error during file processing: {e}")
        return None

# Prompt user for input and output file paths
input_file_path = input("Enter the path to the input file: ")
output_file_path = input("Enter the path to save the processed file: ")

# Process the file and save the output
processed_df = process_bar_separated_file(input_file_path, output_file_path)

if processed_df is not None:
    print("Processing completed successfully.")
