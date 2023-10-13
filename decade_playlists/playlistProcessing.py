import json

def processDecade(curr_data):
    id_str = ''
    i = 0
    song_dict = {}
    for item in curr_data['tracks']['items']:
        if i < 100:
            id_str += str(item['track']['id']) + ", "
            song_dict[str(item['track']['id'])] = str(item['track']['name'])
        i += 1
    print(id_str)
    return song_dict


decade_dict = {}
decade_files = ["the1950s.json", 'the1960s.json', 'the1970s.json', 'the1980s.json', 'the1990s.json', 'the2000s.json']
decades = ["1950s", '1960s', '1970s', '1980s', '1990s', '2000s']
for i in range(len(decades)):
    curr_file = open(decade_files[i])
    curr_data = json.load(curr_file)
    print("\n" + decades[i])
    decade_dict[decades[i]] = processDecade(curr_data)
with open("decades_dict.json", "w") as outfile:
    json.dump(decade_dict, outfile)