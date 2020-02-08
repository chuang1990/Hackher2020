import requests
import xml.dom.minidom
from bs4 import BeautifulSoup as bs

# # get list of song from playlist
# r_playlist = "https://api.spotify.com/v1/playlists/6rqhFgbbKwnb9MLmUQDhG6/tracks"
# get = requests.get(r_playlist)
# soup = bs(get.text,'html.parser')
# print(soup)
# song_list=soup.find_all('a',{'class':'pl-video-title-link'})
# # print(song_list)
# song_urls = []
# for l in song_list:
#     song_urls.append(l.get("href"))
# # print(song_list)

# # responseXML = xml.dom.minidom.parseString(send.text)
# # responseXML_pretty = responseXML.toprettyxml()
# # print(responseXML_pretty)

play_sound = False

if play_sound:
    # for
    ip_addr = "192.168.1.92"
    url = "https://www.youtube.com/watch?v=LZiBVEyJl1E" # enter the URL of the file you want to play here
    
    # print("https://www.youtube.com" + song_urls[0])
    # url = "https://www.youtube.com" + song_urls[0]
    service = "That word..." 
    reason = "...it does not mean..."
    message = "...what you think it means."
    key = "0k0RQaOC1nTLHX1DbHZRXNnBpjAlZOTH" # enter your API key here 
    volumeVal = "40" # enter volume here, a number between 10 and 70

    # form and send the /speaker POST request
    sendXML = "<play_info><app_key>" + key + "</app_key><url>" + url + "</url><service>" + service + "</service><reason>" + reason + "</reason><message>" + message + "</message><volume>" + volumeVal + "</volume></play_info>"
    
    # sendXML = "<play_info><app_key>" + key + "</app_key><now_playing></now_playing></play_info>"
    send = requests.post('http://' + ip_addr + ':8090/speaker', data=sendXML)

    # print a pretty version of the response - not required but can be helpful for reading errors if they occur

    responseXML = xml.dom.minidom.parseString(send.text)
    responseXML_pretty = responseXML.toprettyxml()
    print (responseXML_pretty)  