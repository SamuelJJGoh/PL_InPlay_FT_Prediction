"""
The csv files containing the historical records for the Premier League seaons from 
2018-19 to 2023-24 can be downloaded from the 'footballcsv repository on GitHub. Each file 
has the following columns : 
    
    Date, Team 1 (home team), FT (final score), HT (half-time score), Team 2 (away team).

The data for the 2024-25 season was downloaded from https://www.football-data.co.uk/englandm.php 
as 'raw_eng1_2024-25.csv'. However, this file was not yet formatted consistently with the previous 
seasons. Therefore, it was reformatted and saved as 'eng1_2024-25.csv'.

Each csv file contains 380 rows as there are 10 games per game week, with the season lasting 38 game weeks.
"""

import pandas as pd

data = pd.read_csv("raw_eng1_2024-25.csv")
data = data[["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "HTHG", "HTAG"]]
data["Team 1"] = data["HomeTeam"]
data["FT"] = data["FTHG"].astype(str) + "-" + data["FTAG"].astype(str)
data["HT"] = data["HTHG"].astype(str) + "-" + data["HTAG"].astype(str)
data["Team 2"] = data["AwayTeam"]
data.drop(["HomeTeam", "AwayTeam", "FTHG", "FTAG", "HTHG", "HTAG"], axis=1, inplace=True)

data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y").dt.strftime("%a %b %d %Y")

compared_data = pd.read_csv("data/eng1_2023-24.csv")

print(data)
print(data.dtypes) # all object type
print(compared_data)
print(compared_data.dtypes) # all object type

data.to_csv("data/eng1_2024-25.csv", index=False)