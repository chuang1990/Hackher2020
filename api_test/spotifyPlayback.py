"""
spotifyPlayback.py
Part of code for HackHer413
Sents Request code to start a playlist playback on Bose SoundTouch
Author: Catherine Huang
Date: 02-09-2020
"""
import requests
import xml.dom.minidom

# set the params:
ipaddr = "192.168.1.92" # enter your speaker IP address here
uri = "/playback/container/c3BvdGlmeTpwbGF5bGlzdDozN2k5ZFFaRjFEWGNCV0lHb1lCTTVN"
spotify_account = "animaniac1911"
service = "That word..."
reason = "...it does not mean..."
message = "...what you think it means."
key = "0k0RQaOC1nTLHX1DbHZRXNnBpjAlZOTH" # enter your API key here
volumeVal = "20" # enter volume here, a number between 10 and 70

# set volume for the playback
sendXML = "<volume>" + volumeVal + "</volume>"
send = requests.post("http://" + ipaddr + ":8090/volume", data = sendXML)
# form and send the /speaker POST request
sendXML = '<ContentItem source= "SPOTIFY" location = "%s" sourceAccount = "%s" type = "tracklisturl"></ContentItem>' %(uri, spotify_account)
send = requests.post('http://' + ipaddr + ':8090/select', data=sendXML, headers = {'Content-Type': 'text/xml'})

# send = requests.get('http://' + ipaddr + ':8090/now_playing')

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
# print (responseXML_pretty)

send = requests.get('http://' + ipaddr + ':8090/volume')

responseXML = xml.dom.minidom.parseString(send.text)
responseXML_pretty = responseXML.toprettyxml()
# print (responseXML_pretty)
