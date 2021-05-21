import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
from selenium.webdriver.common.action_chains import ActionChains


# keyboard = Controller()
# time.sleep(3)

options = Options()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome("E:/PY/driver/chromedriver.exe",chrome_options=options)
driver.maximize_window()

driver.get ("https://vi-vn.facebook.com")

email = driver.find_element_by_id('email')
email.send_keys("bothuan24680@gmail.com")
time.sleep(2)

passw = driver.find_element_by_id('pass')
passw.send_keys("Th0186997")
time.sleep(2)

btnLogin = driver.find_element_by_name('login')
btnLogin.send_keys(Keys.ENTER)
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(2)
likes = driver.find_elements_by_xpath(
    "//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
actions = ActionChains(driver)
print(len(likes))
time.sleep(5)
for i in range(0, 5):
    actions.move_to_element(likes[i]).perform()
    driver.execute_script("arguments[0].click();", likes[i])



# i=0
# while i<=5:
#
#     keyboard.press('j')
#     keyboard.release('j')
#
#     time.sleep(2)
#
#     keyboard.press('l')
#     keyboard.release('l')
#
#     time.sleep(2)
#
#     keyboard.press(Key.enter)
#     keyboard.release(Key.enter)
#
#     i += 1




# driver.quit()
