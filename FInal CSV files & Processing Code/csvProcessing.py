import pandas as pd

songs_df = pd.read_csv('Final CSV files & Processing Code/decade_dict.csv')
atrributes_df = pd.read_csv('Final CSV files & Processing Code/songs1950s.csv')
attributes_files = ["Final CSV files & Processing Code/songs1960s.csv", "Final CSV files & Processing Code/songs1970s.csv", "Final CSV files & Processing Code/songs1980s.csv", "Final CSV files & Processing Code/songs1990s.csv", "Final CSV files & Processing Code/songs2000s.csv"]
for i in range(len(attributes_files)):
    curr_df = pd.read_csv(attributes_files[i])
    atrributes_df = atrributes_df.append(curr_df)
complete_df = pd.merge(songs_df, atrributes_df, on='id')
complete_df.to_csv('final.csv', index=False)