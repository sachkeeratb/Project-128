from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

headers = ["Name","Distance","Mass","Radius"]
star_data = []

start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("./msedgedriver.exe")
browser.get(start_url)
time.sleep(10)

def scrape():
    page = requests.get(start_url)
    soup = BeautifulSoup(browser.page_source,"html.parser")
    star_table = soup.find_all('table')
    table_rows = star_table[7].find_all('tr')

    for td_tag in soup.find_all("td",attrs={"class","exoplanet"}):
        tr_tag = td_tag.find_all("tr")
        temp_list = []
        for index,tr_tag in enumerate(tr_tag):
            if index == 0 :
                temp_list.append(tr_tag.findall("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                    temp_list.append("")
        star_data.append(temp_list)

scrape()

final_star_data = []

for index, data in enumerate(star_data):
    new_star_data_element = [elem.replace("\n", "") for elem in new_star_data_element]
    new_star_data_element = new_star_data_element[:7]
    final_star_data.append(data + new_star_data_element)

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_star_data)

with open("final.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(final_star_data)