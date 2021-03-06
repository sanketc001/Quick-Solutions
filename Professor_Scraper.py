import csv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete
# caps["pageLoadStrategy"] = "eager"  # interactive
# caps["pageLoadStrategy"] = "none"   #  undefined
chromedriver = r"C:\Users\USER\Downloads\Compressed\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
chrome_options = Options()
# this is the preference we're passing
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(desired_capabilities=caps, chrome_options=chrome_options)
#Professors name, designation, department, email, number, research interests, current research profile, google scholar link, LinkedIn
driver.get("https://iitgn.ac.in/faculty")
driver.execute_script("window.scrollTo(0, 700)")
x=WebDriverWait(driver,60).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/section[2]/div/div/div/div/div[2]/div[197]/div/div[2]/h4/a")))
m=[]
for i in range(1,198):
    d = {"Professors Name": "NA", "Designation": "NA", "Department": "NA", "Email": "NA", "Number": "NA",
         "Research Interests": "NA", "Current Research Profile": "NA", "Google Scholar Link": "NA", "LinkedIn": "NA"}
    continue_link = driver.find_element(By.XPATH, '/html/body/div[4]/section[2]/div/div/div/div/div[2]/div['+str(i)+']/div/div[2]/h4/a')
    d.update({"Professors Name":continue_link.text})
    continue_link.click()
    try:
        continue_link = driver.find_element(By.XPATH, '/html/body/div[4]/section[2]/div/div/div[2]/div/div/span')
        d.update({"Designation":continue_link.text.split(", ")[0],"Department":continue_link.text.split(", ")[1].split("\n")[0]})
    except:
        pass
    try:
        continue_link = driver.find_element(By.XPATH, '/html/body/div[4]/section[2]/div/div/div[2]/div/p[3]')
        d.update({"Email":continue_link.text.replace(" -AT- ","@")[7:]})
    except:
        pass
    try:
        continue_link = driver.find_element(By.XPATH, '/html/body/div[4]/section[3]/div/div/div[2]/div/div/ul')
        d.update({"Research Interests":continue_link.text})
    except:
        pass
    try:
        continue_link = driver.find_element(By.XPATH, '/html/body/div[4]/section[2]/div/div/div[2]/div/p[5]')
        for k in continue_link.text.split("\n"):
            if(k.startswith("VOIP: ")):
                d.update({"Number":"0792395"+k[6:].strip(" (lab)").strip(" -- joining_soon: no")})
    except:
        pass
    try:
        l=[]
        j=1
        while True:
            continue_link = driver.find_element(By.XPATH, '/html/body/div[4]/section[3]/div/div/div[1]/div/ul[2]/li[1]/div/ol/li['+str(j)+']/p')
            l.append(str(j)+" "+continue_link.text)
            j=j+1
    except:
        if(len(l)>0):
            d.update({"Current Research Profile":"\n".join(l)})
    m.append(d)
    driver.back()
print(m)
with open('professors.csv', 'w',newline="",encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = m[0].keys())
    writer.writeheader()
    writer.writerows(m)