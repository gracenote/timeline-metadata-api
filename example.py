import requests
from time import sleep
import pdb

url = "http://devapi.gracenote.com/v1/timeline/"
resp = requests.post(url,files={'audiofile':open('shady.mp3','rb')})
jresp = resp.json()
id = jresp['id']

progress = float(jresp['progress'])

while progress < 1:
    sleep(10)
    resp = requests.get(url + str(id) +'/')
    jresp = resp.json()
    progress = float(jresp['progress'])

feats = jresp['features']

# print the tempo
print feats['BPM']

#find the first chorus
for i in feats['SEGMENT']:
    if i['TYPE']=='Chorus':
        break
print i['START'], i['END']


