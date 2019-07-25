#Author: Emily Hannon
#Date: 11 July 2019
#Purpose: Takes -s VIM_NUMBER as a command line argument to scrape contents of driving-tests.org into a JSON file.

#Requirements: Selenium must be added to PATH.

from __future__ import print_function

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import json
from selenium.webdriver.chrome.options import Options
import string
import zipfile

PROXY_HOST = "23.94.44.65"
PROXY_PORT = "10998"
USERNAME = "netkingz9" 
PASSWORD = "test123"

def create_proxyauth_extension(proxy_host, proxy_port,
                               proxy_username, proxy_password,
                               scheme='http', plugin_path=None):
    """Proxy Auth Extension

    args:
        proxy_host (str): domain or ip address, ie proxy.domain.com
        proxy_port (int): port
        proxy_username (str): auth username
        proxy_password (str): auth password
    kwargs:
        scheme (str): proxy scheme, default http
        plugin_path (str): absolute path of the extension       

    return str -> plugin_path
    """
    

    if plugin_path is None:
        plugin_path = '/tmp/vimm_chrome_proxyauth_plugin.zip'

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = string.Template(
    """
    var config = {
            mode: "fixed_servers",
            rules: {
              singleProxy: {
                scheme: "${scheme}",
                host: "${host}",
                port: parseInt(${port})
              },
              bypassList: ["foobar.com"]
            }
          };

    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

    function callbackFn(details) {
        return {
            authCredentials: {
                username: "${username}",
                password: "${password}"
            }
        };
    }

    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path

proxyauth_plugin_path = create_proxyauth_extension(
    proxy_host="23.94.44.65",
    proxy_port=10998,
    proxy_username="netkingz9",
    proxy_password="test123"
)


co = Options()
co.add_argument("--start-maximized")
co.add_extension(proxyauth_plugin_path)







#ACTUAL SCRAPING
headers = {
    "User-Agent":"this is a user"
}

parser = argparse.ArgumentParser(description='Returns a json file of scraped website.')
parser.add_argument("-s", "--string", metavar='N', type=str,help='a VIN number')
 
args = parser.parse_args()
#print(str(args.string)) #check that parser works

#set parsed input to variable
vin_num = str(args.string)


browser = webdriver.Chrome(options=co)
browser.get('https://www.iseecars.com/vin')
#find form
elem = browser.find_element_by_id("vin-field") #VIN by name #vin-field by id
elem.clear() #clear form
#fill in form
elem.send_keys(vin_num)
elem.send_keys(Keys.RETURN)
#vin num XPath: //*[@id="vin_val"]
#vin_num_element = browser.find_element_by_class_name('id135_vntbl_col ').get_attribute('textContent')
key_specs = " " #browser.find_element_by_xpath('//*[@id="vin-basicspecs-panel"]').get_attribute('textContent')
#vin_num = vin_num_element.text

safety_ratings = " " #browser.find_element_by_class_name('//*[@id="vin-safety-panel"]/div').get_attribute('style') #get the style width


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
owner_manual = " " #browser.find_element_by_id('//*[@id="vin-manuals-panel"]') #//*[@id="vin-manuals-panel"]/div[1]/a #get the href link


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




