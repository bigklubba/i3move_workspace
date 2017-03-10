#!/usr/bin/env python3

import i3ipc
import sys

if len(sys.argv) != 3:
    print("usage: i3move_workspace <workspace_number> <output>")
    exit(1)

workspace_number = sys.argv[1]
output = sys.argv[2]
i3 = i3ipc.Connection()

outputs = i3.get_outputs()
workspaces = i3.get_workspaces()
workspace_name = ""
for workspace in workspaces:
    if (str(workspace['num']) == workspace_number):
        workspace_name = workspace['name']
        break

if not workspace_name:
    print("could not find workspace")
    exit(1)

i3.command('workspace %s' % workspace_name)
i3.command('move workspace to output %s' % output)
