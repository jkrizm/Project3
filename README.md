# Project3
1. Created a Spotify account we could use to gather data from [Spotify's Web API] (https://developer.spotify.com/documentation/web-api)
2. Used cURL to retrieve out token and proceed to gather the following playlists (playlist ID's found through Spotify)
   i. All Out 50s
   ii. (need to add the rest)
4. Data was retrieved as JSON files. We processed the playlist data in Python to extract the track ID's. A dictionary of song ID to song title was created.
5. We then used the generated comma-separated lists of songs to retrieve track audio features.
6. To convert data to a SQLite database, we used the website https://www.convertcsv.com/json-to-csv.htm to convert JSON files to CSV files.
