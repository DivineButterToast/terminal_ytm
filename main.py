import sys
assert sys.version_info >= (3, 10)
import os
os.chdir(os.getcwd())
import json 
import subprocess                                                                                                                              
from ytmusicapi import YTMusic
import mpv
yt = YTMusic('oauth.json')
print("How many results would you like to see?")
print("1. most")
print("2. more")
print("3. less")
print("4. least")
user_result_length = input("enter reply: ")
while True:
    if (user_result_length == "1" or user_result_length == "most"):
        user_result_length = None
        break
    elif (user_result_length == "2" or user_result_length == "more"):
        user_result_length = 9999
        break
    elif (user_result_length == "3" or user_result_length == "less"):
        user_result_length = 4999
        break
    elif (user_result_length == "4" or user_result_length == "least"):
        user_result_length = 999
        break
    else:
        user_result_length = input("please enter a valid reply: ")

user_input = input("search for a song: ")
data_0 = yt.search(user_input, 'songs', None, 1, True)
data_1 = json.dumps(data_0, indent=4)
start_index = 0                                                                                                        
end_index = user_result_length                                                                                                           
if (user_result_length != None): 
    result = data_1[start_index:end_index]
    data_1 = result    
substring_0 = "category"                                                                                                                                                            
substring_1 = "feedbackTokens"
substring_2 = "videoId"
substring_3 = "duration_seconds"
pointer = 0
count = 0
data_tmp = data_1
while True:       # loop to print occurances                                                                                                                                                                  
    key_0 = data_tmp.find(substring_0,pointer)
    value_0 = data_tmp.find(substring_1,pointer)
    key_1 = data_tmp.find(substring_2,pointer)
    value_1 = data_tmp.find(substring_3,pointer)
    if (value_0 == -1 or value_1 == -1):  
        break                                                                                                                             
    data_tmp_1 = data_tmp[key_0:value_0] + "" + data_tmp[key_1:value_1]
    if (count % 2 == 0):  #avoids duplicates, there could be a better way to do this                                                                                                                                      
        print(data_tmp_1)                                                                                                                                        
    pointer = min(key_1, value_1) + 1 #this is likely the key to better way mentioned above
    count = count + 1
#slice link from songs video id
user_input = input("enter videoId of the song: ")
search_results = yt.get_song(user_input)
song_data = json.dumps(search_results, indent=4)
substring_0 = "iosAppArguments"
substring_1 = "ogType"
substring_2 = '",'
key_0 = song_data.find(substring_0) + len(substring_0) + 4                                                                                                 
value_0 = song_data.find(substring_1) - 1                                                                                              
result_tmp = song_data[key_0:value_0]
value_0 = result_tmp.find(substring_2)
song_to_play = result_tmp[:value_0]

#playing the selection - originally calling through bash
#player_data = subprocess.check_output("mpv --no-video " + song_to_play, shell=True)             
#print(player_data.decode())

#necessary, I encountered errors when importing this in the beginning
import locale
locale.setlocale(locale.LC_NUMERIC, 'C')
user_player = mpv.MPV(ytdl=True, video=False)
user_player.play(song_to_play)
user_player.wait_for_playback()                                                           
                                                                                             
                                                                                                                                        
