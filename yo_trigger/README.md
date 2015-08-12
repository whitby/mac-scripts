Trigger Yo notifications from a munki postinstall script.

# How it works

This script installs:  
1. An empty file at `/Library/Management/Triggers/yo`  
2. A LaunchAgent that watches the above path  
3. A small bash script: `/usr/local/bin/yo-trigger`  

```bash
#!/bin/bash
MESSAGE=`(cat /tmp/yo-message)`
/usr/local/bin/yo -t "$MESSAGE" -i /tmp/yo-icon.png
```

To trigger a notification, deploy your message in a file called `/tmp/yo-message`, and optionally an icon, named `yo-icon.png`
Touch the `/Library/Management/Triggers/yo` file in a postinstall script to launch a notification. 

An example notification package:
https://github.com/whitby/mac-scripts/tree/master/yo_office2016

**Disclaimer:** This is a very simple and limited workaround. 
