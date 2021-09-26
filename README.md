# Spotify Scripts

A collection of utility scripts to do some cool stuff with Spotify. 

- [Prerequisites](#prerequisites)
- [Scripts](#scripts)
  - [`concatenate_playlists.py`](concatenate_playlistspy) 

## Prerequisites

- Setup an application in [Spotify's Developer Dashboard](https://developer.spotify.com/dashboard/). You must have a Spotify Premium account to do so.
	- In your application, set redirect URIs required for the [Authorization Code Flow](https://spotipy.readthedocs.io/en/2.16.1/?highlight=scope#authorization-code-flow). The URI does not need to be a valid web address (i.e. `http://localhost:9090` is fine).

<img width="578" alt="Screen Shot 2021-09-26 at 11 25 47 AM" src="https://user-images.githubusercontent.com/23270779/134814129-a5eb1d1c-82ea-4a02-a40e-e993b96bcaee.png">


- Install [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/?highlight=scope#).

	```zsh
	pip3 install spotipy
	```
- Set the environment variable `SPOTIPY_REDIRECT_URI` equal to what was set in for your application in the Spotify Developer Dashboard.

	```zsh
	export SPOTIPY_REDIRECT_URI="http://localhost:9090"
	```

## Scripts

### `concatenate_playlists.py`

#### Script Arguments

1. Playlist name
2. The remaining arguments are Spotify playlist IDs. 

- Example Usage:

	```
	python3 concatenate_playlists.py playlistName playlistId1 playlistId2 playlistId3 
	```
