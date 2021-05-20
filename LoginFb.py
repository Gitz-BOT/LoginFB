import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

keyboard = Controller()
time.sleep(3)

driver = webdriver.Chrome(executable_path="E:/PY/driver/chromedriver.exe")
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

i=1
while i<=5:
    keyboard.press('j')
    keyboard.release('j')

    time.sleep(2)

    keyboard.press('l')
    keyboard.release('l')

    time.sleep(2)

    keyboard.press('right arrow')
    keyboard.release('right arrow')
    
    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    i += 1;




# driver.quit()
