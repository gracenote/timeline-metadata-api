timeline-metadata-api
=====================

Gracenote's Timeline Metadata API gives developers access to detailed information about a track. The API currently returns four types of features for an uploaded track: beats, BPM, segments and moods.

Using the API
-------------
To get information from a track you must first post the audio file to the API. The Post request will immediately return a JSON object with an id for the uploaded track. To access the features once they're analyzed, you will need to send a subsequent request to http://devapi.gracenote.com/v1/timeline/ .

Posting audio
-------------
To analyze a file, you must send an HTTP Post request to http://devapi.gracenote.com/v1/timeline/ with a form paramater "filename" that stores the data of the audio file.

The post request will return a JSON object that has "id" and "progress" fields. The id will be used to retrieve the features once they have been processed by submitting an HTTP Get request to http://devapi.gracenote.com/v1/timeline/<id> . The analysis may take up to several minutes to complete. The "progress" field will tell you how far along the processing is. The API can handle uploads of the following file types: wav, mp3, mp4, aac, ogg, flac.

Retrieving feature data
-----------------------
As described above, once a track has been uploaded you can get the feature data by sending an HTTP Get request to http://devapi.gracenote.com/v1/timeline/<id>, where <id> is the id returned by the Post request.

When the processing has completed, this Get request will return a JSON object with a key, "features", that stores the. Timeline Metadata features. The features are labeled "BPM", "BEATS", "MOODS", and "SEGMENT".

BPM stores the predicted tempo. BEATS stores an array of beat times.

MOODS stores an array of dictionaries that have a START, END, and mood TYPE. TYPE is a dictionary that stores pairs of moods and weights of the three most prominent moods for that time range.

The SEGMENT object stores an array of dictionaries that describe the structure of the song. Each dictionary has START, END, TEXT and TYPE keys. START and END define the location of the segment in the song. TYPE will either be "Chorus", "Verse" or a lowercase character. Segments that are very similary musically will have the same TYPE.

Examples
--------
##Curl

`curl -F "audiofile=@yuck.mp3" http://devapi.gracenote.com/v1/timeline/ `
 
 ```json
 {
  "filename": "yuck.mp3", 
  "id": 2, 
  "name": "", 
  "progress": 0, 
  "size": "", 
  "status": 1
}
```
 
`curl http://devapi.gracenote.com/v1/timeline/2`

```json

"features": {
    "BEATS": [
      0.13700000942, 
      0.58500003815, 
      1.0330001116,
      ...],
    "BPM": [
      134.232956
    ],
    "MOODS": [
      {
        "END": 1.5,
        "START": 0,
        "TYPE": {
          "Brooding": 61,
          "Fun": 27,
          "Sensual": 8
        }
      },
      {
        "END": 2.5,
        "START": 1.5,
        "TYPE": {
          "Brooding": 75,
          "Fun": 7,
          "Rowdy": 11
        }
      }, ...],
      "SEGMENT": [
      {
        "END": 30.96,
        "START": 0.0,
        "TEXT": "Part A",
        "TYPE": "a"
      },
      {
        "END": 50.4,
        "START": 30.96,
        "TEXT": "Part B",
        "TYPE": "b"
      }, ...],
      "filename": "yuck.mp3",
      "id": "2",
      "progress": "1.0",
      "status": "0"}
```



##Python

```python

import requests
from time import sleep
import pdb

url = "http://devapi.gracenote.com/v1/timeline/"
file_path = 'path_to_file.mp3'
resp = requests.post(url,files={'audiofile':open(file_path,'rb')})
jresp = resp.json()
file_id = jresp['id']

progress = float(jresp['progress'])

while progress < 1:
    sleep(10)
    resp = requests.get(url + str(file_id) +'/')
    jresp = resp.json()
    progress = float(jresp['progress'])

feats = jresp['features']

# print the tempo                                                                                                                                               
print feats['BPM']

# find the first chorus                                                                                                                                          
for i in feats['SEGMENT']:
    if i['TYPE']=='Chorus':
	break
print i['START'], i['END']


```

Download the [example script](example.py) .
