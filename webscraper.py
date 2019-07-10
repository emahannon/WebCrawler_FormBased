from bs4 import BeautifulSoup
import requests
import json
import mechanicalsoup
import argparse

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"

}

parser = argparse.ArgumentParser(description='Returns a json file of scraped website.')
parser.add_argument("-s", "--string", metavar='N', type=str,help='a VIN number')
 
args = parser.parse_args()
#print(str(args.string)) #check that parser works

#set parsed input to variable
vin_num = str(args.string)

#create a browser object
browser = mechanicalsoup.StatefulBrowser()

#page url
url = 'https://driving-tests.org/vin-decoder/'

#handle the form
browser.open(url)
browser.select_form() #CSS selector or a bs4.element.Tag object to identify the form to select. If not specified, selector defaults to “form”, which is useful if, e.g., 
browser["VIN"] = vin_num
#browser["vin"] = vin_num
resp = browser.submit_selected()

#GET raw HTML from the site

response = requests.get(url, timeout=5, headers=headers)
#content = BeautifulSoup(response.content, "html.parser")
content = browser.get_current_page()


#isolate the content
tweet = content.find_all('h1')


print(str(tweet)+ " YEET")

contentArr = []

#isolate the content for a specific tag and class
#then find a specific tag and class for all instances of the content in the doc
for things in content.find_all('section', class_="vin-report"):
    contentObject = {
        "year": things.find('span', class_="report-value", id="nhtsa-29").text,
        "brand": things.find('span', class_="report-value", id="nhtsa-26").text,
        "model": things.find('span', class_="report-value", id="nhtsa-28").text,
        "VIN": things.find('span', id="vin_val").text,
        
        
    }
    print (contentObject)
    contentArr.append(contentObject)

#print(tweetArr)

with open('vinData.json', 'w') as outfile:
    json.dump(contentArr, outfile)