
"""import requests

url = "https://chukul.com/api/data/v2/daily-stock/"
response = requests.get(url = url)
data = response.json()
"""



import requests
import csv

url = "https://chukul.com/api/data/v2/daily-stock/"
response = requests.get(url)
#data = response.json()


# Column headers
fields = ['Symbol', 'LTP', 'Percentage Change', 'Volume']

# Data rows
rows = response.json()

# Writing to a CSV file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)     # Write header
    writer.writerows(rows)      # Write data rows    

