from bs4 import BeautifulSoup
import requests
import json
import mechanicalsoup
import argparse

parser = argparse.ArgumentParser(description="Login to GitHub.")
parser.add_argument("username")
args = parser.parse_args()

args.password = getpass("Please enter your GitHub password: ")

#create a browser object
browser = mechanicalsoup.StatefulBrowser()

#page url
url = 'http://ethans_fake_twitter_site.surge.sh/'

#handle the form
browser.open(url)
browser.select_form(selector="PLACEHOLDER_CSS_SELECTOR") #CSS selector or a bs4.element.Tag object to identify the form to select. If not specified, selector defaults to “form”, which is useful if, e.g., 
browser["FORM ENTRY TITLE"] = args.username
resp = browser.submit_selected()

#GET raw HTML from the site

response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")

#isolate the content
#tweet = content.find('div', class_="tweetcontainer")

tweetArr = []

#isolate the content for a specific tag and class
#then find a specific tag and class for all instances of the content in the doc
for tweet in content.find_all('div', class_="tweetcontainer"):
    tweetObject = {
        "author": tweet.find('h2', class_="author").text,
        "date": tweet.find('h5', class_="dateTime").text,
        "tweet": tweet.find('p', class_="content").text,
        "likes": tweet.find('p', class_="likes").text,
        "shares": tweet.find('p', class_="shares").text
    }
    #print (tweetObject)
    tweetArr.append(tweetObject)

#print(tweetArr)

with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)