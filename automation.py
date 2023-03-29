from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

web = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
web.get('https://forms.gle/tysEFsyj9TBpV6Dc6')
time.sleep(2)

FirstName = "Kaan"
first = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

LastName = "Eren"
last = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

RadioButtonPeriod = web.find_element(By.XPATH,'//*[@id="i16"]/div[3]/div')
RadioButtonPeriod.click()

Submit = web.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
Submit.click()

get_confirmation_div_text = web.find_element(By.CSS_SELECTOR, value = '.vHW8K')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Yanıtınız kaydedildi."):
    print("Test was successful")
else:
    print("Test was not successful")
time.sleep(5)




