## Installing Large Conda Environments on the DSI Cluster

The DSI Cluster limits each user to 50GB of space in their home directory. This is enough space for most purposes, but sometimes installing large Conda environments (especially for machine learning projects) takes up more space than this during the installation process - even if the final environment is only a few gigabytes.

In order to work around this, you can change the `TMPDIR` environment variable to use the `/net/scratch` directory for tempororary files created while building the environment.

To temporarily change `TMPDIR`, run the following command:
```
export TMPDIR=/net/scratch/<your_username>/tmp
```

If you want to set `TMPDIR` permanently, you can add the above command to your `.bashrc` file in your home directory. (You can add it anywhere in the file).

To check that `TMPDIR` was set correctly, run the following command:
```
echo $TMPDIR
```

You should see the path to the temporary directory that you specified.

