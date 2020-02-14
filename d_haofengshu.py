from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By #按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys #键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait #等待页面加载某些元素
import time
import json
browser=webdriver.Chrome("../chromedriver.exe")
try:
    browser.get('https://hfs.yunxiao.com')
    # time.sleep(20)
    # cookie = browser.get_cookies()
    # print(cookie)
    # jsonCookies = json.dumps(cookie)
    # with open('qqhomepage.json', 'w') as f:
    #     f.write(jsonCookies)

    # str = ''
    # with open('qqhomepage.json', 'r', encoding='utf-8') as f:
    #     listCookies = json.loads(f.read())
    # cookie = [item["name"] + "=" + item["value"] for item in listCookies]
    # cookiestr = '; '.join(item for item in cookie)
    # print(cookie)
    # browser.add_cookie({"domain": ".hfs.yunxiao.com", "name": "Hm_lpvt_61aa36706e10114b2dc66352a3d6517e","value": "1580967466"})
    # browser.add_cookie(
    #     {"domain": ".hfs.yunxiao.com", "name": "Hm_lvt_61aa36706e10114b2dc66352a3d6517e", "value": "1580967466"})
    # browser.add_cookie(
    #     {"domain": ".yunxiao.com", "name": "hfs-session-id", "value": "eyJhbGciOiJIUzI1NiJ9.NWUzYTU1MzMwMDAwMDJjZTJiMmNjYjA1LTE1ODA4ODEyMDM4OTY.kDiRVVnF9Ijg9NRb557zkTRdC21JEHFB01uijBgZxq8"})
    #{"domain": ".hfs.yunxiao.com", "expiry": 1612503466, "httpOnly": "false", "name": "Hm_lvt_61aa36706e10114b2dc66352a3d6517e", "path": "/", "secure": "false", "value": "1580967466"}
    #获取输入框元素
    # wait = WebDriverWait(browser, 50)

    time.sleep(2)
    student_click = browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div[1]/div/ul/li[2]/div")
    student_click.click()
    time.sleep(2)
    # /html/body/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input
    input_login_username = browser.find_element_by_tag_name("input")
    print(input_login_username.get_attribute("type"))
    input_login_password = browser.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/input")
    print(input_login_password.get_attribute("type"))

    # 输入账号：1529783965
    input_login_username.send_keys("15297833965")
    # 输入密码: 15297833965r
    input_login_password.send_keys("xxxxxxxx")
    # 按住回车登陆
    input_login_password.send_keys(Keys.ENTER)
    # 5s 等待登陆
    time.sleep(2)
    # 关闭广告：
    ad_click = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/div[1]/span")
    ad_click.click()
    time.sleep(2)
    #  点击期末考试
    final_exam = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/a[2]")
    final_exam.click()
    time.sleep(2)
    print("line 60")
    # find all subject
    # 英语 path "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/button[1]"
    # 语文 path  "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/button[2]"
    # 物理 path "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/button[3]"
    sub_path = "/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[1]/div[1]/div/button["
    for i in range(1,9):
        sub_click = browser.find_element_by_xpath(sub_path+str(i)+"]")
        sub_click.click()
        time.sleep(5)
        print("line 70")
        # /html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[13]/div[1]/button[2]
        # next_page_btn = browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[4]/div[1]/button[2]")
        # next_page_btn =  browser.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[1]/div[3]/div[13]/div[1]/button[2]")
        # next_page_inputs = browser.find_elements_by_name("input")
        # next_page_input = ''
        next_page_input = browser.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div/div[1]/div[3]/div[13]/div[1]/span/div/input")
        # for i_ in range(1,len(next_page_inputs)):
        #     print(1)
        #     if(next_page_inputs[i_].get_attribute("type") == "number" ):
        #         next_page_input = next_page_inputs[i_]
        #         print(2)
        # if (next_page_input == ''):
        #     continue
        print(next_page_input.get_attribute("class"))
        count = 1
        str_image = ""
        print("line 86")
        while(count<4):
            try:
                # next_page_input.send_keys(count)
                # next_page_input.send_keys(Keys.ENTER)
                next_page_input.send_keys(count)
                next_page_input.send_keys(Keys.ENTER)
                next_page_input.send_keys(Keys.F5)
                print("10后开始遍历：\n")
                time.sleep(10)

                input_tag = browser.find_elements_by_tag_name("img")
                list_url = []
                for j in range (1,len(input_tag)-1):
                    str_image = input_tag[j].get_attribute("src")+"\n"
                    list_url.append(input_tag[j].get_attribute("src")+"\n")
                    print(1)
                    if str_image == "https://hfs.yunxiao.com/static/img/icon-face60.22a8685.png\n" :
                        print(2)
                        continue
                    else:
                        str_image = input_tag[j].get_attribute("src")

                    with open(str(i)+".txt", "a") as f:
                        f.write(list_url[j-1])
                # next_page_btn.click()



                time.sleep(10)
            except:
                break
            count = count + 1

finally:
    browser.close()