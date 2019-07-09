from bs4 import BeautifulSoup
import requests
import json

#import mechanize
import re
import mechanize

#enter array of VIM numbers to scrape
vim_num = [
    "jfsjklfdjsklafj",
    "jfklsjkfldsjklfj",
    "hslkdksajdklssjak"
]

#page url
url = 'http://ethans_fake_twitter_site.surge.sh/'

#handle the form
browser.open('http://example.com/form/')
browser.select_form(name='the_form')
browser['field1'] = 'value'
browser['field2'] = 'value'
browser['field3'] = 'value'
browser.submit()

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