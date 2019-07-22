# WebCrawler_FormBased
Form-based web scraping for taking VIM numbers from a site.

Takes a VIM number in the form of a command line argument to output a JSON file.


Requires Selenium to be added to PATH and Chrome to be downloaded. (WITHOUT THIS THE SCRIPT WILL NOT RUN)

Packages used: selenium, argparse, json
All packages must be installed to run.


To run the script, run a command similar to the one listed below:
python /Users/emilyhannon/Documents/GitHub/WebCrawler_FormBased/webscrape2.0.py -s 3FAHP0JG5CR225972

Setting up a cron job in linux:

1. As the shell user in the command line run: crontab -e
2. Paste the below cron command into the bottom of the file that has just opened: (Note: This command should change based on your file system/where python is located on your machine. The only part of the command that should not be changed is the first part with the stars.)

0 0 * * *	python	/Users/emilyhannon/Documents/GitHub/WebCrawler_FormBased/webscrape2.0.py -s 3FAHP0JG5CR225972


This cron job will run once a day at midnight.
