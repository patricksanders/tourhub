import spotify

def test_spotify_artist_search():
    artist = spotify.search_artist("dawes")
    assert artist is not None

def test_spotify_track_search():
    artist = spotify.search_track("dawes", "a little bit of everything")
    assert artist['uri'] == 'spotify:track:14wjwPgJCxk9uOfJMNVUwT'

def test_spotify_find_ids():
    sample_setlist = {
        "artist": "dawes",
        "tracks": [
            "a little bit of everything",
            "time spent in los angeles"
        ]
    }

    ids = spotify.find_setlist_tracks(sample_setlist)
    assert 'spotify:track:14wjwPgJCxk9uOfJMNVUwT' in ids

