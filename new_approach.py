from selenium import webdriver
import csv
from time import sleep
import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd
import math
from selenium.webdriver.common.keys import Keys
from pandas import DataFrame as df
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome('/Users/colegulledge/desktop/chromedriver 4', chrome_options=chrome_options)

contents = []
dates = []
comments = []
qualityz = []
ratingz = []
tagz = []
course_codez = []
master = []
namez = []
lst = []
namez1 = []
firstnamez = []
with open('safe_urls.csv', 'rt') as cp_csv:
    cp_url = csv.reader(cp_csv)
    for row in cp_url:
        links = row[0]
        contents.append(links)
for link in contents:
    driver.get(link)
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    amt_ratings = []
    amt = driver.find_elements_by_css_selector(
        '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(1) > div.RatingValue__NumRatings-qw8sqy-0.jMkisx > div > a')
    for p in range(len(amt)):
        amt_ratings.append(amt[p].text.strip().split('\n'))
    [amt_ratings] = amt_ratings
    makeitastring = ''.join(map(str, amt_ratings))
    final = int(makeitastring.replace('ratings', ''))
    #loops = math.floor((final - 20) / 10)
    loops = math.ceil(((final - 20) / 10))
    print(loops)
    if loops >= 1:
        i = 0
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        sleep(1)
        #button = driver.find_elements_by_class_name("PaginationButton__StyledPaginationButton-txi1dr-1")
        #button = driver.find_elements_by_css_selector("#react-tabs-681939 > button")
        # while i < loops:
        #     try:
        #         i = i + 1
        #         button[0].click()
        #         sleep(2)
        #         #i = i + 1
        #         print(i)
        #
        #     except StaleElementReferenceException:
        #         pass
        wait = WebDriverWait(webdriver, 10)
        try:
            #wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'PaginationButton__StyledPaginationButton-txi1dr-1')))
            while EC.element_to_be_clickable((By.CLASS_NAME, 'PaginationButton__StyledPaginationButton-txi1dr-1')):
                button = driver.find_elements_by_class_name("PaginationButton__StyledPaginationButton-txi1dr-1")
                button[0].click()
                sleep(2)
                if not button[0].is_enabled():
                    sleep(10)
                    button[0].click()

        except StaleElementReferenceException:
            pass
            #wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'PaginationButton__StyledPaginationButton-txi1dr-1')))
    else:
        pass

    date = driver.find_elements_by_class_name(
        "TimeStamp__StyledTimeStamp-sc-9q2r30-0.bXQmMr.RatingHeader__RatingTimeStamp-sc-1dlkqw1-3.BlaCV")
    comment = driver.find_elements_by_class_name("Comments__StyledComments-dzzyvm-0")
    quality = driver.find_elements_by_xpath('//*[@id="ratingsList"]/li/div/div/div[2]/div[1]/div[2]')
    difficulty = driver.find_elements_by_class_name("RatingValues__RatingValue-sc-6dc747-3.jILzuI")
    tags = driver.find_elements_by_class_name("RatingTags__StyledTags-sc-1boeqx2-0")
    course_code = driver.find_elements_by_class_name("RatingHeader__StyledClass-sc-1dlkqw1-2.gxDIt")
    cluster = driver.find_elements_by_class_name("Rating__RatingBody-sc-1rhvpxz-0.dGrvXb")
    trial = driver.find_elements_by_class_name("Tag-bs9vf4-0.hHOVKF")
    first_name = driver.find_elements_by_css_selector('#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG > span:nth-child(1)')
    last_name_take2 = driver.find_elements_by_css_selector('#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG > span.NameTitle__LastNameWrapper-dowf0z-2.glXOHH')
    for i in range(len(date)):
        dates.append(date[i].text.strip())
    for r in range(1, len(comment)):
        comments.append(comment[r].text.strip())  # shoud i split as well?
    for f in range(len(quality)):
        qualityz.append(quality[f].text.strip())
    for q in range(len(difficulty)):
        ratingz.append(difficulty[q].text.strip())
    for w in range(len(course_code)):
        course_codez.append(course_code[w].text.strip())
    for fly in range(len(last_name_take2)):
         namez1.extend([last_name_take2[fly].text.strip()] * final)
    for first in range(len(first_name)):
         firstnamez.extend([first_name[first].text.strip()] * final)

    for x in cluster:
        try:
            child = x.find_element_by_class_name("RatingTags__StyledTags-sc-1boeqx2-0")
            lst.append(child.text.replace('\n',', '))
        except:
            lst.append('NA, NA, NA')


dates = list(filter(None, dates))
course_codez = list(filter(None, course_codez))
print(len(firstnamez))
print(len(dates))
if len(firstnamez) != len(dates):
    sys.exit("Lengths are not equal, something has gone wrong")
else:
    pass


master_two = [(fname, lname, time, qual, rat, code, ments, *tagie.split(", ")) for fname, lname, time, qual, rat, code, ments, tagie in zip(firstnamez, namez1, dates, qualityz, ratingz, course_codez, comments, lst)]
master_two = [list(ele) for ele in master_two]

for i in master_two:
    if len(i) == 8:#was 7
        i = i.extend(['NA','NA'])
    elif len(i) == 9: #was 8
        i = i.append('NA')
    else:
        pass
print(len(master_two))
column_names =['fname', 'lname', 'date', 'quality', 'difficulty','course_code','comment', 'tag1', 'tag2', 'tag3']
df = pd.DataFrame(master_two, columns=column_names)
print(df.shape)
print(df.head(30))
df.to_csv(r'/Users/colegulledge/Desktop/Spring_2020/indy/ratemyprof/main/all_reviews_hopefully.csv')
