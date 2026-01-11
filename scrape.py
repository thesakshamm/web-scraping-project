
"""import requests

url = "https://chukul.com/api/data/v2/daily-stock/"
response = requests.get(url = url)
data = response.json()
"""



import requests
import csv

url = "https://chukul.com/api/data/v2/daily-stock/"
response = requests.get(url)
data = response.json()

with open("stocks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # header (you decide meaning of each index)
    writer.writerow(["symbol", "ltp", "percentageChange", "volume"])

    for row in data:
        writer.writerow(row)

    

