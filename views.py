from django.shortcuts import render
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from main.models import Salad, StudentReviews, Trial
import math
from selenium.webdriver.common.keys import Keys

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-notifications')
# driver = webdriver.Chrome('/Users/colegulledge/desktop/chromedriver 4', chrome_options=chrome_options)
#
print("hi Cole")
urlz = Salad.objects.filter(url__contains='h').exclude(avg_rating__isnull=True).values_list('url', flat=True).to_csv('/Users/colegulledge/Desktop/Spring_2020/indy/ratemyprof/main/safeurls.csv')
#
# def scrape(site):
#     # print('hiiii coleeee')
#     driver.get("https://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=College+of+Charleston&schoolID=254&queryoption=TEACHER")
#     #driver.get(site)
#     i = 1
#     button = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div[1]/div/div[5]/div/div[1]")
#     # There are 1700 professors that have been rated at the college of charleston, with
#     #  a twenty displaying on each page, with each 'load' more loading 20 more.
#     # if we would like to scrape all, which i can, i < 86
#     while i < 1:
#         driver.execute_script("arguments[0].click();", button)
#         sleep(2)
#         i = i + 1
#     professor_name = driver.find_elements_by_class_name('name')
#     names = []
#     links = []
#     rate = []
#     for p in range(0, len(professor_name)):
#         names.append(professor_name[p].text.strip().split('\n'))
#     elems = driver.find_elements_by_css_selector("a[href*='tid']")
#     for elem in elems:
#         links.append(elem.get_attribute("href"))
#     ratings = driver.find_elements_by_class_name('rating')
#     for f in range(len(ratings)):
#         rate.append(ratings[f].text.strip().split('\n'))
#     #print('This is take 1')
#     # [rate] = rate
#     # makeitastrings = ''.join(map(str, rate))
#     # rate = int(makeitastrings.replace('ratings', ''))
#     # for u, r, z in zip(names, links, rate):
#     #     temp_names = Salad(Name=u[0],
#     #                        num_ratings=u[1],
#     #                        url = r,
#     #                        avg_rating = z)
#     #     temp_names.save()
#     # for u, r, z in zip(names, links, rate):
#     #     trial_names = Trial(Name=u[0],
#     #                        num_ratings=u[1],
#     #                        url = r,
#     #                        avg_rating = z)
#     #     trial_names.save()
#
#     # # # #Filter to Urls with at least one rating... it works, #1566 urls to scrape.. lol
#     urlz = Salad.objects.filter(url__contains='h').exclude(avg_rating__isnull=True)[0:2].values_list('url', flat=True)
#     # #
#     # # # first_url = Salad.objects.filter(
#     # # #     url__iexact='https://www.ratemyprofessors.com/ShowRatings.jsp?tid=825559&showMyProfs=true').values_list('url',
#     # # #                                                                                                             flat=True)
#     # #
#     print(urlz)
#     print(len(urlz))
#     dates = []
#     comments = []
#     qualityz = []
#     ratingz = []
#     course_codez = []
#     lst = []
#
#     for link in urlz:
#         driver.get(link)
#         # for link in links:
#         webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#         amt_ratings = []
#         amt = driver.find_elements_by_css_selector(
#             '#root > div > div > div.PageWrapper__StyledPageWrapper-sc-3p8f0h-0.hswDmO > div.TeacherRatingsPage__TeacherBlock-a57owa-1.hkWQzD > div.TeacherInfo__StyledTeacher-ti1fio-1.kFNvIp > div:nth-child(1) > div.RatingValue__NumRatings-qw8sqy-0.jMkisx > div > a')
#         for p in range(len(amt)):
#             amt_ratings.append(amt[p].text.strip().split('\n'))
#         [amt_ratings] = amt_ratings
#         makeitastring = ''.join(map(str, amt_ratings))
#         final = int(makeitastring.replace('ratings', ''))
#         loops = math.floor((final - 20) / 10)
#         print(loops)
#         if loops >= 1:
#             i = 1
#             webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
#             sleep(1)
#             button = driver.find_elements_by_class_name("PaginationButton__StyledPaginationButton-txi1dr-1")
#             while i < loops:
#                 button[0].click()
#
#                 sleep(2)
#                 i = i + 1
#         else:
#             pass
#
#         date = driver.find_elements_by_class_name(
#             "TimeStamp__StyledTimeStamp-sc-9q2r30-0.bXQmMr.RatingHeader__RatingTimeStamp-sc-1dlkqw1-3.BlaCV")
#         comment = driver.find_elements_by_class_name("Comments__StyledComments-dzzyvm-0")
#         quality = driver.find_elements_by_xpath('//*[@id="ratingsList"]/li/div/div/div[2]/div[1]/div[2]')
#         difficulty = driver.find_elements_by_class_name("RatingValues__RatingValue-sc-6dc747-3.jILzuI")
#         course_code = driver.find_elements_by_class_name("RatingHeader__StyledClass-sc-1dlkqw1-2.gxDIt")
#         cluster = driver.find_elements_by_class_name("Rating__RatingBody-sc-1rhvpxz-0.dGrvXb")
#
#         for i in range(len(date)):
#             dates.append(date[i].text.strip())
#         for r in range(1, len(comment)):
#             comments.append(comment[r].text.strip())
#         for f in range(len(quality)):
#             qualityz.append(quality[f].text.strip())
#         for q in range(len(difficulty)):
#             ratingz.append(difficulty[q].text.strip())
#         for w in range(len(course_code)):
#             course_codez.append(course_code[w].text.strip())
#         for x in cluster:
#             try:
#                 child = x.find_element_by_class_name("RatingTags__StyledTags-sc-1boeqx2-0")
#                 lst.append(child.text.replace('\n', ', '))
#
#             except:
#                 lst.append('NA, NA, NA')
#
#     dates = list(filter(None, dates))  # REMOVING EMPTY STRINGS
#     course_codez = list(filter(None, course_codez))  # REMOVING EMPTY STRINGS
#     master_two = [(time, qual, rat, code, ments, *tagie.split(", ")) for time, qual, rat, code, ments, tagie in
#                   zip(dates, qualityz, ratingz, course_codez, comments, lst)]
#     master_two = [list(ele) for ele in master_two]
#     for el in master_two:
#         if len(el) == 6:
#             el = el.extend(['NA', 'NA'])
#         elif len(el) == 7:
#             el = el.append('NA')
#         else:
#             pass
#     print('now adding to dbs')
#     for u, r, z in zip(names, links, rate):
#         trial_names = Trial(Name=u[0],
#                             num_ratings=u[1],
#                             url=r,
#                             avg_rating=z)
#         trial_names.save()
#     for y in master_two:
#         review = StudentReviews(
#             date=y[0],
#             quality=y[1],
#             difficulty=y[2],
#             course_code=y[3],
#             comment=y[4],
#             tag1=y[5],
#             tag2=y[6],
#             tag3=y[7],
#             professor= trial_names)
#         review.save()
# #this puts the correct amount of comments into DB, and 20 professors orginal scrape..
# ##However, foreign key is only the LAST instance in the Trial Table.
#     ##dont make no sense
#
#     return None
#
#     # return render(request=request,
#     #               template_name='default.html',
#     #               context={})
#
#
# sitez = "https://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=College+of+Charleston&schoolID=254&queryoption=TEACHER"
# scrape(sitez)
