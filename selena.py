from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# browser.set_window_size(766, 1154)
browser.set_window_size(513, 800)
browser.set_window_position(0, 0)
browser.get('https://fidibo.com/login/simple?callback=library')
# browser.get('http://howbigismybrowser.com/')

assert browser.find_element_by_link_text('ورود به فیدیبو')
sleep(3)
login_or_reg = browser.find_element_by_id('RegisterOrLoginBtn')
login_or_reg.click()
sleep(1)
email_box = browser.find_element_by_id('loginEmail')
email_box.send_keys('aaaaaaaaaalllllllllliiiiiiiiii@gmail.com')
sleep(1)
password_box =browser.find_element_by_id('LoginPassword')
password_box.send_keys('aa1374')
sleep(1)
login_btn = browser.find_element_by_id('LoginBtn')
login_btn.click()
sleep(5)
browser.save_screenshot('./1.png')
page_two = browser.find_element_by_link_text('۲')
page_two.click()

read_online = browser.find_element_by_xpath(
    '/html/body/main/div[1]/div/div/article/div/div[1]/div/div[2]/div[5]/div[2]/div/a[2]')
read_online.click()
browser.switch_to.window(browser.window_handles[-1])
wait = WebDriverWait(browser, 60)
wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, '#loading-placeholder > img')))
sleep(15)


def pagination():
    for i in range(1, 850):
        wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, '#loading-placeholder > img')))
        browser.save_screenshot('%s.png' % (str(i)))
        nxt_page_btn = browser.find_element_by_id('___nextPageMobile')
        nxt_page_btn.click()
        sleep(1)


pagination()


