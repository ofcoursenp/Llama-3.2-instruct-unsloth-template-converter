import pandas as pd
import json

# Load the CSV file
input_file = 'input.csv'  # Change this to your input CSV file path
output_file = 'output.json'  # Output file name

# Read the CSV file
df = pd.read_csv(input_file)

# Check for missing values in 'Questions' and 'Answer' columns
df = df[['Questions', 'Answer']]  # Keep only relevant columns
# df.fillna('No answer provided.', inplace=True)  # Fill NaN values with a default message
print(df)
# Function to format question and answer
def format_qa(row):
    return [
        {'from': 'human', 'value': row['Questions']},
        {'from': 'gpt', 'value': row['Answer']}
    ]

# Apply the formatting function to each row and convert to JSON format
formatted_data = df.apply(format_qa, axis=1).tolist()

# Save the formatted data to a JSON file
with open(output_file, 'w') as f:
    json.dump(formatted_data, f, indent=4)

print(f"Formatted data has been saved to {output_file}.")
