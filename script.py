import os
import requests

# Get URLs and dataset ID from environment variables
get_url = os.environ.get("GET_URL", "https://matrix.srdc.com.tr/dt4h/feast/api/Dataset?url=https://datatools4heart.eu/feature-sets/study1_features_new")
post_base_url = os.environ.get("POST_BASE_URL", "https://fl.bsc.es/flmanager/API/v1/data/push_file_content")
file_id = os.environ.get("FILE_ID", "your_file_id")
user_id = os.environ.get("USER_ID", "your_user_id")
execution_id = os.environ.get("EXECUTION_ID", "your_execution_id")

# Basic authentication credentials
username = os.environ.get("USERNAME", "your_username")
password = os.environ.get("PASSWORD", "your_password")

# Perform GET request
response_get = requests.get(get_url)

# Check if the GET request was successful
if response_get.status_code == 200:
    # Get the content of the file from the GET response
    file_content = response_get.content

    # Save the content to a file within the execution folder
    execution_folder_path = os.path.join(user_id, execution_id)
    #os.makedirs(execution_folder_path, exist_ok=True)
    #file_path = os.path.join(execution_folder_path, 'summary.txt')
    file_path = 'summary.txt'


    with open(file_path, 'wb') as file:
        file.write(file_content)


    # Construct the POST URL with dataset ID, user ID, and execution ID
    #post_url = f"{post_base_url}/{file_id}?user_id={user_id}&execution_id={execution_id}"

    # Perform POST request with the entire file content and basic authentication
    #files = {'files': ('file_content.txt', file_content)}
    #auth = (username, password)
    #response_post = requests.post(post_url, files=files, auth=auth)

    # Print response information
    print("GET Request Status Code:", response_get.status_code)
    #print("POST Request Status Code:", response_post.status_code)
    #print("POST Response Text:", response_post.text)
else:
    print(f"GET Request failed with status code {response_get.status_code}")

