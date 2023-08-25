from azext_fabric.helpers import *
from azure.cli.core.util import user_confirmation
import json


###################################################################################################
#
# capacities
#
###################################################################################################


# capacities_list
#
# :return: JSON array of Fabric Capacities
def capacities_list():
    response = fabric_get_request("/capacities/author")
    return response


###################################################################################################
#
# connections
#
###################################################################################################


# connections_list
#
# :return: JSON array of Connections
def connections_list():
    response = fabric_get_request("/v2.0/myorg/me/gatewayClusterDatasources?$expand=users")
    return response


# connections_show
#
# :param fabric_connection_name: Name of the Connection
# :return: JSON configuration
def connections_show(fabric_connection_name):
    response = get_fabric_connection(fabric_connection_name)
    return response


###################################################################################################
#
# domains
#
###################################################################################################


# domains_create
#
# :param fabric_domain_name: Name of the Fabric Domain to create
# :param fabric_domain_description: Description of the Fabric Domain
# :return: JSON configuration
def domains_create(fabric_domain_name, fabric_domain_description=""):
    print(fabric_domain_name)
    print(fabric_domain_description)
    request_body = {
        "description": fabric_domain_description,
        "displayName": fabric_domain_name
    }

    response = fabric_post_request(f"/metadata/admin/dataDomains", request_body)
    return response


# domains_list
#
# :return: JSON array of Domains
def domains_list():
    response = fabric_get_request("/metadata/dataDomains")
    return response


###################################################################################################
#
# lakehouse
#
###################################################################################################


# lakehouse_create
#
# :param fabric_workspace_name: Name of the Fabric Lakehouse to create
# :param fabric_workspace_name: Name of the Fabric Workspeace to create the Lakehouse in
# :return: JSON configuration
def lakehouse_create(fabric_lakehouse_name, fabric_workspace_name):
    workspaceObjectId = get_fabric_workspace(fabric_workspace_name)["objectId"]

    request_body = {
        "artifactType": "Lakehouse",
        "displayName": fabric_lakehouse_name
    }

    response = fabric_post_request(f"/metadata/workspaces/{workspaceObjectId}/artifacts", request_body)
    return response


# lakehouse_delete
#
# :param fabric_workspace_name: Name of the Fabric Lakehouse to delete
# :param fabric_workspace_name: Name of the Fabric Workspeace which contains the Lakehouse
# :param yes: Confirmation of deletion
# :return: JSON configuration
def lakehouse_delete(fabric_lakehouse_name, fabric_workspace_name, yes=None):
    workspaceObjectId = get_fabric_workspace(fabric_workspace_name)["objectId"]
    lakehouseObjectId = lakehouse_show(fabric_workspace_name, fabric_lakehouse_name)["artifactObjectId"]

    if not yes:
        user_confirmation("Are you sure you want to delete the Lakehouse '{0}' in Workspace '{1}'".format(fabric_lakehouse_name, fabric_workspace_name), yes=yes)

    fabric_delete_request(f"/metadata/artifacts/{lakehouseObjectId}")
    return


# lakehouse_list
#
# :param fabric_workspace_name: Optional Fabric Workspace name to filter on
# :return: JSON configuration
def lakehouse_list(fabric_workspace_name=None):
    response = get_fabric_artifacts(["Lakehouse"], ["Lakehouse"])
    if fabric_workspace_name is not None:
        workspace_lakehouses = [keys for keys in response if keys['workspaceName'].casefold() == fabric_workspace_name.casefold()]
        return workspace_lakehouses
    else:
        return response


# lakehouse_show
#
# :param fabric_workspace_name: Fabric Workspace name where the Lakehouse exists
# :param fabric_lakehouse_name: Fabric Lakehouse name to fetch
# :return: JSON configuration
def lakehouse_show(fabric_workspace_name, fabric_lakehouse_name):
    workspace_lakehouses = get_fabric_artifacts(["Lakehouse"], ["Lakehouse"])
    for lakehouse in workspace_lakehouses:
        if "workspaceName" in lakehouse and lakehouse["workspaceName"].casefold() == fabric_workspace_name.casefold() and lakehouse["displayName"].casefold() == fabric_lakehouse_name.casefold():
            return lakehouse
    else:
        raise ValidationError(f"Could not find a Fabric Lakehouse by the name of '{fabric_lakehouse_name}' in the '{fabric_workspace_name}' workspace")


###################################################################################################
#
# shortcut
#
###################################################################################################


def shortcut_create(fabric_connection_name, fabric_workspace_name, fabric_lakehouse_name="31f5c2ef-bfc8-456e-aea4-cd518cf994dc", fabric_shortcut_name="", fabric_shortcut_type="Files"):
    connectionDetails = get_fabric_connection(fabric_connection_name)
    connectionObjectId = connectionDetails["id"]
    connectionServer = json.loads(connectionDetails["connectionDetails"])["server"]

    workspaceObjectId = get_fabric_workspace(fabric_workspace_name)["objectId"]

    request_url = f"/v2.0/workspaces/{fabric_workspace_name}/artifacts/{fabric_lakehouse_name}/shortcuts/{fabric_shortcut_type}/{fabric_shortcut_name}"

    request_body = {
        "subFolderPath": fabric_shortcut_type,
        "name": fabric_shortcut_name,
        "autoRenameOnConflict": "true",
        "targetProperties":
        {
            "Path": f"{connectionServer}/",
            "TargetAccountType":"ExternalADLS",
            "TargetType":"Folder",
            "CustomProperties":
            {
                "shortcutDataConnectionId": connectionObjectId
            }
        }
    }

    response = fabric_onelake_put_request(request_url, request_body)
    return response


###################################################################################################
#
# warehouse
#
###################################################################################################


# warehouse_create
#
# :param fabric_warehouse_name: Name of the Fabric Lakehouse to create
# :param fabric_workspace_name: Name of the Fabric Workspeace to create the Warehouse in
# :return: JSON configuration
def warehouse_create(fabric_warehouse_name, fabric_workspace_name):
    workspaceObjectId = get_fabric_workspace(fabric_workspace_name)["objectId"]

    request_body = {
        "name": fabric_warehouse_name
    }

    response = fabric_post_request(f"/v1.0/myorg/groups/{workspaceObjectId}/datawarehouses", request_body)
    return response


###################################################################################################
#
# workspace
#
###################################################################################################


# workspace_create
#
# :param fabric_capacity_name: Name of the Fabric Capacity to use for the Workspace
# :param fabric_workspace_name: Name of the Fabric Workspeace to create
# :param fabric_domain_name: Optional Domain to create the Workspace in
# :return: JSON configuration
def workspace_create(fabric_capacity_name, fabric_workspace_name, fabric_domain_name=None):
    capacityObjectId = get_fabric_capacity_object_id(fabric_capacity_name)
    if fabric_domain_name is not None:
        domainObjectId = get_fabric_domain(fabric_domain_name)["objectId"]
    else:
        domainObjectId = ""

    request_body = {
        "displayName": fabric_workspace_name,
        "capacityObjectId": capacityObjectId,
        "isServiceApp": "false",
        "datasetStorageMode": "2",
        "domainObjectId": domainObjectId
    }

    response = fabric_post_request("/metadata/folders", request_body)
    return response


# workspace_list
#
# :return: JSON array of Workspaces
def workspace_list():
    request_body = {
        "supportedTypes": [
            "Model",
            "Sql",
            "KustoDatabase",
            "Lakehouse",
            "Datawarehouse",
            "Lakewarehouse"
        ],
        "tridentSupportedTypes": [
            "dataset",
            "datamart",
            "KustoDatabase",
            "Lakehouse",
            "data-warehouse",
            "lake-warehouse"
        ],
        "filters": []
    }

    response = fabric_post_request("/metadata/datahub/workspaces", request_body)

    return response