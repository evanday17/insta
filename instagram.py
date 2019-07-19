from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys


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
        
    
        #  find the login field and then enter login info
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)
        user_name = self.driver.find_element_by_name('username')
        user_name.send_keys(self.username)
    
        #  find the pw field and then enter pw
        pass_word = self.driver.find_element_by_name('password')
        pass_word.send_keys(self.password)
    
        #find submit button and click
        driver.find_element_by_xpath('//button[@type ="submit"]').click()
      

    def followers(self):
        #driver.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        #follower = self.driver.find_element_by_type('Search')
        #follower.send_keys(self.follwer)
        #pass
        #driver.find_element_by_xpath('//class[contains(text(), "Not Now")]').click()
        driver.find_element_by_xpath('//button[@class ="mt3GC"]').click()


def main():
    print('Hello, welcometo my instagram bot')
    username = input('enter your username: ')
    password = input('enter your password: ')
    follower = input('enter an account so we can target their followers: ')
    
    user = instagram(username, password, follower)
    user.login()
        
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
