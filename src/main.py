import time
import json
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException        

json_file = open("../config.json")
variables = json.load(json_file)
json_file.close()
email = variables["email"]
password = variables["password"]
t2fa = variables["t2fa"]

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://discord.com/app/')
source = driver.page_source, 'lxml'
email_box = driver.find_element_by_name('email')
password_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
email_box.send_keys(email)
password_box.send_keys(password)
submit_button.click()

try:
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/h5/span')
except NoSuchElementException:
    invalidpasemail = False
invalidpasemail = True

if invalidpasemail == False:
    print("Invalid email or password! Please double check the config.json file to make sure you didn't make a typo!")
else:
    try:
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/form/div/div[3]/div/h5/span')
    except NoSuchElementException:
        input2fa = False
    input2fa = True

    if input2fa == False:
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[3]/div/div/input').send_keys(t2fa)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[3]/button[1]').click()

        try:
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/form/div/div[3]/div/h5/span')
        except NoSuchElementException:
            invalid2fa = False
        invalid2fa = True

        if invalid2fa == True:
            print("2FA code is invalid! Please use valid backup or authenticator code!")
        else:
            print('Valid 2fa!')
    else:

        time.sleep(5)
        try:
            driver.find_element_by_xpath('//*[@id="private-channels-0"]/div')
        except NoSuchElementException:
            friendsbutton = False
        friendsbutton = True

        try:
            driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/form/div/img')
        except NoSuchElementException:
            logo2fa = False
        logo2fa = True

        if friendsbutton == True & logo2fa == False:
            print('Successfully Logged in!')
        else:
            print('An error occured!')