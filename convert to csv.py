import pandas as pd

# Function to format question and answer
def format_qa(row):
    # Check if Answer is NaN and provide a default message if necessary
    answer = row['Answer'] if pd.notna(row['Answer']) else "No answer provided."
    
    return [
        {'question': row['Questions'], 'answer': answer}
    ]

# Load the CSV file
input_file = 'input.csv'  # Change this to your input CSV file path
output_file = 'output.csv'  # Output file name

# Read the CSV file
df = pd.read_csv(input_file)

# Apply the formatting function to each row and prepare rows for the new DataFrame
rows = []
for index, row in df.iterrows():
    formatted_conversations = format_qa(row)
    new_row = {
        "conversations": formatted_conversations,
        "source": 1,
        "score": 1
    }
    rows.append(new_row)

# Create a DataFrame from the new rows
output_df = pd.DataFrame(rows)

# Save DataFrame to a CSV file
output_df.to_csv(output_file, index=False)

print(f"Formatted data has been saved to {output_file}.")
