import os
import requests

# Get study ID from environment variables
study_id = os.environ.get('STUDY_ID', "default_study_id")
node_name = os.environ.get('NODE_NAME')

# Create the output directory if it doesn't exist
execution_dir = os.environ.get("EXECUTION_DIR", "/home/ubuntu/UB_manager/sandbox/dt4h_summary_materializer")
output_dir = os.path.join(execution_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Construct URL mappings for different nodes based on environment variables
node_urls = {}
for key, value in os.environ.items():
    if key.startswith("GET_URL_"):
        node = key[len("GET_URL_"):]
        node_urls[node] = value

# Get user ID and execution ID from environment variables
user_id = os.environ.get("USER_ID", "your_user_id")
execution_id = os.environ.get("EXECUTION_ID", "your_execution_id")

# Get the URL based on the node name
get_url = node_urls.get(node_name)
if not get_url:
    print(f"No URL found for node {node_name}.")
    exit()

try:
    # Perform GET request
    response_get = requests.get(get_url)

    if response_get.status_code == 200:
        file_content = response_get.content
        file_path = os.path.join(output_dir, f'summary_{node_name.lower()}.txt')

        with open(file_path, 'wb') as file:
            file.write(file_content)

        print(f"GET Request for {node_name} Status Code:", response_get.status_code)
    else:
        print(f"GET Request for {node_name} failed with status code {response_get.status_code}")
except Exception as e:
    print(f"An error occurred while processing {node_name}: {e}")
