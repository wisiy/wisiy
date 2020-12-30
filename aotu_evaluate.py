import time
from selenium.webdriver.remote.errorhandler import ElementClickInterceptedException
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import pymysql
from selenium.webdriver.chrome.options import Options

#
# 打开数据库连接
conn = pymysql.connect(host="10.18.0.78", port=8883, user='root', passwd='ZYzwfw@123', db='sp_98_ziyangshi')
cursor = conn.cursor()
cursor.execute("SELECT * FROM scexevaluateeventcallback WHERE IFEVALUATE=0 AND UID=4055271273457197056;")
# while 1:
#     res = cursor.fetchone()
#     if res is None:
#         break
#     print(res)
res = cursor.fetchmany(3)
listR = []
listID = []
url = ''
uid = ''
for r in res:
    url = r[7]
    uid = r[6]
    listR.append(url)
    listID.append(uid)

print(listR[:3], '...' + '\n共有：', +len(listR), '条')
# print(listR[0][7])

count = len(listR)
for F in listR:
    # personListCount = len(res)
    chrome_options = Options()
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    for i in enumerate(listR, start=1):
        # for j in enumerate(listID, start=1):
        #     uid = j[1]
        #     print(uid)
        url = i[1]
        print(url, i)
        # driver.get(url)
        driver.get(url)
        time.sleep(2)
        button = driver.find_element_by_css_selector(
            '#app > div > section.ei-content > div.ei-content-right > section.right-second > div.rigth-submit > button')
        button.click()
        time.sleep(2)
        submit = driver.find_element_by_css_selector('#app > div > section.ei-box > div.box > div.box-content > div.box-botton-group > p.pactive')
        submit.click()
        backResult = driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div')[0].text
        print(backResult)
        # if backResult == '请勿重复提交' or '提交成功':
        #     cursor.execute("UPDATE scexevaluateeventcallback SET IFEVALUATE=1 WHERE UID='%s';" % uid)
        # else:
        #     print('有其他问题，请检查')
        # databaseResult = cursor.execute("SELECT * FROM scexevaluateeventcallback WHERE URL='%s';" % url)
        # print(databaseResult)
        time.sleep(2)
        driver.quit()
cursor.close()
conn.commit()
conn.close()
# import requests
# import json
#
# url = 'http://hcp.sczwfw.gov.cn/appEval/index.html#/evalInstrument?affairCode=512000-20201223-003381'
# req = requests.get(url, json={})
# pos = requests.post(url, json={})
# # res = json.loads((req.text))
# # page = req.content
# # page = page.decode('utf-8')
# # print(req,page)
# # print(pos.text)
# print(req.text)
