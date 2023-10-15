import json

decade_data =[]
decade_files = ["decade_playlists/the1950s.json", 'decade_playlists/the1960s.json', 'decade_playlists/the1970s.json', 'decade_playlists/the1980s.json', 'decade_playlists/the1990s.json', 'decade_playlists/the2000s.json']
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
            id_str += str(item['track']['id']) + ", "
            song_dict['id'] = str(item['track']['id'])
            song_dict['name'] = str(item['track']['name'])
            song_dict['decade'] = decades[i]
            decade_data.append(song_dict)
        j += 1
        print(id_str)

with open("decades_dict.json", "w") as outfile:
    json.dump(decade_data, outfile)