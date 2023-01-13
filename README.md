# VIT Wifi Autologin
This is a super simple python script I made to quickly login to VIT's Hostel Wifi. Once installed, just hit ```Win+R``` and then ```wifi``` to run.
# Installation
This script requires ```python-dotenv``` and ```requests``` library to run. Run ```pip install python-dotenv requests``` if you don't have it. 

## Windows:
- For manual installation: Copy the ```setup.py```,```main.py``` and ```wifi.bat``` files to "C:\Windows\Users\YourName\vit-wifi-autologin\" and then run ```setup.py```.
- For quick setup and install, run this command in a powershell with administrator privileges and follow the prompts:
```ps
New-Item -ItemType "directory" -Path "$HOME\vit-wifi-autologin"; Invoke-WebRequest -Uri "https://github.com/Seudonym/vit-wifi-autologin/raw/master/main.py" -Outfile "$HOME\vit-wifi-autologin\main.py";  Invoke-WebRequest -Uri "https://github.com/Seudonym/vit-wifi-autologin/raw/master/setup.py" -Outfile "$HOME\vit-wifi-autologin\setup.py";  Invoke-WebRequest -Uri "https://github.com/Seudonym/vit-wifi-autologin/raw/master/wifi.bat" -Outfile "$HOME\wifi.bat"; python "$HOME\vit-wifi-autologin\setup.py"; rm "$HOME\vit-wifi-autologin\setup.py"
```
⚠️⚠️⚠️WARNING!!! DON'T RUN COMMANDS OR SCRIPTS FROM UNTRUSTED SOURCES UNLESS YOU KNOW WHAT YOU'RE DOING⚠️⚠️⚠️
