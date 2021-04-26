#!/bin/bash
clear
echo "
_ __  __ _______ _    _  ____  _   _
      | |  \/  |__   __| |  | |/ __ \| \ | |
      | | \  / |  | |  | |__| | |  | |  \| |
  _   | | |\/| |  | |  |  __  | |  | | . ` |
 | |__| | |  | |  | |  | |  | | |__| | |\  |
  \____/|_|  |_|  |_|  |_|  |_|\____/|_| \_|

"
# Termux session string generator for TeleBot
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Jasem-muhammad/JMTHON/main/telesetup.py
pip install telethon
python telesetup.py
