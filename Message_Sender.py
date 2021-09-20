#Imports the json python module
import json
#Imports Request and urlopen from urllib.request
from urllib.request import Request, urlopen

#Your webhook url goes here
WEBHOOK_URL = 'ENTER HERE'

#Defines the code
def main():

    #Defines the headers
    headers = {
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
        }

    #Create a file called "message.txt" and write in the contents you would like to send. @everyone and @here works. This opens the file "message.txt".
    message = open("message.txt","r")

    #Defines the payload to be sent, the contents of the file to be sent are read.
    payload = json.dumps({'content': message.read()})

    #Defines the request
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)

    #Executes the request by opening the URL url
    urlopen(req)

#Executes the code
main()
