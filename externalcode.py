import requests
import base64

# # Assuming your config file contains the URL of the GitHub repository and the file path
# repository_url = "https://api.github.com/repos/JelleFirlefyn/remote-control"
# file_path = "/test.py"

def download_and_execute(repository_url, file_path):
    # Make a request to the GitHub API to get the contents of the file
    response = requests.get(f"{repository_url}/contents/{file_path}")
    if response.status_code == 200:
        content = response.json()
        code = base64.b64decode(content["content"]).decode("utf-8")

        # Execute the code
        exec(code)
    else:
        print("Failed to fetch the file from the repository.")
