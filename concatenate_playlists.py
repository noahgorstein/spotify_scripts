import spotipy
from sys import argv
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth

# ###########################
# ON REPEAT PLAYLIST IDS
# ###########################
# OMRI - 37i9dQZF1Epk3rCnDbRzoW
# RYAN - 37i9dQZF1EpjwNta6kRS75
# JACK - 37i9dQZF1EpkeEt7H42BOM
# JORDAN - 37i9dQZF1EprSmFIIwNCNf
# BEN - 37i9dQZF1EpywHzaNngt66
# NOAH - 37i9dQZF1EpsXgi13RB1Os

def concat_playlists(playlists):
    for val in playlists:
        pl = sp.playlist(val)
        print("Processing --- Playlist ID:", val, " --- Name: ", pl["name"])

        offset = 0
        playlistDict = {}
        while True:
            playlist_items = sp.playlist_items(val,
                                               offset=offset,
                                               fields='items.track.id,total',
                                               additional_types=['track'])

            for playlist_item in playlist_items['items']:
                trackId = playlist_item['track']['id']
                trackObject = sp.track(trackId)
                playlistDict[trackId] = trackObject['name']

            if len(playlist_items['items']) == 0:
                break

            offset = offset + len(playlist_items['items'])

        for key, val in playlistDict.items():
            trackSet.add(key)


def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


if __name__ == '__main__':
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public"))
    if len(argv) < 4:
        print("Must provide at least 2 playlists to join")
    else:
        playlist_name = argv[1]
        playlists = argv[2:]

        # to avoid duplicates in playlist
        trackSet = set()

        concat_playlists(playlists)

        trackList = list(trackSet)
        print(trackList)

        # Noah user id: 1222971566
        playlist = sp.user_playlist_create(user="1222971566", name=playlist_name)
        playlistId = playlist['id']
        playlistHalf1, playlistHalf2 = split_list(trackList)
        sp.playlist_add_items(playlistId, playlistHalf1)
        sp.playlist_add_items(playlistId, playlistHalf2)
