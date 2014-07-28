```
sudo hdiutil create -srcfolder Umbrella UmbrellaRoamingClient.dmg
munkiimport --subdirectory=whitby/opendns UmbrellaRoamingClient.dmg --item="RoamingClient_MAC_1.5.25.pkg" --destinationpath="/tmp/umbrella" --catalog testing --unattended-install --installcheck_script="./installcheck_script" --postinstall_script="./postinstall_script"
```
