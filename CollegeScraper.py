import requests
from bs4 import BeautifulSoup

from random import randint
from time import sleep










url = "http://www.engineering.careers360.com/colleges/list-of-engineering-colleges-in-India?page="
collegeRank = 11;
pageNumb = 0

for num in range(1, 556):
	pageNumb = pageNumb+1
	url = url + str(num)
	print(url + "    " +str(pageNumb))
	responseHTML = requests.get(url)


	htmlContent = str(responseHTML.content, "utf-8")
	f = open('./pages/'+str(num)+'.html', 'w')
	f.write(htmlContent)
	f.close()


	soup = BeautifulSoup(responseHTML.content)
	links = soup.find_all("div", {"class": "title"})
	for link in links:
		sleep(randint(7,17))
		clgURL= link.findChildren()[0].get("href")


		clgResponseHTML = requests.get(clgURL)
		htmlContent = str(clgResponseHTML.content, "utf-8")

		clgName = str(collegeRank) + " " + clgURL[47:].replace("-", " ")
		clgF = open(clgName+'.html', 'w')
		clgF.write(htmlContent)
		clgF.close()
		collegeRank = collegeRank + 1







