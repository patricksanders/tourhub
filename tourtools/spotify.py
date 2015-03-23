import spotipy

sp = spotipy.Spotify()

# Search Spotify and make list of URIs for a setlist.
# Expects dict of form:
# {
#   artist: foo,
#   tracks: [bar, baz, bah]
# }
def find_setlist_tracks(setlist):
    artist = setlist['artist']
    track_ids = []
    for track in setlist['tracks']:
        result = search_track(artist, track)
        track_ids.append(result['uri'])
    return track_ids

# Do a Spotify search for an artist.
# Returns a list of search results.
def search_artist(artist_name):
    return search(artist_name, "artist")['artists']['items']

# Do a Spotify search for a particular song.
# Returns a single track object.
def search_track(artist_name, track_name):
    query = artist_name + " " + track_name
    return search(query, "track", 1)['tracks']['items'][0]

# Perform Spotify search
# term: search term
# search_type: album, artist, track, or playlist
# limit: a number
def search(term, search_type, limit=10):
    j = sp.search(q=term, type=search_type, limit=limit)
    return j

