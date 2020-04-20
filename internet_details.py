# Collect Vianet Intetnet details

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
    driver.find_element(By.NAME, 'btnLogin').click()
    try:
        driver.find_element(By.CSS_SELECTOR, 'body > div.container.login > div:nth-child(1) > div.col-sm-12.col-md-4 > div > div')
        sys.exit('ERROR! Login credential incorrect')
    except NoSuchElementException:
        pass
        
def GetDetails():
    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()
    username = driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(3) > td').text
    speed = driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(2)').text
    fupStatus = driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(2)').text
    endDate = driver.find_element(By.CSS_SELECTOR, 'tbody:nth-child(1) > tr:nth-child(8) > td').text
    driver.find_element(By.ID, 'tab_usage').click()
    t.sleep(0.7)
    usages = driver.find_element(By.CSS_SELECTOR, '.ttldownload').text
    month = driver.find_element(By.CSS_SELECTOR, '#month').text
    driver.get('https://customers.vianet.com.np/customers/logout')
    print('Hi, '+username+' you are subscribed to '+speed+'. It is currently '+fupStatus+' and your Internet bill is due at '+endDate+'. You have used '+usages+' bandwidth')
   
if __name__ == '__main__':
    LoginVianet()
    GetDetails()
    driver.quit()
