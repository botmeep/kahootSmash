from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import random, string, time, ctypes, threading

ctypes.windll.kernel32.SetConsoleTitleA("kahootSmasher")
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--log-level=3")

PATH = '.\chromedriver.exe'
kahootUrl = 'https://kahoot.it/'
tabNum = 0
threadCount = 0

class Smasher:
    def __init__(self, pin=None):
        self.pin = pin
        self.drivers = []

    def randomString(self):
        letters = string.ascii_lowercase
        outputString = ''.join(random.choice(letters) for i in range(10))
        return outputString

    def createBot(self):
        global tabNum
        bot = webdriver.Chrome(executable_path=PATH, chrome_options=chrome_options)
        self.drivers.append(bot)

        while True:
            bot.get(kahootUrl)
            inputBox = bot.find_element_by_id('game-input')
            inputBox.click()
            inputBox.send_keys(self.pin)
            inputBox.send_keys(Keys.RETURN)

            try:
                time.sleep(2)
                randomUser = self.randomString()
                nicknameBox = bot.find_element_by_id('nickname')
                nicknameBox.click()
                nicknameBox.send_keys(randomUser)
                nicknameBox.send_keys(Keys.RETURN)
            except:
                print("Invalid Game Pin!")
                exit()

            time.sleep(3)
            bot.execute_script("window.open('');")
            tabNum = tabNum + 1
            bot.switch_to.window(bot.window_handles[tabNum])
    
if __name__ == "__main__":
    print(range(2))
    smash = Smasher(input("Game Pin: "))
    threadCount = int(input("Thread Count: "))
    print(f'Flooding with {threadCount} threads.')
    
    for x in range(threadCount):
        print("started thread")
        t = threading.Thread(target=smash.createBot())
        t.start()