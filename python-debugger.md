The Python debugger in VS Code is a powerful tool and allows for much more fine-grained debugging than a series of print statements or inserted breakpoints.

However, getting going with the debugger can be a bit confusing - especially on the DSI Cluster and in situations when you need to pass command line arguments to your script.

## Using the VS Code Python Debugger on the Cluster

In order to use the VS Code Python debugger on the cluster, you need to set up a `launch.json` file. You should be prompted to do this the first time you launch the debugger (`F5`).

To edit the file, you can click the settings gear in the VS Code debugger menu or you can edit it directly in the `.vscode` directory in the root of the folder that you've opened in VS Code.

`launch.json` should look something like this:
```
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: script_name.py",
            "type": "python",
            "request": "launch",
            "cwd": "${workspaceFolder}/directory/you/want/to/run/commands/from",
            "program": "${workspaceFolder}/path/to/script.py",
            "args": [
                "--command_line_arg_1",
                "arg_1_value",
                "--command_line_arg_2,
                "arg_2_value",
            ],
            "env": {
                "MY_ENV_VAR": "value"
            },
            "console": "integratedTerminal"
        }
    ]
}
```

Next, you can insert breakpoints by clicking on the left of the script in the VS Code editor (you should see a red dot appear).

From there, you should be able to run the debugger as normal and see the state of your program at any step.