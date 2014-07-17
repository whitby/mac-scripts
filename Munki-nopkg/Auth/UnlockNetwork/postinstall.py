#!/usr/bin/env python

import subprocess
import sys
import plistlib
import platform

# Group System Preferences should be opened to
group = 'everyone'

# Get the OS Version
v = platform.mac_ver()[0][:4]

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.services.systemconfiguration.network']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()
formatted = plistlib.readPlistFromString(out)

# If we're on 10.9 and the group doesn't match, we're going to correct it.
if v == '10.9':
    if formatted['group'] != group:
        formatted['group'] = group
        # Convert back to plist
        input_plist = plistlib.writePlistToString(formatted)
        # Write the plist back to the authorizationdb
        command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.services.systemconfiguration.network']
        task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err) = task.communicate(input=input_plist)

# If we're on 10.8 and the rule doesn't match, we're going to correct it.
if v == '10.8':
    if formatted['rule'] != 'allow':
        formatted['rule'] = 'allow'
        # Convert back to plist
        input_plist = plistlib.writePlistToString(formatted)
        # Write the plist back to the authorizationdb
        command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.services.systemconfiguration.network']
        task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (out, err) = task.communicate(input=input_plist) 

command = ['/usr/bin/security', 'authorizationdb', 'read', 'system.preferences.network']

task = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, err) = task.communicate()
formatted = plistlib.readPlistFromString(out)

# If the group doesn't match, we're going to correct it.
if formatted['group'] != group:
    formatted['group'] = group
    # Convert back to plist
    input_plist = plistlib.writePlistToString(formatted)
    # Write the plist back to the authorizationdb
    command = ['/usr/bin/security', 'authorizationdb', 'write', 'system.preferences.network']
    task = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = task.communicate(input=input_plist)