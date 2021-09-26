# Spotify Scripts

A collection of utility scripts to do some cool stuff with Spotify. 

## Prerequisites

- Setup an application in [Spotify's Developer Dashboard](https://developer.spotify.com/dashboard/).
	- In your application, set valid redirect URIs required for the [Authorization Code Flow](https://spotipy.readthedocs.io/en/2.16.1/?highlight=scope#authorization-code-flow).
- Install [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/?highlight=scope#).

	```
	pip3 install spotipy
	```

## `concatenate_playlists.py`

First argument to the script is the playlist name. The remaining arguments are Spotify playlist IDs. 

- Example Usage:

	```
	python3 concatenate_playlists.py playlistName playlistId1 playlistId2 playlistId3 
	```
