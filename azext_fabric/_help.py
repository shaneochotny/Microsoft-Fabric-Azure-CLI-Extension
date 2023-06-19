from knack.help_files import helps

helps['fabric'] = """
type: group
short-summary: Unofficial extension for managing Fabric domains, workspaces, and artifacts.
"""


###################################################################################################
#
# capacities
#
###################################################################################################

helps['fabric capacities'] = """
type: group
short-summary: Manage Fabric Capacities.
"""

helps['fabric capacities list'] = """
    type: command
    short-summary: List available Fabric capacities.
"""

###################################################################################################
#
# connections
#
###################################################################################################

helps['fabric connections'] = """
type: group
short-summary: Manage Fabric Connections.
"""

helps['fabric connections list'] = """
    type: command
    short-summary: List Fabric Connections.
"""

helps['fabric connections show'] = """
    type: command
    short-summary: Show the details of a Connection.
"""

###################################################################################################
#
# domains
#
###################################################################################################

helps['fabric domains'] = """
type: group
short-summary: Manage Fabric Domains.
"""

helps['fabric domains create'] = """
    type: command
    short-summary: Create a Fabric Domain.
"""

helps['fabric domains list'] = """
    type: command
    short-summary: List Fabric Domains.
"""

###################################################################################################
#
# lakehouse
#
###################################################################################################

helps['fabric lakehouse'] = """
type: group
short-summary: Manage Fabric Lakehouses.
"""

helps['fabric lakehouse create'] = """
    type: command
    short-summary: Create a Fabric Lakehouse.
"""

helps['fabric lakehouse delete'] = """
    type: command
    short-summary: Delete a Fabric Lakehouse.
"""

helps['fabric lakehouse list'] = """
    type: command
    short-summary: List all Fabric Lakehouses.
"""

helps['fabric lakehouse show'] = """
    type: command
    short-summary: Show the details of a Fabric Lakehouse.
"""

###################################################################################################
#
# warehouse
#
###################################################################################################

helps['fabric warehouse'] = """
type: group
short-summary: Manage Fabric Warehouses.
"""

helps['fabric warehouse create'] = """
    type: command
    short-summary: Create a Fabric Warehouse.
"""

###################################################################################################
#
# workspace
#
###################################################################################################

helps['fabric workspace'] = """
type: group
short-summary: Manage Fabric Workspaces.
"""

helps['fabric workspace create'] = """
    type: command
    short-summary: Create a Fabric Workspace.
"""

helps['fabric workspace list'] = """
    type: command
    short-summary: List Fabric Workspaces.
"""
