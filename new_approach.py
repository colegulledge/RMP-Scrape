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
from selenium.webdriver.common.action_chains import ActionChains
from pandas import DataFrame as df
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-notifications')
driver = webdriver.Chrome('/Users/colegulledge/desktop/chromedriver 4', chrome_options=options)

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
wta = []
average_dif_proff = []
with open('813matchingurls.csv', 'rt') as cp_csv:
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
    clicks = math.ceil(((final - 20) / 10))
    print(clicks)
    # driver.execute_script("arguments[0].click()", button) #this is the answer to my issue.. but i do not know how to get it
    ##to itereate untill the button no longer exists, and how to append it to next page
    if clicks >= 1:
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        sleep(1)
        # try:
        #     while EC.element_to_be_clickable((By.XPATH, '/ html / body / div[2] / div / div / div[4] / div[4] / div / div / button')):
        #         button = driver.find_elements_by_xpath("/ html / body / div[2] / div / div / div[4] / div[4] / div / div / button")
        #         button[0].click()
        #         sleep(2)
        #         if not button[0].is_enabled():
        #             print('ad is covering button, hopefully this works')
        #             wait2 = WebDriverWait(driver, 150)
        #             wait2.until(EC.element_to_be_clickable(By.XPATH("/ html / body / div[2] / div / div / div[4] / div[4] / div / div / button").click()))
        #
        # except StaleElementReferenceException:
        #     pass
        wait = WebDriverWait(driver, 10)
        while True:
            try:
                elem = wait.until(EC.element_to_be_clickable((By.XPATH, "/ html / body / div[2] / div / div / div[4] / div[4] / div / div / button")))
                driver.execute_script("arguments[0].click();", elem)
            except TimeoutException:
                print('timeout')
                break
            except StaleElementReferenceException:
                print('stale')
                break
    else:
        print('under 10 reviews')
        pass

    # date = driver.find_elements_by_class_name(
    #     "TimeStamp__StyledTimeStamp-sc-9q2r30-0.bXQmMr.RatingHeader__RatingTimeStamp-sc-1dlkqw1-3.BlaCV")
    # comment = driver.find_elements_by_class_name("Comments__StyledComments-dzzyvm-0")
    # quality = driver.find_elements_by_xpath('//*[@id="ratingsList"]/li/div/div/div[2]/div[1]/div[2]')
    # difficulty = driver.find_elements_by_class_name("RatingValues__RatingValue-sc-6dc747-3.jILzuI")
    # tags = driver.find_elements_by_class_name("RatingTags__StyledTags-sc-1boeqx2-0")
    # course_code = driver.find_elements_by_class_name("RatingHeader__StyledClass-sc-1dlkqw1-2.gxDIt")
    # cluster = driver.find_elements_by_class_name("Rating__RatingBody-sc-1rhvpxz-0.dGrvXb")
    # trial = driver.find_elements_by_class_name("Tag-bs9vf4-0.hHOVKF")
    # first_name = driver.find_elements_by_css_selector('#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG > span:nth-child(1)')
    # last_name_take2 = driver.find_elements_by_css_selector('#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG > span.NameTitle__LastNameWrapper-dowf0z-2.glXOHH')

    date = driver.find_elements_by_class_name(
        "TimeStamp__StyledTimeStamp-sc-9q2r30-0.bXQmMr.RatingHeader__RatingTimeStamp-sc-1dlkqw1-3.BlaCV")
    #perc_wta = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[4]/div[1]/div[1]/div[3]/div[1]/div[1]')
    avg_diff = driver.find_elements_by_css_selector(
        '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div.TeacherFeedback__StyledTeacherFeedback-gzhlj7-0.cxVUGc > div:nth-child(2) > div.FeedbackItem__FeedbackNumber-uof32n-1.kkESWs')
    comment = driver.find_elements_by_xpath('//*[@id="ratingsList"]/li/div/div/div[3]/div[3]')
    quality = driver.find_elements_by_xpath('//*[@id="ratingsList"]/li/div/div/div[2]/div[1]/div/div[2]')
    difficulty = driver.find_elements_by_xpath('//*[@id="ratingsList"]/li/div/div/div[2]/div[2]/div/div[2]')
    tags = driver.find_elements_by_class_name("RatingTags__StyledTags-sc-1boeqx2-0")
    course_code = driver.find_elements_by_class_name("RatingHeader__StyledClass-sc-1dlkqw1-2.gxDIt")
    cluster = driver.find_elements_by_class_name("Rating__RatingBody-sc-1rhvpxz-0.dGrvXb")
    trial = driver.find_elements_by_class_name("Tag-bs9vf4-0.hHOVKF")
    first_name = driver.find_elements_by_css_selector(
        '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG > span:nth-child(1)')
    last_name_take2 = driver.find_elements_by_css_selector(
        '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(2) > div.NameTitle__Name-dowf0z-0.cfjPUG > span.NameTitle__LastNameWrapper-dowf0z-2.glXOHH')

    for i in range(len(date)):
        dates.append(date[i].text.strip())
    for r in range(len(comment)):
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
    #for jj in range(len(perc_wta)):
        #wta.extend([perc_wta[jj].text.strip()] * final)
    # for ff in range(len(avg_diff)):
    #     average_dif_proff.extend([avg_diff[ff].text.strip()] * final)
    for x in cluster:
        try:
            child = x.find_element_by_class_name("RatingTags__StyledTags-sc-1boeqx2-0")
            lst.append(child.text.replace('\n',', '))
        except:
            lst.append('NA, NA, NA')
    if len(comments) == len(firstnamez):
        print('This Url has been scrapped and all is good')
        print(len(comments))
    else:
        sys.exit('Lengths r not equal prelim')
    if (len(comments)*2) != len(course_codez):
        print(namez1)
        print(firstnamez)
        sys.exit("the last name in the above list is the bastard with the missing coursecode")
    else:
        pass


dates = list(filter(None, dates))
course_codez = list(filter(None, course_codez))
print(len(course_codez))
print(len(dates))
if len(firstnamez) == len(dates):
    print('all gucci, time to zip')
else:
    sys.exit("Lengths are not equal, something has gone wrong")


# master_two = [(fname, lname, time, qual, rat, code, ments, *tagie.split(", ")) for fname, lname, time, qual, rat, code, ments, tagie in zip(firstnamez, namez1, dates, qualityz, ratingz, course_codez, comments, lst)]
# master_two = [list(ele) for ele in master_two]
print(len(firstnamez))
print(len(comments))
print(len(course_codez))
print(len(namez1))
print(len(qualityz))
print(len(ratingz))
print(len(dates))
master_two = [(fname, lname, time, qual, rat, code, ments, *tagie.split(", ")) for fname, lname, time, qual, rat, code, ments, tagie, in zip(firstnamez, namez1, dates, qualityz, ratingz, course_codez, comments, lst,)]
master_two = [list(ele) for ele in master_two]
print(len(master_two))
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
print('holyfuckyoudidit')
df.to_csv(r'/Users/colegulledge/Desktop/Spring_2020/indy/ratemyprof/main/ALLLREVIEWSHOPEFULLYTAKE5.csv')
