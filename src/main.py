import os
import json
from cmd import Cmd
try:
    from colorama import Fore, init
except:
    os.system('pip install colorama')
try:
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
except:
    os.system('pip install selenium')

init(autoreset=True)

json_file = open("../config.json")
variables = json.load(json_file)
json_file.close()
email = variables["email"]
password = variables["password"]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

def online():
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[1]/div').click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="status-picker-online"]/div'))).click()
    print('[STATUS] Successfully changed status to online!')
def idle():
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[1]/div').click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="status-picker-idle"]/div'))).click()
    print('[STATUS] Successfully changed status to idle!')
def dnd():
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[1]/div').click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="status-picker-dnd"]/div'))).click()
    print('[STATUS] Successfully changed status to DND!')
def offline():
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[1]/div').click()
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="status-picker-invisible"]/div'))).click()
    print('[STATUS] Successfully changed status to offline!')

banner = Fore.RED + '''
\n\n
------------------------------------------------\n
 __     __   __   __   __   __              
|  \ | /__` /  ` /  \ |__) |  \             
|__/ | .__/ \__, \__/ |  \ |__/             
                                            
___  __        ___            ___  __   __  
 |  /  \ |__/ |__  |\ | |    |__  /__` /__` 
 |  \__/ |  \ |___ | \| |___ |___ .__/ .__/ 
                                            
 __   ___       ___  __   __  ___           
/__` |__  |    |__  |__) /  \  |            
.__/ |___ |___ |    |__) \__/  |            \n

------------------------------------------------\n\n\n'''

print(banner)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('https://discord.com/app')
WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.NAME, 'email'))).send_keys(email)
print('[LOGIN] Input email')
driver.find_element_by_name('password').send_keys(password)
print('[LOGIN] Input password')
try:
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/div/form/div/div/div[1]/div[2]/button[2]').click()
except NoSuchElementException:
    driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[2]/button[2]').click()
print('[LOGIN] Clicked login button')
try:
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/h5/span')))
    print(Fore.RED + '[LOGIN] Incorrect email or password, please double check the "config.json file"!')
    driver.quit()
    exit()
except:
    pass

try:
    WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div')))
    nd = True
except:
    nd = False

if nd == True:
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/section/div/div[1]')))
        captcha = True
    except:
        captcha = False

    if captcha == True:
        input('[CAPTCHA] A captcha has appeared! Press enter once you are finished!\n')
    elif captcha == False:
        pass

    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/form/div/div[1]')))
        twofa = True
    except:
        twofa = False

    if twofa == True:
        twofacode = input('[2FA] Please enter your 2FA code: ')
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/form/div/div[2]/div/div/input').send_keys(twofacode)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div/form/div/div[2]/button[1]').click()
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/form/div/div[2]/div/h5'))).is_displayed()
            print(Fore.RED + '[2FA] Invalid 2FA code!')
            driver.quit()
            exit()
        except:
            pass
    elif twofa == False:
        pass

elif nd == False:
    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/section/div/div[1]')))
        captcha = True
    except:
        captcha = False

    if captcha == True:
        input('[CAPTCHA] A captcha has appeared! You have 2 options you can take, make ChromeDriver non-headless and restart the program, or, if you already have ChromeDriver in non-headless, solve the captcha on screen and press enter.\n')
    elif captcha == False:
        pass

    try:
        WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[1]')))
        twofa = True
    except:
        twofa = False

    if twofa == True:
        twofacode = input('[2FA] Please enter your 2FA code: ')
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[2]/div/div/input').send_keys(twofacode)
        driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/form/div/div[2]/button[1]').click()
        try:
            WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div/form/div/div[2]/div/h5'))).is_displayed()
            print(Fore.RED + '[2FA] Invalid 2FA code!')
            driver.quit()
            exit()
        except:
            pass
    elif twofa == False:
        pass

print('[LOGIN] Please wait as you are logged in...')

try:
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div[2]/div[3]/button[3]')))
    print(Fore.GREEN + '[LOGIN] Successfully logged in!')
except TimeoutException:
    print(Fore.RED + '[LOGIN] An unexpected error occurred!')
    driver.quit()
    exit()

print('[CMD] To view a list of all current commands in the interactive command prompt, type "help"!')
print('\n\n')

class InteractiveCMD(Cmd):

    def do_exit(self, inp):
        print('[CLOSING] Exiting drivers and closing prompt')
        driver.quit()
        return True
 
    def do_status(self, inp):
        if inp == 'online':
            online()
        elif inp == 'idle':
            idle()
        elif inp == 'dnd':
            dnd()
        elif inp == 'offline':
            offline()
        else:
            print(Fore.RED + 'Invalid arguement(s). Accepted arguments: online, idle, dnd, offline, rainbow')

    def help_exit(self):
       print("Exits the program")

    def help_status(self):
       print("Changes your Discord status | Example usage: status dnd\nAccepted arguments: online, idle, dnd, offline, rainbow")

cmd = InteractiveCMD()
cmd.cmdloop()
print(Fore.GREEN + '[CLOSING] Successfully closed!')