from azext_fabric.helpers import *

def capacities_list():
    response = fabric_get_request("/capacities/author")
    return response

def domains_list():
    response = fabric_get_request("/metadata/dataDomains")
    return response

def getSqlProvisioningStatus():
    response = fabric_get_request("/metadata/artifacts/65bedfd3-3a1a-4b75-9310-423a859db920")
    
    print(f"provisionState: {response.get('provisionState')}")

def workspace_list():
    response = fabric_get_request("/metadata/gallery/dataflows")
    return response

def workspace_create(fabric_capacity_name, fabric_workspace_name, fabric_domain_name=None):
    capacityObjectId = get_fabric_capacity_object_id(fabric_capacity_name)
    if fabric_domain_name is not None:
        domainObjectId = get_fabric_domain_object_id(fabric_domain_name)
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


def lakehouse_create(fabric_lakehouse_name, fabric_workspace_name):
    workspaceObjectId = get_fabric_workspace_object_id(fabric_workspace_name).lower()

    request_body = {
        "artifactType": "Lakehouse",
        "displayName": fabric_lakehouse_name
    }

    response = fabric_post_request(f"/metadata/workspaces/{workspaceObjectId}/artifacts", request_body)
    return response


def warehouse_create(fabric_warehouse_name, fabric_workspace_name):
    workspaceObjectId = get_fabric_workspace_object_id(fabric_workspace_name).lower()

    request_body = {
        "name": fabric_warehouse_name
    }

    response = fabric_post_request(f"/v1.0/myorg/groups/{workspaceObjectId}/datawarehouses", request_body)
    return response