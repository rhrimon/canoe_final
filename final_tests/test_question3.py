import time
import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from bs4 import SoupStrainer as strainer
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestGiphy:
    url = 'https://giphy.com/'    

    def chrome_options(self):
        #set chrome headless options
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("window-size=1400,2100") 
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')  

        return chrome_options


    def test_giphy(self): 
        #use selenium to navigate to giphy
        driver = webdriver.Chrome(options=self.chrome_options())
        driver.get(self.url)
        time.sleep(1)

        #search for fintech gifs and click search
        driver.find_element_by_xpath('//*[@id="searchbar"]/div/div/form/input').send_keys('fintech')
        driver.find_element_by_xpath('//*[@id="searchbar"]/div/a/div/div[2]').click()
        time.sleep(1)

        #use bs4 to retrieve script where tags are stored from results page
        response = requests.get(driver.current_url)
        soup = bs(response.content, "html.parser")
        page_script = soup.find_all('script')[12].string.strip()
        
        #further parse through script
        index1 = page_script.index('[')
        index2 = page_script.index('}]')
        gif_list = page_script[index1:index2 + 2]

        #load json item as string 
        gifs_json = json.loads(gif_list)

        # loop through tags until cute tag is found
        is_cute = False
        for gif in gifs_json:
            for tag in gif['tags']:
                print(tag)
                if tag == 'cute':
                    is_cute = True
        
        assert is_cute == True