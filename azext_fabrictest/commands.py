from azure.cli.core.commands import CliCommandType

def load_command_table(self, _):

    with self.command_group("fabric") as g:
        g.custom_command('sql-provisioning-status', 'getSqlProvisioningStatus')

    with self.command_group("fabric workspace") as g:
        g.custom_command('create', 'createWorkspace')
