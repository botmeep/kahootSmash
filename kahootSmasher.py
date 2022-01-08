"""
  _         _                 _    _____                     _     
 | |       | |               | |  / ____|                   | |    
 | | ____ _| |__   ___   ___ | |_| (___  _ __ ___   __ _ ___| |__  
 | |/ / _` | '_ \ / _ \ / _ \| __|\___ \| '_ ` _ \ / _` / __| '_ \ 
 |   < (_| | | | | (_) | (_) | |_ ____) | | | | | | (_| \__ \ | | |
 |_|\_\__,_|_| |_|\___/ \___/ \__|_____/|_| |_| |_|\__,_|___/_| |_|

Created by switchmeep.
Thank you for using kahootSmash.

"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random, string, time, ctypes

ctypes.windll.kernel32.SetConsoleTitleA("kahootSmasher")
chrome_options = Options()
chrome_options.add_argument("--incognito --disable-logging --log-level=3")

PATH = '.\chromedriver.exe'
driver = webdriver.Chrome(executable_path = PATH, chrome_options=chrome_options)
kahootUrl = 'https://kahoot.it/'
tabNum = 0

pin = input("Game Pin:\n")

def randomString():
    letters = string.ascii_lowercase
    outputString = ''.join(random.choice(letters) for i in range(10))
    return outputString

def createBot(gamePin):
    global tabNum, driver, kahootUrl
    driver.get(kahootUrl)
    inputBox = driver.find_element_by_id('game-input')
    inputBox.click()
    inputBox.send_keys(gamePin)
    inputBox.send_keys(Keys.RETURN)

    try:
        time.sleep(2)
        randomUser = randomString()
        nicknameBox = driver.find_element_by_id('nickname')
        nicknameBox.click()
        nicknameBox.send_keys(randomUser)
        nicknameBox.send_keys(Keys.RETURN)
    except:
        print("Invalid Game Pin!")
        exit()

    time.sleep(3)
    driver.execute_script("window.open('');")
    tabNum = tabNum + 1
    driver.switch_to.window(driver.window_handles[tabNum])
    
while True:
    createBot(pin)