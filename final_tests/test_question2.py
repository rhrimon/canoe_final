import time
import string
import random
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

class TestForm:
    #form url
    url = 'https://teroauralinna.github.io/vue-demo-form/'
    #generate first name
    first_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(random.randint(5,20)))
    #generate last name
    last_name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(random.randint(5,20)))
    #generate email
    email = (''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(random.randint(5,15)))) + random.choice(['@gmail.com', '@yahoo.com', '@outlook.com'])
    #generate additional info
    additional_info = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(random.randint(50,1000)))
    #success message to look for after form is submitted
    success_message = "The form is submitted!"

    def chrome_options(self):
        #set chrome headless options
        chrome_options=webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("window-size=1400,2100") 
        chrome_options.add_argument('--disable-gpu')

        return chrome_options

    #POSITIVE 
    #everything filled out properly and submitted
    def test_form_positive(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter first name
        driver.find_element_by_id('firstName').send_keys(self.first_name)
        #enter last name
        driver.find_element_by_id('lastName').send_keys(self.last_name)
        #enter email
        driver.find_element_by_id('email').send_keys(self.email)
        #select subscription type
        select = Select(driver.find_element_by_id('type'))
        select.select_by_value(random.choice(['free', 'starter', 'enterprise']))
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #agree to terms and conditions
        driver.find_element_by_id('terms').click()
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        time.sleep(1)

        assert self.success_message in driver.page_source


    #NEGATIVE
    # - blank form
    def test_form_blank(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        
        assert self.success_message not in driver.page_source

    # - blank first name
    def test_form_blank_first_name(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter last name
        driver.find_element_by_id('lastName').send_keys(self.last_name)
        #enter email
        driver.find_element_by_id('email').send_keys(self.email)
        #select subscription type
        select = Select(driver.find_element_by_id('type'))
        select.select_by_value(random.choice(['free', 'starter', 'enterprise']))
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #agree to terms and conditions
        driver.find_element_by_id('terms').click()
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        time.sleep(1)
        
        assert self.success_message not in driver.page_source

    # - blank last name
    def test_form_blank_last_name(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter first name
        driver.find_element_by_id('firstName').send_keys(self.first_name)
        #enter email
        driver.find_element_by_id('email').send_keys(self.email)
        #select subscription type
        select = Select(driver.find_element_by_id('type'))
        select.select_by_value(random.choice(['free', 'starter', 'enterprise']))
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #agree to terms and conditions
        driver.find_element_by_id('terms').click()
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        time.sleep(1)
        
        assert self.success_message not in driver.page_source

    # - blank email
    def test_form_blank_email(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter first name
        driver.find_element_by_id('firstName').send_keys(self.first_name)
        #enter last name
        driver.find_element_by_id('lastName').send_keys(self.last_name)
        #select subscription type
        select = Select(driver.find_element_by_id('type'))
        select.select_by_value(random.choice(['free', 'starter', 'enterprise']))
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #agree to terms and conditions
        driver.find_element_by_id('terms').click()
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        time.sleep(1)

        assert self.success_message not in driver.page_source

    # - invalid email
    def test_form_invalid_email(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter first name
        driver.find_element_by_id('firstName').send_keys(self.first_name)
        #enter last name
        driver.find_element_by_id('lastName').send_keys(self.last_name)
        #enter email
        driver.find_element_by_id('email').send_keys(self.first_name)
        #select subscription type
        select = Select(driver.find_element_by_id('type'))
        select.select_by_value(random.choice(['free', 'starter', 'enterprise']))
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #agree to terms and conditions
        driver.find_element_by_id('terms').click()
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[8]/button').click()
        time.sleep(1)

        assert self.success_message not in driver.page_source

    # - subscription type blank
    def test_form_sub_type_blank(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter first name
        driver.find_element_by_id('firstName').send_keys(self.first_name)
        #enter last name
        driver.find_element_by_id('lastName').send_keys(self.last_name)
        #enter email
        driver.find_element_by_id('email').send_keys(self.email)
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #agree to terms and conditions
        driver.find_element_by_id('terms').click()
        time.sleep(1)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        time.sleep(1)

        assert self.success_message not in driver.page_source

    # - terms not accepted
    def test_form_sub_terms_not_accepted(self):
        #use selenium to open form and enter all fields with valid data
        driver = webdriver.Chrome(options=self.chrome_options())
        #navigate to url
        driver.get(self.url)
        time.sleep(1)
        #enter first name
        driver.find_element_by_id('firstName').send_keys(self.first_name)
        #enter last name
        driver.find_element_by_id('lastName').send_keys(self.last_name)
        #enter email
        driver.find_element_by_id('email').send_keys(self.email)
        #select subscription type
        select = Select(driver.find_element_by_id('type'))
        select.select_by_value(random.choice(['free', 'starter', 'enterprise']))
        #enter additional info
        driver.find_element_by_id('additionalInfo').send_keys(self.additional_info)
        #click submit button
        driver.find_element_by_xpath('//*[@id="app"]/div/div/div/form/div[7]/button').click()
        time.sleep(1)

        assert self.success_message not in driver.page_source
