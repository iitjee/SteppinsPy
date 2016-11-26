/*
https://docs.python.org/2/library/webbrowser.html









*/


import requests


url = "http://www.engineering.careers360.com/colleges/list-of-engineering-colleges-in-India?page="
r = requests.get(url)  #you get as response object;  see type(r)
htmlContent = str(r.content, "utf-8")  #r.convert is in bytes; should convert to string for file handling


	f = open('myDownloadedPage.html', 'w')  #Open file for writing
	f.write(htmlContent)  #Write Data
	f.close()
