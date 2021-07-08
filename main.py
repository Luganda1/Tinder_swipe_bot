from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint
import time

EMAIL = ""
PASSWORD = ""
chrome_driver_path = r"C:\Users\tramr\OneDrive\Desktop\website\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app/recs")# main_page = driver.current_window_handle
# loginig in to tinder
driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
time.sleep(5)
# using facebook to login
facebook_login = driver.find_element_by_xpath('//*[@id="t1738222425"]/div/div/div[1]/div/div[3]/span/div[2]/button')
facebook_login.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element_by_name("email")
email.send_keys(EMAIL)
password = driver.find_element_by_name("pass")
password.send_keys(PASSWORD)
sign_in = driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

driver.switch_to.window(base_window)
print(driver.title)
time.sleep(15)
# facebook_login.click()

# clicking on the allow location
driver.find_element_by_css_selector('#t1738222425 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$primary-gradient\).button--primary-shadow.StyledButton.Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)').click()

time.sleep(5)
# accepting notification
driver.find_element_by_css_selector('#t1738222425 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$primary-gradient\).button--primary-shadow.StyledButton.Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)').click()
time.sleep(5)
# accepting cookies
driver.find_element_by_xpath('//*[@id="t-828363795"]/div/div[2]/div/div/div[1]/button').click()
for _ in range(1, 100):
    time.sleep(2)
    try:
         #swipping left
        driver.find_element_by_css_selector('#t-828363795 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-like-green\) > button').click()
    except ElementClickInterceptedException:
        print("work on this")
        continue






print("''''")

time.sleep(60)
driver.quit()