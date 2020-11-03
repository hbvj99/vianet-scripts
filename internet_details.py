# Collect Vianet Internet details

from router_change_ip import *
import credentials as c
import time as t

def LoginVianet():
    driver.get('https://customers.vianet.com.np/customers/login')
    driver.find_element(By.NAME, 'username').click()
    driver.find_element(By.NAME, 'username').click()
    element = driver.find_element(By.NAME, 'username')
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.NAME, 'username').send_keys(c.vianet_usr)
    driver.find_element(By.NAME, 'password').click()
    driver.find_element(By.NAME, 'password').send_keys(c.vianet_psw)
    driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
    try:
        driver.find_element(By.CSS_SELECTOR, ".btn-login").click()
        sys.exit('ERROR! Login credential incorrect')
    except (NoSuchElementException, TypeError):
        pass
        
def GetDetails():
    driver.get('https://customers.vianet.com.np/services/internet')
    username = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(2) > td:nth-child(2)").text
    endDate = driver.find_element_by_xpath("//*[@id='stat2']/div[5]/span").text.split(' ')[2]
    speed = driver.find_element(By.CSS_SELECTOR, ".stat3 span").text
    fupStatus = driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > span").text.split('/')[0]
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(6) > span").click()
    t.sleep(0.)
    usages = driver.find_element(By.CSS_SELECTOR, "#tblUsageData .ttldownload").text
    month = driver.find_element(By.CSS_SELECTOR, '#month').text
    driver.get('https://customers.vianet.com.np/customers/logout')
    print(f'Hi, {username} you are subscribed to {speed}. It is currently {fupStatus}, your Internet bill is due at {endDate}. You have used {usages} bandwidth.')
   
if __name__ == '__main__':
    LoginVianet()
    GetDetails()
    driver.quit()
