import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pytest

# tắt thông báo
options = Options()
options.add_argument("--disable-notifications")
# tạo webdriver
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
#độ lớn cửa sổ trình duyệt
driver.maximize_window()

#link dẫn tới trang web
driver.get ("https://vi-vn.facebook.com")
time.sleep(2)

# tìm id email và nhập email
email = driver.find_element_by_id('email')
email.send_keys("@gmail.com")
time.sleep(2)

# tìm id pass và nhập pass
passw = driver.find_element_by_id('pass')
passw.send_keys("")
time.sleep(2)

# tìm name login và đăng nhập
btnLogin = driver.find_element_by_name('login')
btnLogin.send_keys(Keys.ENTER)
time.sleep(2)


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
# likes = driver.find_elements_by_xpath(
#     "//div[@class='tvfksri0 ozuftl9m']//div[@aria-label='Thích']")
likes = driver.find_elements_by_xpath("//div[@class='tvfksri0 ozuftl9m']//span[text() = 'Thích']")
actions = ActionChains(driver)
print(len(likes))
time.sleep(5)

for i in range(1, 5):
    actions.move_to_element(likes[i]).perform()
    driver.execute_script("arguments[0].click();", likes[i])
driver.quit()



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
