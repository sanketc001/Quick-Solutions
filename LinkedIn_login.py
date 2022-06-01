import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  # interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
chromedriver = r"C:\Users\USER\Downloads\Compressed\chromedriver.exe"

os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()

# this is the preference we're passing
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
driver.get('https://www.linkedin.com')
time.sleep(2)
driver.maximize_window()

#********** LOG IN *************

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")
username.send_keys('email')
password.send_keys('password')
time.sleep(5)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()

for j in range(24,51):
    # driver.get('https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page='+str(j))
    driver.get('https://www.linkedin.com/search/results/people/?geoUrn=%5B%22105080838%22%5D&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=' + str(j))
    time.sleep(2)
    allButtons=driver.find_elements_by_tag_name('button')
    connectButtons=[i for i in allButtons if i.text=='Connect']
    for i in connectButtons:
        driver.execute_script("arguments[0].click();",i)
        time.sleep(2)
        send=driver.find_element_by_xpath("//button[@aria-label='Send now']")
        driver.execute_script("arguments[0].click();", send)
        closeButton=driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
        driver.execute_script("arguments[0].click();", closeButton)
        time.sleep(2)