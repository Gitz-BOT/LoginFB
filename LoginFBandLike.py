from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}

chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.maximize_window()
driver.get("https://www.facebook.com/")
driver.find_element_by_id("email").send_keys("bothuan24680@gmail.com")
time.sleep(2)
driver.find_element_by_id("pass").send_keys("Th0186997")
time.sleep(2)
driver.find_element_by_name("login").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
likes = driver.find_elements_by_xpath(
    "//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
actions = ActionChains(driver)
print(len(likes))
time.sleep(5)
for i in range(0, 5):
    actions.move_to_element(likes[i]).perform()
    driver.execute_script("arguments[0].click();", likes[i])