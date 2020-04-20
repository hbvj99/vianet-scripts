# ISCOM HT803-1GE EPON Home Terminal
# Generate new public IP through reconnect

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, NoSuchFrameException
from requests import get
import sys
import credentials as c

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
 
def LoginRouter():
    driver.get('http://192.168.1.1/admin/login.asp')
    driver.find_element(By.ID, 'username').click()
    driver.find_element(By.ID, 'username').click()
    element = driver.find_element(By.ID, 'username')
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.ID, 'username').send_keys(c.router_usr)
    driver.find_element(By.ID, 'psd').send_keys(c.router_psw)
    driver.find_element(By.CSS_SELECTOR, '.button:nth-child(1)').click()
    try:
        driver.find_element(By.CSS_SELECTOR, 'body > blockquote > form > table > tbody > tr:nth-child(1) > td > h4')
        sys.exit('ERROR! Superadmin login credential incorrect')
    except NoSuchElementException:
        pass
    driver.switch_to.frame(0)   
    
def NewIp():
    driver.find_element(By.CSS_SELECTOR, 'td:nth-child(2) > p').click()
    driver.find_element(By.CSS_SELECTOR, 'td:nth-child(2) span').click()
    element = driver.find_element(By.CSS_SELECTOR, 'td:nth-child(2) span')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, 'body')
    actions = ActionChains(driver)
    driver.switch_to.default_content()
    driver.switch_to.frame(2)
    element = driver.find_element(By.CSS_SELECTOR, '.button:nth-child(39)')
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR, '.button:nth-child(39)').click()
    driver.find_element(By.CSS_SELECTOR, 'input').click()
    
    geo = get('http://ip-api.com/json').json()    
    print('SUCCESS! New public IP is '+geo['query']+' by '+geo['isp'])       

if __name__ == '__main__':
    LoginRouter()
    NewIp()
    driver.quit()