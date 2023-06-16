from azure.cli.core._profile import Profile
from azure.cli.core.azclierror import ValidationError
import requests

POWERBI_RESOURCE="https://analysis.windows.net/powerbi/api"
FABRIC_BASEURL="https://wabi-west-us3-a-primary-redirect.analysis.windows.net"


def fabric_get_request(api_url):
    try:
        request_url = f"{FABRIC_BASEURL}{api_url}"
        response = requests.get(request_url, headers=build_request_header())
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
 
    return response.json()


def fabric_post_request(api_url, request_body):
    try:
        request_url = f"{FABRIC_BASEURL}{api_url}"
        response = requests.post(request_url, headers=build_request_header(), json=request_body)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
 
    return response.json()


def build_request_header():
    access_token = Profile().get_raw_token(resource=POWERBI_RESOURCE)[0][2].get("accessToken")
    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return header


def get_fabric_capacity_object_id(fabric_capacity_name):
    from azext_fabric.custom import capacities_list
    capacities = capacities_list()

    for capacity in capacities:
        if capacity["displayName"] == fabric_capacity_name:
            return capacity["capacityObjectId"]
    else:
        raise ValidationError(f"Could not find a Fabric Capacity by the name of: {fabric_capacity_name}")


def get_fabric_domain_object_id(fabric_domain_name):
    from azext_fabric.custom import domains_list
    domains = domains_list()

    for domain in domains["domains"]:
        if domain["displayName"] == fabric_domain_name:
            return domain["objectId"]
    else:
        raise ValidationError(f"Could not find a Fabric Domain by the name of: {fabric_domain_name}")


def get_fabric_workspace_object_id(fabric_workspace_name):
    from azext_fabric.custom import workspace_list
    workspaces = workspace_list()

    for workspace in workspaces:
        if workspace["workspaceName"] == fabric_workspace_name:
            return workspace["workspaceObjectId"]
    else:
        raise ValidationError(f"Could not find a Fabric Workspace by the name of: {fabric_workspace_name}")
