"""import requests

url = "https://chukul.com/api/data/v2/daily-stock/"
response = requests.get(url = url)
data = response.json()
"""

import mysql.connector
import requests
import csv

url = "https://chukul.com/api/data/v2/daily-stock/"
response = requests.get(url)
# data = response.json()


# csv write
headers = ["Symbol", "LTP", "Percentage Change", "Volume"]
data_to_dump = response.json()


with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data_to_dump)

db = mysql.connector.connect(host="localhost", username="root", database="stocks_data")


print(db)
