#!  ver.2.7
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.remote.webdriver as tab
import time

#bro = webdriver.Firefox()
#bro.get('http://javascriptist.net/ref/form.submit.html')
#usern = bro.find_element_by_name('name')
#with open("A.cpp") as f:
#	usern.send_keys(souce_code)
#time.sleep(50)

bro = webdriver.Firefox()
bro.get('http://redmine.nphantom.com')
usern = bro.find_element_by_id('username')
usern.send_keys('kei')
passw = bro.find_element_by_id('password')
passw.send_keys('12223124a'+Keys.ENTER)

#wid = tab.window_handles()
#tab.switch_to_window("brow")
brow = webdriver.Firefox()
brow.get('http://gitlab.nphantom.com')
userna = brow.find_element_by_id('user_login')
userna.send_keys('kei')
passwo = brow.find_element_by_id('user_password')
passwo.send_keys('12223124a'+Keys.ENTER)
#tab.switch_to_window(wid)
