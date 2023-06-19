from azure.cli.core.commands import CliCommandType

def load_command_table(self, _):
    with self.command_group("fabric capacities") as g:
        g.custom_command('list', 'capacities_list')

    with self.command_group("fabric connections") as g:
        g.custom_command('list', 'connections_list')
        g.custom_command('show', 'connections_show')

    with self.command_group("fabric domains") as g:
        g.custom_command('create', 'domains_create')
        g.custom_command('list', 'domains_list')

    with self.command_group("fabric lakehouse") as g:
        g.custom_command('create', 'lakehouse_create')
        g.custom_command('delete', 'lakehouse_delete')
        g.custom_command('list', 'lakehouse_list')
        g.custom_command('show', 'lakehouse_show')

    with self.command_group("fabric shortcut create") as g:
        g.custom_command('azuredatalake', 'shortcut_create')

    with self.command_group("fabric warehouse") as g:
        g.custom_command('create', 'warehouse_create')

    with self.command_group("fabric workspace") as g:
        g.custom_command('create', 'workspace_create')
        g.custom_command('list', 'workspace_list')