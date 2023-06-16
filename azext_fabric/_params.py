from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import name_type

fabric_capacity_name_type = CLIArgumentType(
    help='Name of the Fabric Capacity.',
    arg_type=name_type,
    options_list=['--capacity-name'])

fabric_workspace_name_type = CLIArgumentType(
    help='Name of the Fabric Workspace.',
    arg_type=name_type,
    options_list=['--workspace-name'])

def load_arguments(self, _):
    with self.argument_context('fabric lakehouse create') as c:
        c.argument('fabric_lakehouse_name', options_list=['--lakehouse-name'], help='Name of the Fabric Lakehouse in which to add the Workspace.')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')

    with self.argument_context('fabric warehouse create') as c:
        c.argument('fabric_warehouse_name', options_list=['--warehouse-name'], help='Name of the Fabric Warehouse in which to add the Workspace.')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')

    with self.argument_context('fabric workspace create') as c:
        c.argument('fabric_capacity_name', arg_type=fabric_capacity_name_type, options_list=['--capacity-name'], id_part='capacity-name')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')
        c.argument('fabric_domain_name', options_list=['--domain-name'], help='Name of the Fabric Domain in which to add the Workspace.')
