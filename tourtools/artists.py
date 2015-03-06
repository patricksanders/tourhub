import requests
import json

url_base = "http://api.setlist.fm/rest/0.1/"
client = requests.session()

def get_mbid(artist_name):
    query = {"artistName":artist_name}
    res_id="search/artists.json"
    url = "".join( [url_base, res_id] )
    r = client.get(url, params=query)
    j = json.loads(r.text)
    j = j['artists']['artist']
    j = { element['@name'] : element['@mbid'] for element in j }
    return j

    
