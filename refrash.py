import requests
from bs4 import BeautifulSoup

def ref_curs():
	session = requests.Session()
	response = session.get('http://google.com')

	c = session.cookies.get_dict()

	coc = ""

	for i in c:
		coc += f"{i}={c[i]}; " 

	headers = {	"accept" : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				"accept-encoding" : 'gzip, deflate, br',
				"accept-language" : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
				"cache-control" : 'max-age=0',
				"cookie" : coc,
				"sec-ch-ua" : '"Chromium";v="90", "Opera GX";v="76", ";Not A Brand";v="99"',
				"sec-ch-ua-mobile" : '?0',
				"sec-fetch-dest" : 'document',
				"sec-fetch-mode" : 'navigate',
				"sec-fetch-site" : 'same-origin',
				"sec-fetch-user" : '?1',
				"upgrade-insecure-requests" : '1',
				"user-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 GROW-2135 Safari/537.36 OPR/76.0.4017.222}'}

	USD = "https://www.google.com/search?client=opera-gx&q=курс+доллара+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8"
	UAH = "https://www.google.com/search?client=opera-gx&q=курс+гривны+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8"
	KZT = "https://www.google.com/search?client=opera-gx&q=курс+KZT+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8"
	BYN = "https://www.google.com/search?client=opera-gx&q=курс+BYN+к+рублю&sourceid=opera&ie=UTF-8&oe=UTF-8"



	USD = float(BeautifulSoup(session.get(USD,headers=headers).text, 'html.parser').find("span","DFlfde SwHCTb").string.replace(",","."))
	KZT = float(BeautifulSoup(session.get(KZT,headers=headers).text, 'html.parser').find("span","DFlfde SwHCTb").string.replace(",","."))
	BYN = float(BeautifulSoup(session.get(BYN,headers=headers).text, 'html.parser').find("span","DFlfde SwHCTb").string.replace(",","."))
	UAH = float(BeautifulSoup(session.get(UAH,headers=headers).text, 'html.parser').find("span","DFlfde SwHCTb").string.replace(",","."))
	
	return dict(USD=float(USD),UAH=float(UAH),KZT=float(KZT),BYN=float(BYN))
