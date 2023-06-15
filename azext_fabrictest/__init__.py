import azext_fabrictest._help
from azure.cli.core import AzCommandsLoader

class FabricCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        fabrictest_custom = CliCommandType(operations_tmpl='azext_fabrictest.custom#{}')
        super(FabricCommandsLoader, self).__init__(cli_ctx=cli_ctx, custom_command_type=fabrictest_custom)

    def load_command_table(self, args):
        from azext_fabrictest.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, _):
        pass

COMMAND_LOADER_CLS = FabricCommandsLoader