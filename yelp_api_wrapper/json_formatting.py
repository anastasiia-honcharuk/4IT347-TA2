import json

# Function to load and process each JSON object in the file
def process_json_file(file_path):
    processed_data = []

    with open(file_path, 'r') as file:
        for line in file:
            try:
                json_object = json.loads(line)
                processed_data.append(json_object)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
                continue

    return processed_data

# File path to the original "yelp.json"
file_path = "yelp.json"

# Process the file
processed_data = process_json_file(file_path)

# Write the processed data back to the file with proper formatting
with open(file_path, 'w') as file:
    json.dump(processed_data, file, indent=2)

print("JSON file has been reformatted successfully.")
