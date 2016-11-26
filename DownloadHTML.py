/*
https://docs.python.org/2/library/webbrowser.html









*/


import requests


url = "http://www.engineering.careers360.com/colleges/list-of-engineering-colleges-in-India?page="
webContent = requests.get(url)  #you get in bytes
htmlContent = str(webContent.content, "utf-8")  #should convert to string for file ha


	f = open('myDownloadedPage.html', 'w')  #Open file for writing
	f.write(htmlContent)  #Write Data
	f.close()
