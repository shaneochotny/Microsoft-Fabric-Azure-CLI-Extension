from azure.cli.core._profile import Profile
from azure.cli.core.azclierror import ValidationError
import requests

POWERBI_AUTH_AUDIENCE="https://analysis.windows.net/powerbi/api"
FABRIC_ONELAKE_AUTH_AUDIENCE="https://storage.azure.com"


FABRIC_BASEURL="https://wabi-west-us3-a-primary-redirect.analysis.windows.net"
FABRIC_ONELAKE_BASEURL="https://onelake.dfs.fabric.microsoft.com"


def fabric_get_request(api_url):
    try:
        request_url = f"{FABRIC_BASEURL}{api_url}"
        response = requests.get(request_url, headers=build_request_header(POWERBI_AUTH_AUDIENCE))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
 
    return response.json()


def fabric_post_request(api_url, request_body):
    try:
        request_url = f"{FABRIC_BASEURL}{api_url}"
        response = requests.post(request_url, headers=build_request_header(POWERBI_AUTH_AUDIENCE), json=request_body)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
 
    return response.json()


def fabric_delete_request(api_url):
    try:
        request_url = f"{FABRIC_BASEURL}{api_url}"
        response = requests.delete(request_url, headers=build_request_header(POWERBI_AUTH_AUDIENCE))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
 
    return


def fabric_onelake_put_request(api_url, request_body):
    try:
        request_url = f"{FABRIC_ONELAKE_BASEURL}{api_url}"
        response = requests.put(request_url, headers=build_request_header(FABRIC_ONELAKE_AUTH_AUDIENCE), json=request_body)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
 
    return response.json()


def build_request_header(auth_resource):
    access_token = Profile().get_raw_token(resource=auth_resource)[0][2].get("accessToken")
    header = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "X-Powerbi-User-Admin": "true"
    }
    return header


def get_fabric_capacity_object_id(fabric_capacity_name):
    from azext_fabric.custom import capacities_list
    capacities = capacities_list()

    for capacity in capacities:
        if "displayName" in capacity and capacity["displayName"].casefold() == fabric_capacity_name.casefold():
            return capacity["capacityObjectId"]
    else:
        raise ValidationError(f"Could not find a Fabric Capacity by the name of: {fabric_capacity_name}")


def get_fabric_connection(fabric_connection_name):
    from azext_fabric.custom import connections_list
    connections = connections_list()

    for connection in connections["value"]:
        if "datasourceName" in connection and connection["datasourceName"].casefold() == fabric_connection_name.casefold():
            return connection
    else:
        raise ValidationError(f"Could not find a Fabric Connection by the name of: {fabric_connection_name}")


def get_fabric_domain(fabric_domain_name):
    from azext_fabric.custom import domains_list
    domains = domains_list()

    for domain in domains["domains"]:
        if "displayName" in domain and domain["displayName"].casefold() == fabric_domain_name.casefold():
            return domain
    else:
        raise ValidationError(f"Could not find a Fabric Domain by the name of: {fabric_domain_name}")


def get_fabric_workspace(fabric_workspace_name):
    from azext_fabric.custom import workspace_list
    workspaces = workspace_list()

    for workspace in workspaces:
        if "workspaceName" in workspace and workspace["workspaceName"].casefold() == fabric_workspace_name.casefold():
            return workspace
    else:
        raise ValidationError(f"Could not find a Fabric Workspace by the name of: {fabric_workspace_name}")


def get_fabric_artifacts(supported_types=[ "Model", "Sql", "KustoDatabase", "Lakehouse", "Datawarehouse", "Lakewarehouse" ],
                         trident_supported_types=[ "dataset", "datamart", "KustoDatabase", "Lakehouse", "data-warehouse", "lake-warehouse" ]):
    request_body = {
        "supportedTypes": supported_types,
        "tridentSupportedTypes": trident_supported_types,
        "pageNumber": 1,
        "pageSize": 1000
    }

    response = fabric_post_request("/metadata/datahub/V2/artifacts", request_body)
    return response
