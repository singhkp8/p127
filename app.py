from selenium import webdriver
import time
import csv
from bs4 import BeautifulSoup

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:/Users/singhk3/Desktop/Kavya/game folder/Python class/c127/pro/chromedriver.exe")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["V mag","proper name","Bayer designation","Distance","spectral class","Mass","Radius","Luminosity"]
    star_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs = {"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index , li_tag in enumerate(li_tag):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")

            planet_data.append(temp_list)
        browser.find_element_by_xpath('[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrape.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(star_data)


scrape()
