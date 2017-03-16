import sys, os
import time
import datetime
import bs4
import requests

with requests.session() as c:
	print("Searching in zip code: 98006 \n")
	neon = "Neon - No Stock"
	gray = "Gray - No Stock"
	url = "https://primenow.amazon.com/"

	c.get(url)
	login_data = dict(newPostalCode = "98006");
	c.post(url, data=login_data, headers = {'User-agent': 'Mozilla/5.0'})
	while(True):
		os.system('clear')
		page = c.get("https://primenow.amazon.com/search?k=nintendo+switch&p_95=&merchantId=&ref_=pn_gw_nav_ALL", headers = {'User-agent': 'Mozilla/5.0'})
		soup = bs4.BeautifulSoup(page.text, 'lxml')
		filtered = soup.findAll("p", {"class": "asin__details__title"})
		for item in filtered:
			if(item.text.strip() == "Nintendo Switch with Neon Blue and Neon Red Joy-Con"):
				neon = "##### Neon - IN STOCK! #####"
				for x in range(0, 10):
					os.system('tput bel');
				break
			neon = "Neon - No Stock"
		for item in filtered:
			if (item.text.strip() == "Nintendo Switch with Gray Joy-Con"):
				gray = "##### Gray - IN STOCK! #####"
				for x in range(0, 10):
					os.system('tput bel');
				break
			gray = "Gray - No Stock"
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		print(st + "\n" + neon + "\n" + gray + "\n")
		time.sleep(int(30))
