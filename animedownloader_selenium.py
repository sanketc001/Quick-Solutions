import os
import time
import pyautogui
url="https://gogoanime.lu/tensei-kenja-no-isekai-life-dai-2-no-shokugyou-wo-ete-sekai-saikyou-ni-narimashita-episode-"#input("Video URL without episode: ")
start =1 #int(input("First Episode to Download: "))
end =2 #int(input("Last Episode to Download: "))+1
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
userAgent = UserAgent().random
print(userAgent)
caps = DesiredCapabilities().CHROME
# caps["pageLoadStrategy"] = "normal"  #  complete
caps["pageLoadStrategy"] = "eager"  # interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
chromedriver = r"E:\Compressed\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
service = ChromeService(executable_path=ChromeDriverManager().install())
options = Options()
# this is the preference we're passing
options.add_argument(f'user-agent={userAgent}')
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
options.add_experimental_option("prefs", prefs)
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=service, desired_capabilities=caps, options=options)
for i in range(start, end):
    driver.get(url + str(i))
    driver.execute_script("window.scrollTo(0, 100)")
    # a = pyautogui.locateOnScreen('img.png', grayscale=True)
    driver.find_element('xpath',"/html/body/div[2]/div/div/section/section[1]/div[1]/div[2]/div[1]/div[5]/ul/li[1]/a").click()
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
    pyautogui.click('img_480.png')
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])