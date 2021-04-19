import re
import time
import requests
import unidecode
import chromedriver_binary
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestLorem():
    url = 'https://markjs.io/configurator.html'

    def chrome_options(self):
        #set chrome headless options
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("window-size=1400,2100") 
        chrome_options.add_argument('--disable-gpu')

        return chrome_options

    def test_lorem(self):
        #use bs4 to retrieve and store example text paragraph
        response = requests.get(self.url)
        soup = bs(response.content, "html.parser")
        example_text = soup.find_all('div', {'class': 'panel-body'})[1].getText()

        #use unidecode to remove diacritics from example text
        normalized_text = unidecode.unidecode(example_text)

        #use regex to find all case insensitive examples of lorem
        case_insensitive_lorems = re.findall(r'(?i)lorem', normalized_text)

        #use regex to find all case sensitive examples of lorem
        case_sensitive_lorems = re.findall(r'lorem', normalized_text)
        print(case_sensitive_lorems)

        #use selenium to open configurator and enter 'lorem' as keyword to search
        driver = webdriver.Chrome(options=self.chrome_options())
        driver.get(self.url)
        time.sleep(1)
        #clear 'keyword' field of prefilled text
        driver.find_element_by_id('keyword').clear()
        driver.find_element_by_id('keyword').send_keys('lorem')
        time.sleep(1)

        #select 'exactly' as accuracy to ensure accurate results
        select_accuracy = Select(driver.find_element_by_id('form-keyword-accuracy'))
        select_accuracy.select_by_value('exactly')

        #select 'ignore joiners' to ensure all lorems are found
        driver.find_element_by_id('form-keyword-ignoreJoiners').click()

        #make sure 'Case Sensitive' field is not selected
        if driver.find_element_by_id('form-keyword-caseSensitive').is_selected() == True:
            driver.find_element_by_id('form-keyword-caseSensitive').click()
        
        #click Mark button
        driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[1]/div/div[2]/form[1]/button').click()
        time.sleep(1)

        #assert correct number of matches for case insensitive results
        assert len(driver.find_elements_by_css_selector('.configurator .context :not(p):not(.ignore)')) == len(case_insensitive_lorems)

        #check case sensitive box and click 'Mark' button to search for case sensitive results
        driver.find_element_by_id('form-keyword-caseSensitive').click()
        driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[1]/div/div[2]/form[1]/button').click()
        time.sleep(1)

        #assert correct number of matches for case sensitive results
        assert len(driver.find_elements_by_css_selector('.configurator .context :not(p):not(.ignore)')) == len(case_sensitive_lorems)        

        driver.close()