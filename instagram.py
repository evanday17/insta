from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import instaloader
from selenium.webdriver.chrome.options import Options



# ***need to add in random sleep times after diff actions tolook human
# *** use this: time.sleep(random.randrange(30))

username = 'e_day_17'
password = 'Slipknot*8'
follower = 'ccdsips'
followers = []
followers_2 = []

#need this to access instaloader....i think = )
#this will login using instaloader and then grab all followers and add to a list
L = instaloader.Instaloader()
L.login(username,password)
profile = instaloader.Profile.from_username(L.context, follower)
for follower in profile.get_followers():
    followers.append(follower.username)

print('****************************************************')
print(len(followers), ' profiles have been added to your list of people to follow')
print('****************************************************')
#  test to see if it workins: print(followers[0])



'''now that we have our list of followers we need to login into insta
 and follow our list.  '''
 
# login and click that annoying pop up window
driver = webdriver.Chrome( executable_path = r'C:\Users\EDay\Desktop\chromedriver.exe')
driver.get('https://www.instagram.com/accounts/login/')
time.sleep(4)

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(password)

driver.find_element_by_xpath('//button[@type ="submit"]').click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aOOlW.HoLwm"))).click()

# let's loop through the followers, and follow each person
# use selenium to open follwer page and click follow button


i = 0
while i < 100 :
    followers_2.append(followers[i])
    i += 1
    
for f in followers_2:
        driver.get('https://www.instagram.com/' + f + '/')
        followButton = driver.find_element_by_css_selector('button')
        if (followButton.text != 'Following'):
            followButton.click()
            print('Followed ', f)
            time.sleep(random.randrange(600))
        else:
            print("You are already following ", f)

    
print('****************************************************')
print("time to sleep before unfollowing")
print('****************************************************')
time.sleep(600) # sleep for 10 minutes
    

for f in followers_2:
    driver.get('https://www.instagram.com/' + f + '/')
    followButton = driver.find_element_by_css_selector('button')
    if (followButton.text == 'Following'):
        followButton.click()
        time.sleep(random.randrange(600))
        confirmButton = driver.find_element_by_xpath('//button[text() = "Unfollow"]')
        confirmButton.click()
        print('Unfollowed ', f)
    elif (followButton.text == 'Follow Back'):
        followButton.click()
        time.sleep(random.randrange(600))
        confirmButton = driver.find_element_by_xpath('//button[text() = "Unfollow"]')
        confirmButton.click()
        print('Unfollowed ', f)
    else:
        print("You are not following ", f)

    

'''
follow function 
#goes to profile and clicks on followers
follower_list = []
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(follower)
time.sleep(5)
driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys(Keys.ENTER,Keys.ENTER)
time.sleep(3)
driver.find_element_by_css_selector('ul li a').click()



#self.browser.close()'''
