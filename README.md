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
8. The SQLite database was updated at the command line to include a primary key and to apply the correct data type to each column.
9. The database contains the following columns:
index (primary key), id (spotify key), song_name, artist, pic_url, preview_url, decade, release_year, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, type, uri, track_href, analysis_url, duration_ms, time_signature
10. Starting from the Flask API that was covered in '10-Advanced-SQL\3\Activities\10-Ins_Flask_with_ORM', the homework associated with that lesson, and an example that Eli provided last week in class, we created our app to connect the SQLite DB (SpotifyDB) ot our javascript and html. The routes include rendering the pages for the homepage, by decade, and by musical feature (aka, attribute), a route that pulls all the data, one that pulls the distinct decade, and one that pulls the different musical features.
11. We created 3 javascript files, which link to 3 html pages (1 js to 1 html), and one css style sheet that is connected to all html pages.
   - The homepage displays a musical attribute dropdown, that when selected, populates ranges on a slider. Moving the slider to different positions leads to the sample song for that position in the range to begin playing. Next to the slider, the album cover, artist, and song name appear. While above the slider, the attribute and the value corresponding to the sample song appear. The definition that corresponds to the attribute becomes spotify green. There are also start and stop buttons to control the music manually.
   - The By Decade page displays histograms for each attribute within a decade, selected from a dropdown.
   - The By Musical Feature page displays a line plot with error bars to see how the mean and variance of a given musical feature changes across the decades.
12. All files to run the website are in the folder called 'website'. This includes the final SpotifyDB.sqlite file. All other folders are steps along the way in building up the final product. 
   

