import pandas as pd

songs_df = pd.read_csv('processing/decade_dict.csv')
atrributes_df = pd.read_csv('processing/songs1950s.csv')
attributes_files = ["processing/songs1960s.csv", "processing/songs1970s.csv", "processing/songs1980s.csv", "processing/songs1990s.csv", "processing/songs2000s.csv"]
for i in range(len(attributes_files)):
    curr_df = pd.read_csv(attributes_files[i])
    atrributes_df = atrributes_df.append(curr_df)
complete_df = pd.merge(songs_df, atrributes_df, on='id')
complete_df.to_csv('final.csv', index=False)