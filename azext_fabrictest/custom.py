import requests
from azure.cli.core._profile import Profile

def getSqlProvisioningStatus():
    access_token = Profile().get_raw_token(resource="https://analysis.windows.net/powerbi/api")[0][2].get("accessToken")

    api_url = 'https://wabi-west-us3-a-primary-redirect.analysis.windows.net/metadata/artifacts/35c469a9-8be5-421e-932d-63fd85556a92'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(api_url, headers=headers)
    
    print(f"provisionState: {response.json().get('provisionState')}")

def createWorkspace():
    access_token = Profile().get_raw_token(resource="https://analysis.windows.net/powerbi/api")[0][2].get("accessToken")

    api_url = 'https://wabi-west-us3-a-primary-redirect.analysis.windows.net/metadata/folders'
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    body = {
        "displayName": "myclitest",
        "capacityObjectId": "214DDB59-0299-4532-98C1-C74B31AB4BD5",
        "isServiceApp": "false",
        "datasetStorageMode": "2",
        "domainObjectId": ""
    }

    post = requests.post(api_url, headers=headers, json=body)