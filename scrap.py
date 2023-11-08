from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

start_url ="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"


service =Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get(start_url)
time.sleep(10)

planet_data = []

def scrape():
    for i in range(0,10):
        print(f'Scrapping page {i+1}...')

        soup = BeautifulSoup(driver.page_source, "html.parser")
        #print(soup)

        for ul_tag in soup.find_all('ul', attrs  = {"class", "exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try: 
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            driver.find_element(by=By.XPATH, value= '//*[@id="primary_column"]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()




scrape()

headers = ['name','light_years', 'planet_mass', 'ST', 'dS']

dataFile = pd.DataFrame(planet_data, columns = headers)
dataFile.to_csv("finalData.csv", index = True, index_label = 'id')


