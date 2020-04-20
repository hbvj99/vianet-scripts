#Reboot device

from router_change_ip import *

def RbtDevice():
    driver.find_element(By.CSS_SELECTOR, 'td:nth-child(5) b span').click()
    element = driver.find_element(By.CSS_SELECTOR, 'td:nth-child(5) b span')
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR, 'body')
    actions = ActionChains(driver)
    driver.find_element(By.CSS_SELECTOR, 'td:nth-child(5) > p > a > span').click()
    driver.switch_to.default_content()
    driver.switch_to.frame(2)
    driver.find_element(By.CSS_SELECTOR, 'input:nth-child(1)').click()
    driver.find_element(By.CSS_SELECTOR, 'input').click()
    print('SUCCESS! Device is rebooting...')

if __name__ == '__main__':
    LoginRouter()
    RbtDevice()
    driver.quit()
