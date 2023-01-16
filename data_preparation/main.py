import pandas as pd
import json

# ################################### process_match_summary (result) ###########################################

with open('t20_json_files/t20_wc_match_results.json') as f_match:
    data_match = json.load(f_match)
df_match = pd.DataFrame(data_match[0]['matchSummary'])
# print(df_match.head(5))

# print(f'how many elements are there')
# print(df_match.shape)

# renaming scorecard as match_id
df_match.rename({'scorecard': 'match_id'}, axis=1, inplace=True)
# print(df_match.head(5))

# create a match_id that maps team names to a unique match_id.
match_ids_dict = {}
for index, row in df_match.iterrows():
    key1 = row['team1'] + ' Vs ' + row['team2']
    key2 = row['team2'] + ' Vs ' + row['team1']
    match_ids_dict[key1] = row['match_id']
    match_ids_dict[key2] = row['match_id']

# print(match_ids_dict)
df_match.to_csv('t20_csv_files/dim_match_summary.csv', index=False)

# ################################### process_batting_summary (result) ###########################################


with open('t20_json_files/t20_wc_batting_summary.json') as f_batting:
    data_batting = json.load(f_batting)
    all_records_batting = []

    for rec_batting in data_batting:
        all_records_batting.extend(rec_batting['battingSummary'])  # putting them in list

# Fetching only batting summary data and making that as an array of batting summary
df_batting = pd.DataFrame(all_records_batting)

# adding new column called out or not_out
df_batting['out/not_out'] = df_batting.dismissal.apply(lambda x: 'out' if len(x) > 0 else 'not_out')
# print(df_batting.head(10))

# Drop the column dismissal
df_batting.drop(columns='dismissal', inplace=True)
# print(df_batting.head(10))

# Removing special characters in cricketer's name
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace('\xa0', ''))
df_batting['batsmanName'] = df_batting['batsmanName'].apply(lambda x: x.replace('†', ''))

# adding col match_id to the table batting_summary by matching 'match' col
# print(df_batting.columns)

# added extra column called match_id by comparing match from dict
df_batting['match_id'] = df_batting['match'].map(match_ids_dict)
# print(df_batting.head(10))

# export table
df_batting.to_csv('t20_csv_files/fact_bating_summary.csv', index=False)


# ################################### process_bowling_summary (result) ###########################################

with open('t20_json_files/t20_wc_bowling_summary.json') as f_bowling:
    data_bowling = json.load(f_bowling)
    all_records_bowling = []
    for rec_bowling in data_bowling:
        all_records_bowling.extend(rec_bowling['bowlingSummary'])
# print(all_records_bowling[:2])

df_bowling = pd.DataFrame(all_records_bowling)
# print(df_bowling.shape)
# print(df_bowling.head(10))

df_bowling['match_id'] = df_bowling['match'].map(match_ids_dict)
# df_bowling.head()

df_bowling.to_csv('t20_csv_files/fact_bowling_summary.csv', index=False)

# ################################### process_batting_summary (result) ###########################################


with open('t20_json_files/t20_wc_player_info.json') as f_player:
    data_player = json.load(f_player)

df_player = pd.DataFrame(data_player)
# df_player.head(10)
# print(df_player.shape)

# Cleanup special characters in name
df_player['name'] = df_player['name'].apply(lambda x: x.replace('â€', ''))
df_player['name'] = df_player['name'].apply(lambda x: x.replace('†', ''))
df_player['name'] = df_player['name'].apply(lambda x: x.replace('\xa0', ''))
# df_player.head(10)

# print(df_player.columns)

df_player.to_csv('t20_csv_files/dim_players_no_images.csv', index=False)
