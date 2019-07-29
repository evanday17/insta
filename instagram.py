from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# need to randomize sleep times to look like a human

class instagram():
    
    def __init__(self, username, password,follower):
        self.driver = webdriver.Chrome( executable_path = r'C:\Users\EDay\Desktop\chromedriver.exe')
        self.username = username
        self.password = password
        self.follower = follower
        
        #self.chrome_options = Options()
        #chrome_options.add_argument("--headless")

    def login(self):
        #  open up the page        
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        
        time.sleep(3)
        #  find the login field and then enter login info
        user_name = self.driver.find_element_by_name('username')
        user_name.send_keys(self.username)
    
        #  find the pw field and then enter pw
        pass_word = self.driver.find_element_by_name('password')
        pass_word.send_keys(self.password)
    
        #find submit button and click
        driver.find_element_by_xpath('//button[@type ="submit"]').click()
     
        #wait 10 seconds and click on the not now on the pop up
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

    def followers(self):
        pass


def main():
    print('Hello, welcometo my instagram bot')
    username = input('enter your username: ')
    password = input('enter your password: ')
    follower = input('enter an account so we can target their followers: ')
    
    user = instagram(username, password, follower)
    user.login()
        
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
