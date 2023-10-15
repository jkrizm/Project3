# Project3
1. Created a Spotify account we could use to gather data from [Spotify's Web API](https://developer.spotify.com/documentation/web-api). This gave us the client ID and client secret that we could use to get our access token (using cURL command).
3. Used cURL to retrieve to gather the following playlists (playlist ID's found through Spotify)
   i. All Out 50s
   ii. All Out 60s
   iii. All out 70s
   iv. All out 80s
   v. All out 90s
   vi. All out 00s
5. Data was retrieved as JSON files. We processed the playlist data in Python to extract the track ID's. A dictionary of song ID to song title was created.
6. The comma-separated list of songs for each playlist (generated via the python code) was then processed to remove any spaces and entered into cURL commands to retrieve track audio features.
7. To convert data to a SQLite database, we used the website https://www.convertcsv.com/json-to-csv.htm to convert JSON files to CSV files.
