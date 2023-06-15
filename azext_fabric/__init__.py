import azext_fabric._help
from azure.cli.core import AzCommandsLoader

class FabricCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        fabric_custom = CliCommandType(operations_tmpl='azext_fabric.custom#{}')
        super(FabricCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=fabric_custom)

    def load_command_table(self, args):
        from azext_fabric.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from ._params import load_arguments
        load_arguments(self, command)

COMMAND_LOADER_CLS = FabricCommandsLoader