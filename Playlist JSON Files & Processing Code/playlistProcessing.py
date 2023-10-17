import json

decade_data =[]
decade_files = ["Playlist JSON Files & Processing Code/the1950s.json", 'Playlist JSON Files & Processing Code/the1960s.json', 'Playlist JSON Files & Processing Code/the1970s.json', 'Playlist JSON Files & Processing Code/the1980s.json', 'Playlist JSON Files & Processing Code/the1990s.json', 'Playlist JSON Files & Processing Code/the2000s.json']
decades = [1950, 1960, 1970, 1980, 1990, 2000]
for i in range(len(decades)):
    curr_file = open(decade_files[i])
    curr_data = json.load(curr_file)
    id_str = ''
    j = 0
    for item in curr_data['tracks']['items']:
        song_dict = {}
        print("\n" + str(decades[i])+"s")
        if j < 100:
            curr_track = item['track']
            id_str += curr_track['id'] + ", "
            song_dict['id'] = curr_track['id']
            song_dict['song_name'] = curr_track['name']
            song_dict['artist'] = curr_track['artists'][0]['name']
            song_dict['pic_url'] = curr_track['album']['images'][0]['url']
            song_dict['preview_url'] = curr_track['preview_url']
            song_dict['decade'] = decades[i]
            if curr_track['album']['release_date_precision'] != 'year':
                song_dict['release_year']  = curr_track['album']['release_date'].split('-')[0]
            else:
                song_dict['release_year'] = curr_track['album']['release_date']
            decade_data.append(song_dict)
        j += 1
        print(id_str)

with open("decades_dict.json", "w") as outfile:
    json.dump(decade_data, outfile)