import os
import time
import pyautogui
url=input("Video URL without episode: ")
start = int(input("First Episode to Download: "))
end = int(input("Last Episode to Download: "))+1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  # interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
chromedriver = r"E:\Compressed\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
service = ChromeService(executable_path=ChromeDriverManager().install())
chrome_options = Options()
# this is the preference we're passing
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, desired_capabilities=caps, options=chrome_options)
for i in range(start, end):
    driver.get(url + str(i))
    driver.execute_script("window.scrollTo(0, 100)")
    # a = pyautogui.locateOnScreen('img.png', grayscale=True)
    driver.find_element('xpath',"/html/body/div[2]/div/div/section/section[1]/div[1]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
    time.sleep(5)
    pyautogui.click('img_480.png')
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])