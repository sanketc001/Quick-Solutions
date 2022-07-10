import csv
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
with open("startups.csv","r") as file:
    rows=csv.reader(file)
    l=[]
    for row in rows:
        l.append(row)
for i in l[1:]:
    if(i[4]!="NA"):
        try:
            if(i[4].startswith("http")==False):
                driver.get("https://"+i[4])
            else:
                driver.get(i[4])
            driver.switch_to.new_window()
        except:
            print(i[4],l.index(i))