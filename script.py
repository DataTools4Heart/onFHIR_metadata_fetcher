import os
import requests

# Get URLs and dataset ID from environment variables
get_url_ub = os.environ.get("GET_URL_UB", "http://161.116.84.46/onfhir-feast/api/Dataset?url=https://datatools4heart.eu/feature-sets/study1")
get_url_srdc = os.environ.get("GET_URL_SRDC", "https://matrix.srdc.com.tr/dt4h/feast/api/Dataset?url=https://datatools4heart.eu/feature-sets/study1_features_new")

user_id = os.environ.get("USER_ID", "your_user_id")
execution_id = os.environ.get("EXECUTION_ID", "your_execution_id")

execution_dir = os.environ.get("EXECUTION_DIR")

# Perform GET request for UB
response_get_ub = requests.get(get_url_ub)
if response_get_ub.status_code == 200:
    file_content_ub = response_get_ub.content
    file_path_ub = os.path.join(execution_dir, 'summary_ub.txt')
    with open(file_path_ub, 'wb') as file_ub:
        file_ub.write(file_content_ub)
    print("GET Request for UB Status Code:", response_get_ub.status_code)
else:
    print(f"GET Request for UB failed with status code {response_get_ub.status_code}")

# Perform GET request for SRDC
response_get_srdc = requests.get(get_url_srdc)
if response_get_srdc.status_code == 200:
    file_content_srdc = response_get_srdc.content
    file_path_srdc = os.path.join(execution_dir, 'summary_srdc.txt')
    with open(file_path_srdc, 'wb') as file_srdc:
        file_srdc.write(file_content_srdc)
    print("GET Request for SRDC Status Code:", response_get_srdc.status_code)
else:
    print(f"GET Request for SRDC failed with status code {response_get_srdc.status_code}")



    # Construct the POST URL with dataset ID, user ID, and execution ID
    #post_url = f"{post_base_url}/{file_id}?user_id={user_id}&execution_id={execution_id}"

    # Perform POST request with the entire file content and basic authentication
    #files = {'files': ('file_content.txt', file_content)}
    #auth = (username, password)
    #response_post = requests.post(post_url, files=files, auth=auth)

    # Print response information
    #print("POST Request Status Code:", response_post.status_code)
    #print("POST Response Text:", response_post.text)

