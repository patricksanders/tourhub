import requests
import json
import math
import difflib

url_base = "http://api.setlist.fm/rest/0.1/"
client = requests.session()

"""
So, this says get_mbid, like a single mbid, so I think we 
should cleanse this and return the closest mbid to it, if 
something is set as such.
"""
def get_mbid(artist_name, closest=False):
    query = {"artistName":artist_name}
    res_id="search/artists.json"
    url = "".join( [url_base, res_id] )
    r = client.get(url, params=query)
    j = json.loads(r.text)
    j = j['artists']['artist']
    j = { element['@name'] : element['@mbid'] for element in j }
    if match is True:
        matches = j.keys()
        closest = difflib.get_close_matches(artist_name, matches, 1)[0]
        j = j[closest]
    return j

def get_setlists(mbid):
    finished = False
    page = 1
    j = json.loads('[]')
    while not finished:
        setlists, finished = _setlist_query(mbid, page)
        
        j.append(setlists)
        page += 1

    return j

def _setlist_query(mbid, page):
    res_id = "artist/" + mbid  + "/setlists.json?p=" + str(page)
    url = "".join( [url_base, res_id] )
    r = client.get(url)
    j = json.loads(r.text)

    page = int(j['setlists']['@page'])
    total_items = float(j['setlists']['@total'])
    items_per_page = float(j['setlists']['@itemsPerPage'])

    j = j['setlists']['setlist']
    if page < math.ceil(total_items / items_per_page):
        done = False
    else:
        done = True
    j = { element['@id'] : element['sets'] for element in j }
    return j, done
    
    
