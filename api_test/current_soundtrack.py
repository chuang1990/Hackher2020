import requests
import xml.dom.minidom


# set the params:

ipaddr = "192.168.1.92" # enter your speaker IP address here
url = "http://www.nasa.gov/mp3/590331main_ringtone_smallStep.mp3" # enter the URL of the file you want to play here
service = "That word..."
reason = "...it does not mean..."
message = "...what you think it means."
key = "0k0RQaOC1nTLHX1DbHZRXNnBpjAlZOTH" # enter your API key here
volumeVal = "30" # enter volume here, a number between 10 and 70

# form and send the /speaker POST request

sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

# print a pretty version of the response - not required but can be helpful for reading errors if they occur

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
