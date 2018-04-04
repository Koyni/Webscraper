from bs4 import
import urllib.request

def scrapeprince():
	url = 'https://coinmarketcap.com/currencies/bitcoin/'
	page = urllib,request.urlopen(url)
	soup = BeautifulSoup(page, "html.parser")
	name_box = strftime("as of" + "%m/%d/%Y %H:%M", gmtime()) + ", the current price of Bitcoin is" + "$" + soup.find(attrs={"class": "text-large2"}
		text = name_box.encode()
		f = open ('bitcoinprice.txt', 'wb')
		f.close()

