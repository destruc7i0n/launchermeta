# launchermeta

This is a library that will interact with version_manifest.json

```python
from launchermeta import LauncherMeta

lm = LauncherMeta()

# get latest release
latest_release = lm.get_latest_release()
client = latest_release.get_client_download()
client.download_to('/tmp') # download the client

# get specific release
latest_release = lm.get_version_by_id('1.9')
client = latest_release.get_client_download()
client.download_to('/tmp') # download the client
```

#### Note
There are other functions in the code itself, feel free to look there for a specific function that you need.