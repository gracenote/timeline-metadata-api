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

curl -F "audiofile=@name\_of\_file.mp3" http://devapi.gracenote.com/v1/timeline/
curl http://devapi.gracenote.com/v1/timeline/<id>


##Python
[example script](example.py)
