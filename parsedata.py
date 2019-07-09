import json
import pandas as pd

with open('twitterData.json') as json_data:
    jsonData = json.load(json_data)

df = pd.DataFrame(jsonData)

print(df.head(10))


#for i in jsonData:
    #print (i['date'])