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


terminal = db.cursor()
sql = "INSERT into stocks1 (sym,ltp,percentage_change,volume) VALUES (%s, %s,%s ,%s)"


# sql execution


terminal.execute("TRUNCATE TABLE stocks1;")
db.commit()

terminal.executemany(sql, data_to_dump)
db.commit()

stock_symbol = (input("Enter the stock symbol: ")).upper()
terminal.execute("SELECT * FROM stocks1 WHERE sym = %s;", (stock_symbol,))
result = terminal.fetchone()
if result:
    print(f"Data for {stock_symbol}: {result}")
else:
    f"no data found for {stock_symbol}"

db.close()
