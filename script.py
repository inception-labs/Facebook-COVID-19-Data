import requests
import json
import pandas as pd
fileNames = ["SUD_vaccine_acpt.csv"]
urls = ["https://covidmap.umd.edu/api/resources?indicator=vaccine_acpt&type=daily&country=Sudan&daterange=20200301-20210609"]
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
    
    

    
    
