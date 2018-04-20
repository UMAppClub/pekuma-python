#------------------------------------------------------------------------------------
# This is a web scraper which does data collection, data cleansing and data saving
# Written by Leon Wee, April 2018.
# Anyone may freely copy or modify this program.
#------------------------------------------------------------------------------------

import requests, bs4, csv, re # remember to do pip install beautifulsoup4, and pip install requests

res = requests.get('https://cryptoreport.com')

res.raise_for_status()

cryptoReport = bs4.BeautifulSoup(res.text, "html.parser")


elems = cryptoReport.select('td')

i = 0 # define the boundary
coins = [] 
coin = []

for elem in elems:
	if i == 1: # when i == 1, don't add the value into coin because if was a picture
		i += 1
		continue

	if i != 7:
		coin.append(re.sub('[$,%]','',elem.get_text())) # add the data into coin and do some cleaning by substituting $,% symbols by '' (an empty string)
		i += 1
		continue

	if i == 7:
		coin.append(re.sub('[$,]','',elem.get_text()))
		coins.append(coin)
		i = 0 # reset the boundary
		coin = [] # reset the coin
		continue

outputFile = open('cryptoreport.csv', 'w', newline='') # create a csv file named cryptoreport.csv, 'w' stands for write since we are gonna write some data into the file

outputWriter = csv.writer(outputFile)

outputWriter.writerow(["No.", "Name", "Symbol", "Price ($)", "Change (%)", "Market Cap ($)", "24 Hour Volume ($)"]) # write a row of header to indicate what does each collumn represents

for coin in coins: # loop through all coin in coins and write them into the csv file
	outputWriter.writerow(coin) 