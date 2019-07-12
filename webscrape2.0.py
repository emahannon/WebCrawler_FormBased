#Author: Emily Hannon
#Date: 11 July 2019
#Purpose: Takes -s VIM_NUMBER as a command line argument to scrape contents of driving-tests.org into a JSON file.

#Requirements: Selenium must be added to PATH.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import json

headers = {
    "User-Agent":"new user"
}

parser = argparse.ArgumentParser(description='Returns a json file of scraped website.')
parser.add_argument("-s", "--string", metavar='N', type=str,help='a VIN number')
 
args = parser.parse_args()
#print(str(args.string)) #check that parser works

#set parsed input to variable
vin_num = str(args.string)


browser = webdriver.Chrome()
browser.get('https://driving-tests.org/vin-decoder/')
#find form
elem = browser.find_element_by_name("VIN") #VIN by name #vin-field by id
elem.clear() #clear form
#fill in form
elem.send_keys(vin_num)
elem.send_keys(Keys.RETURN)
#vin num XPath: //*[@id="vin_val"]
#vin_num_element = browser.find_element_by_class_name('id135_vntbl_col ').get_attribute('textContent')
vin_num_element = browser.find_element_by_class_name('panel panel-info').get_attribute('textContent')
#vin_num = vin_num_element.text


print(vin_num_element)
print()


#browser.close()

#remove leading spaces
#remove categories and only leave behind data
#then reorganize

