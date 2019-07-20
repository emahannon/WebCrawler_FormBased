#Author: Emily Hannon
#Date: 11 July 2019
#Purpose: Takes -s VIM_NUMBER as a command line argument to scrape contents of driving-tests.org into a JSON file.

#Requirements: Selenium must be added to PATH.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import json

headers = {
    "User-Agent":"just a user"
}

parser = argparse.ArgumentParser(description='Returns a json file of scraped website.')
parser.add_argument("-s", "--string", metavar='N', type=str,help='a VIN number')
 
args = parser.parse_args()
#print(str(args.string)) #check that parser works

#set parsed input to variable
vin_num = str(args.string)


browser = webdriver.Chrome()
browser.get('https://www.iseecars.com/vin')
#find form
elem = browser.find_element_by_id("vin-field") #VIN by name #vin-field by id
elem.clear() #clear form
#fill in form
elem.send_keys(vin_num)
elem.send_keys(Keys.RETURN)
#vin num XPath: //*[@id="vin_val"]
#vin_num_element = browser.find_element_by_class_name('id135_vntbl_col ').get_attribute('textContent')
key_specs = browser.find_element_by_xpath('//*[@id="vin-basicspecs-panel"]/div[1]').get_attribute('textContent')
#vin_num = vin_num_element.text

safety_ratings = browser.find_element_by_class_name('stars-sprite-bottom-img').get_attribute('style') #get the style width


features = browser.find_element_by_xpath('//*[@id="vin-features-panel"]/div[2]/div/div[2]/div').get_attribute('textContent') #//*[@id="vin-features-panel"]/div[2]/div/div[2]/div
market_pricing = browser.find_element_by_xpath('//*[@id="vin-price-panel"]/table').get_attribute('textContent') #//*[@id="vin-price-panel"]/table
mileage_analysis = browser.find_element_by_xpath('//*[@id="vin-condition-panel"]').get_attribute('textContent') #//*[@id="vin-condition-panel"]
# get href link VVV
recall_check = browser.find_element_by_xpath('//*[@id="vin-carfax-panel"]').get_attribute('href') #//*[@id="vin-carfax-panel"] #get the href link
days_listed = browser.find_element_by_xpath('//*[@id="vin-dom-panel"]/table').get_attribute('textContent') #//*[@id="vin-dom-panel"]/table
listing_history = browser.find_element_by_xpath('//*[@id="vin-history-panel"]').get_attribute('textContent') #//*[@id="vin-history-panel"]
projected_depreciation = browser.find_element_by_xpath('//*[@id="vin-deprication-panel"]').get_attribute('textContent') #//*[@id="vin-deprication-panel"]
car_comparison = browser.find_element_by_xpath('//*[@id="vin-similar-panel"]').get_attribute('textContent') #//*[@id="vin-similar-panel"]
time_to_buy = browser.find_element_by_xpath('//*[@id="vin-besttimetobuy-panel"]').get_attribute('textContent') #//*[@id="vin-besttimetobuy-panel"]
selling_vehicle = browser.find_element_by_xpath('/html/body/div[2]/div[17]').get_attribute('textContent') #/html/body/div[2]/div[17]
# get href link VVVVV
#owner_manual = browser.find_element_by_id('vin-manuals-panel').get_attribute('textContent') #//*[@id="vin-manuals-panel"]/div[1]/a #get the href link

owner_manual = " "

print(key_specs)
print()

#put all the data into a json file

contentObject = {
        "Key Specs": key_specs,
        "Safety Ratings": safety_ratings,
        "Features": features,
        "Market Value & Pricing Info": market_pricing,
        "Mileage Analysis": mileage_analysis,
        "Free Recall Check": recall_check,
        "Days Listed For Sale": days_listed,
        "Listing History": listing_history,
        "Projected Depreciation": projected_depreciation,
        "Similar Car Comparison": car_comparison,
        "Best Times To Buy": time_to_buy,
        "Selling This Vehicle": selling_vehicle,
        "Owner's Manual": owner_manual
    }
print (contentObject)


#print(tweetArr)

with open('vinData.json', 'w') as outfile:
    json.dump(contentObject, outfile)


#browser.close()

#remove leading spaces
#remove categories and only leave behind data
#then reorganize




