import requests
import xml.dom.minidom
import math
from bs4 import BeautifulSoup as bs

# set the params:

ipaddr = "192.168.1.92" # enter your speaker IP address here
macaddr = "7C-01-0A-5C-D4-E1"
url = "https://freesound.org/data/previews/275/275571_4486188-hq.mp3" # enter the URL of the file you want to play here
service = "That word..."
reason = "...it does not mean..."
message = "...what you think it means."
key = "0k0RQaOC1nTLHX1DbHZRXNnBpjAlZOTH" # enter your API key here
volumeVal = "40" # enter volume here, a number between 10 and 70

# form and send the /speaker POST request
send = requests.get('http://' + ipaddr + ':8090/volume')
responseXML = xml.dom.minidom.parseString(send.text)
volume_tag = responseXML.getElementsByTagName('volume')
#targetvolume_tag = volume_tag.getElementsByTagName('targetvolume')
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
print(volume_tag[0].childNodes[0].firstChild.nodeValue)
volumeVal = volume_tag[0].childNodes[0].firstChild.nodeValue

updated_volume = str(math.floor(int(volumeVal)/2))
print(updated_volume)
#sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
#send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

send = requests.get('http://' + ipaddr + ':8090/now_playing')
responseXML = bs(send.text, 'html.parser')
# responseXML = xml.dom.minidom.parseString(send.text)
# responseXML_pretty = responseXML.toprettyxml()
print (responseXML.prettify())

# send = requests.get('http://' + ipaddr + ':8090/select')
# responseXML = xml.dom.minidom.parseString(send.text)
# responseXML_pretty = responseXML.toprettyxml()
# print (responseXML_pretty)

keystate = "press"
keyvalue = "PAUSE"
sendXML = "<key state=\""+ keystate + "\" sender=\"Gabbo\">"+keyvalue+"</key>"
send = requests.post('http://' + ipaddr + ':8090/key', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)


sendXML = "<volume>"+updated_volume+"</volume>"
send = requests.post('http://' + ipaddr + ':8090/volume', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)

sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
send = requests.post('http://' + ipaddr + ':8090/speaker', data=sendXML)

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
print (responseXML_pretty)
