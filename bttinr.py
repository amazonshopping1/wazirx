import json
import requests
import csv
import time
while True:
    url = "https://api.wazirx.com/api/v2/tickers/bttinr"
    JSONContent = requests.get(url).json()
    content = json.dumps(JSONContent, indent = 4, sort_keys=True)

    filename = "new.csv"
    with open(filename,'a') as csvfile:
        csvwriter = csv.DictWriter(csvfile,fieldnames=['at','ticker'])
        content = json.dumps(JSONContent, indent = 4, sort_keys=True)
        csvwriter.writerow(JSONContent)
        time.sleep(1)
