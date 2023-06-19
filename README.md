# Microsoft-Fabric-Azure-CLI-Extension

Entirely unofficial Azure CLI extension for Microsoft Fabric and my own automated deployments.

az extension add --source https://github.com/shaneochotny/Microsoft-Fabric-Azure-CLI-Extension/raw/main/dist/fabric-0.0.1-py2.py3-none-any.whl

## Currently Supports:

    capacities
        list : List available Fabric capacities.

    connections
        list : List Fabric Connections.
        show : Show the details of a Connection.
    
    domains
        create : Create a Fabric Domain.
        list : List Fabric Domains.

    lakehouse
        create : Create a Fabric Lakehouse.
        delete : Delete a Fabric Lakehouse.
        list   : List all Fabric Lakehouses.
        show   : Show the details of a Fabric Lakehouse.
    
    warehouse
        create : Create a Fabric Warehouse.
    
    workspace
        create : Create a Fabric Workspace.
        list   : List Fabric Workspaces.