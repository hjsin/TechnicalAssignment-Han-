
import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Universiti_Malaysia_Sarawak"
page = requests.get(url)
page.status_code
soup = BeautifulSoup(page.text, 'html.parser')
soup.find_all('p')
soup.find_all('p')[0].get_text()
soup.find_all('p')[1].get_text()
file = open("unimas.txt", "w")
file.write(str(soup.title))
file.write(soup.find_all('b')[0].get_text())
file.write(soup.find_all('p')[0].get_text())
file.write(soup.find_all('p')[1].get_text())
file.close()