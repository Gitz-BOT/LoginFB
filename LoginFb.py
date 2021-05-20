import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

keyboard = Controller()

driver = webdriver.Chrome(executable_path="E:/PY/driver/operadriver.exe")
driver.get ("https://vi-vn.facebook.com")

email = driver.find_element_by_id('email')
email.send_keys("bothuan24680@gmail.com")
time.sleep(5)

passw = driver.find_element_by_id('pass')
passw.send_keys("Th0186997")
time.sleep(5)

btnLogin = driver.find_element_by_name('login')
btnLogin.send_keys(Keys.ENTER)
time.sleep(5)

i=1
while i<=5:
    keyboard.press('j')
    keyboard.release('j')

    time.sleep(2)

    keyboard.press('l')
    keyboard.release('l')

    time.sleep(2)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    i += 1;




# driver.quit()
