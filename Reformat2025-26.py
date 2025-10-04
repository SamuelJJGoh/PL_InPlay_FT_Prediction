## decided to include the data for the current Premier League season (2025-26)
## file also downloaded from https://www.football-data.co.uk/englandm.php
## this csv file also needs reformatting, similar to 2024-25
## file only contains data up to the 6th game week, giving us 60 rows

import pandas as pd

data = pd.read_csv("raw_eng1_2025-26.csv")
data = data[["Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "HTHG", "HTAG"]]
data["Team 1"] = data["HomeTeam"]
data["FT"] = data["FTHG"].astype(str) + "-" + data["FTAG"].astype(str)
data["HT"] = data["HTHG"].astype(str) + "-" + data["HTAG"].astype(str)
data["Team 2"] = data["AwayTeam"]
data.drop(["HomeTeam", "AwayTeam", "FTHG", "FTAG", "HTHG", "HTAG"], axis=1, inplace=True)

data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y").dt.strftime("%a %b %d %Y")

data.to_csv("data/eng1_2025-26.csv", index=False)