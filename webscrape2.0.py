#Author: Emily Hannon
#Date: 11 July 2019
#Purpose: Takes -s VIM_NUMBER as a command line argument to scrape contents of driving-tests.org into a JSON file.

#Requirements: Selenium must be added to PATH.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import json

headers = {
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"
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
elem = browser.find_element_by_id("vin-field") #VIN by name
elem.clear() #clear form
#fill in form
elem.send_keys(vin_num)
elem.send_keys(Keys.RETURN)
#vin num XPath: //*[@id="vin_val"]
vin_num_element = browser.find_element_by_xpath('//*[@id="vin-basicspecs-panel"]/div[1]/div[1]').get_attribute('textContent')
#vin_num = vin_num_element.text


print(vin_num_element)
print()


#browser.close()

#remove leading spaces
#remove categories and only leave behind data
#then reorganize

