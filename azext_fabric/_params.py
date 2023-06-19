from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import name_type, get_enum_type

fabric_capacity_name_type = CLIArgumentType(
    help='Name of the Fabric Capacity.',
    arg_type=name_type,
    options_list=['--capacity-name'])

fabric_workspace_name_type = CLIArgumentType(
    help='Name of the Fabric Workspace.',
    arg_type=name_type,
    options_list=['--workspace-name'])

fabric_connection_name_type = CLIArgumentType(
    help='Name of the Fabric Connection.',
    arg_type=name_type,
    options_list=['--connection-name'])

yes_arg_type = CLIArgumentType(
        options_list=['--yes', '-y'],
        action='store_true',
        help='Do not prompt for confirmation.'
    )

def load_arguments(self, _):
    with self.argument_context('fabric domains create') as c:
        c.argument('fabric_domain_name', options_list=['--name'], help='Name of the Fabric Domain in which to create.')
        c.argument('fabric_domain_description', options_list=['--description'], help='Description of the Fabric Domain.')

    with self.argument_context('fabric lakehouse create') as c:
        c.argument('fabric_lakehouse_name', options_list=['--lakehouse-name'], help='Name of the Fabric Lakehouse in which to create the Workspace.')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')

    with self.argument_context('fabric lakehouse delete') as c:
        c.argument('fabric_lakehouse_name', options_list=['--lakehouse-name'], help='Name of the Fabric Lakehouse in which to delete the Workspace.')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')
        c.argument('yes', arg_type=yes_arg_type)

    with self.argument_context('fabric lakehouse list') as c:
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')

    with self.argument_context('fabric lakehouse show') as c:
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')
        c.argument('fabric_lakehouse_name', options_list=['--lakehouse-name'], help='Name of the Fabric Lakehouse.')

    with self.argument_context('fabric shortcut create azuredatalake') as c:
        c.argument('fabric_connection_name', arg_type=fabric_connection_name_type, options_list=['--connection-name'], id_part='connection-name')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')
        c.argument('fabric_lakehouse_name', options_list=['--lakehouse-name'], help='Name of the Fabric Lakehouse in which to create the Shortcut.')
        c.argument('fabric_shortcut_name', options_list=['--shortcut-name'], help='Name of the Shortcut.')
        c.argument('fabric_shortcut_type', options_list=['--shortcut-type'], arg_type=get_enum_type(['Files', 'Tables'], default='Files'), help='Type of the Shortcut.')

    with self.argument_context('fabric warehouse create') as c:
        c.argument('fabric_warehouse_name', options_list=['--warehouse-name'], help='Name of the Fabric Warehouse in which to create the Workspace.')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')

    with self.argument_context('fabric workspace create') as c:
        c.argument('fabric_capacity_name', arg_type=fabric_capacity_name_type, options_list=['--capacity-name'], id_part='capacity-name')
        c.argument('fabric_workspace_name', arg_type=fabric_workspace_name_type, options_list=['--workspace-name'], id_part='workspace-name')
        c.argument('fabric_domain_name', options_list=['--domain-name'], help='Name of the Fabric Domain in which to create the Workspace.')


#fabric shortcut create onelake
#    --connection-name
#    --workspace-name
#    --lakehouse-name
#    --shortcut-name
#    --shortcut-type
#    --source-workspace-name
#    --source-lakehouse-name
#    --source-type

#fabric shortcut create azuredatalake
#    --connection-name
#    --workspace-name
#    --lakehouse-name
#    --shortcut-name
#    --shortcut-type