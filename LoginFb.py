import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller

keyboard = Controller()
time.sleep(3)

driver = webdriver.Chrome(executable_path="E:/PY/driver/operadriver.exe")
driver.get ("https://vi-vn.facebook.com")

email = driver.find_element_by_id('email')
email.send_keys("@gmail.com")
time.sleep(2)

passw = driver.find_element_by_id('pass')
passw.send_keys("")
time.sleep(2)

btnLogin = driver.find_element_by_name('login')
btnLogin.send_keys(Keys.ENTER)
time.sleep(2)


i=1
while i<=5:

    btnLike = driver.find_element_by_css_selector('#mount_0_0_ID > div > div:nth-child(1) > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.pfnyh3mw.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.dp1hu0rb.p01isnhg > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.g5gj957u.pmt1y7k9.buofh1pr.hpfvmrgz.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.f7vcsfb0.fjf4s8hc.b6rwyo50.oyrvap6t > div > div > div:nth-child(3) > div > div.pedkr2u6.tn0ko95a.pnx7fd3z > div > div:nth-child(2) > div > div > div > div > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(4) > div > div > div:nth-child(1) > div > div.tvfksri0.ozuftl9m > div > div:nth-child(1) > div.oajrlxb2.gs1a9yip.g5ia77u1.mtkw9kbi.tlpljxtp.qensuy8j.ppp5ayq2.goun2846.ccm00jje.s44p3ltw.mk2mc5f4.rt8b4zig.n8ej3o3l.agehan2d.sk4xxmp2.rq0escxv.nhd2j8a9.pq6dq46d.mg4g778l.btwxx1t3.pfnyh3mw.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.tgvbjcpo.hpfvmrgz.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.l9j0dhe7.i1ao9s8h.esuyzwwr.f1sip0of.du4w35lb.lzcic4wl.abiwlrkh.p8dawk7l')

    # keyboard.press('j')
    # keyboard.release('j')
    #
    # time.sleep(2)
    #
    # keyboard.press('l')
    # keyboard.release('l')
    #
    # time.sleep(2)
    #
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    i += 1




# driver.quit()
