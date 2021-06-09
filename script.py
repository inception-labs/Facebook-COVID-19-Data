import requests
import json
import pandas as pd
fileNames = ["newFile2.csv"]
urls = ["https://covidmap.umd.edu/api/resources?indicator=mask&type=daily&country=Tunisia&daterange=20201201-20201204"]
if(len(fileNames) != len(urls)):
    print("Need the same number of files and urls")
    exit()
for fileName, url in zip(fileNames,urls):
    response = requests.get(url)
    obj = json.loads(response.text)
    df = pd.read_json(json.dumps(obj['data']))
    csv_str = df.to_csv()
    f = open(fileName, "w", newline="")
    f.write(csv_str)
    f.close()

    
    
