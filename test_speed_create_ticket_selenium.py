from internet_details import *
from speed_variable import *


def CheckConnectionIssueTicket():
    # Automatically select best near server
    driver.get('http://www.speedtest.net/run')
    t.sleep(40)
    ping = driver.find_element(By.CSS_SELECTOR, '.ping-speed').text
    download = driver.find_element(By.CSS_SELECTOR, '.download-speed').text
    upload = driver.find_element(By.CSS_SELECTOR, '.upload-speed').text
    connection = driver.find_element(
        By.CSS_SELECTOR, '.result-item-connection-mode > .result-data').text
    sponsor = driver.find_element(By.CSS_SELECTOR, '.result-label > a').text
    ip = driver.find_element(By.CSS_SELECTOR, '.js-data-ip').text
    isp = driver.find_element(By.CSS_SELECTOR, '.js-data-isp').text
    url = driver.current_url
    location = driver.find_element(
        By.CSS_SELECTOR, '.result-data.js-sponsor-name').text

    results = {
        'ping': ping,
        'download': download,
        'upload': upload,
        'connection': connection,
        'sponsor': sponsor,
        'ip': ip,
        'isp': isp,
        'url': url,
        'location': location
    }

    msg_footer = '\n\nPlease fix this issue ASAP. thank you\n\n--this message was auto-generated by a bot--'
    msg = 'Hi,\nMy internet connection is slow. The download speed was '+download+'Mbps, upload was '+upload+'Mbps when test was made from ' + \
        location+' hosted by '+sponsor+' with ping '+ping + \
        'ms. My Public IP was '+ip+', refer '+url+' for more info.'+msg_footer
    latency_msg = 'Hi,\nMy internet connection is unstable. The ping was '+ping + \
        'ms when test was made from '+location+' hosted by ' + \
        sponsor+'. Please refer '+url+msg_footer

    def Login():
        LoginVianet()
        driver.get('https://customers.vianet.com.np/services/internet')
        driver.find_element(By.ID, "myTicket").click()
        t.sleep(0.5)
    if (float(download) >= set_download_speed and float(upload) >= set_upload_speed):
        print('Awesome! Your internet connection is fine, no issue ticket was created')
        print('Current download is '+download+'Mbps, upload is '+upload+'Mbps with ping ' +
              ping+'ms when test is made from '+location+' hosted by '+sponsor)
    elif (float(ping) >= set_ping):
        Login()
        driver.find_element(By.ID, 'description').send_keys(latency_msg)
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        print('Internet issue ticket is successfully created and posted as:\n\n'+latency_msg+'\n')
    else:
        Login()
        driver.find_element(By.CSS_SELECTOR, "#internet-Technical > .option_issue_type:nth-child(5)").click()
        driver.find_element(By.ID, "description").click()
        driver.find_element(By.ID, 'description').send_keys(msg)
    try:
        driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
        print('Internet issue ticket is successfully created and posted as:\n\n'+msg+'\n')
    except NoSuchElementException:
        print('Some error occurred! ticket cannot be posted.')

    driver.get('https://customers.vianet.com.np/customers/logout')

if __name__ == '__main__':
    CheckConnectionIssueTicket()
    driver.quit()
