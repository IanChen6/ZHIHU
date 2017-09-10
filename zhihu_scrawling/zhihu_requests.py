# -*- coding: utf-8 -*-
import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib

import re

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
header = {
    "HOST": "www.zhihu.com",
    "Refer": "https://www.zhihu.com/",
    "User-Agent": agent

}

session = requests.session()
session.cookies = cookielib.LWPCookieJar(filename="cookies.txt")#以这种格式保存cookie
try:
    session.cookies.load(ignore_discard=True)
except:
    print("cookie unresolved")

def get_index():#
    url = "https://www.zhihu.com/"
    response = session.get(url=url, headers=header)
    with open("index_page.html",'w') as f:
        f.write(response.text)
    print('ok')

def get_captcha():
    import time
    t=str(int(time.time()*1000))#https://www.zhihu.com/captcha.gif?r=1505053437845&type=login&，获取图片验证码的r参数
    captcha_url="https://www.zhihu.com/captcha.gif?r={0}&type=login&".format(t)
    t=session.get(captcha_url,headers=header)
    #保存该图片文件
    with open("captcha.jpg","wb") as f:
        f.write(t.content)
        f.close()

    from PIL import Image
    try:
        im=Image.open("captcha.jpg")
        im.show()
        im.ckose()
    except:
        pass


def is_login():
    #通过个人中心状态码来判断是否登录状态
    inbox_url="https://www.zhihu.com/settings/profile"
    response=session.get(inbox_url,headers=header,allow_redirects=False)
    if response.status_code==200:
        print("已登录")
    else:
        print("未登录")
        return False
    pass

    captcha=input("impute captcha:\n")
    return captcha

def get_xsrf():
    url = "https://www.zhihu.com/"
    response = session.get(url=url, headers=header)  # 使用get获取时，
    # header为python2或python3，会导致出错,所以要传入headers
    # print(response.text)
    # text = '<input type="hidden" name="_xsrf" value="7e24c07ff5d9da1badf28710f5af2bea"/>'

    # match_obj = re.match('.*name="_xsrf" value="(.*?)".*', response.text, re.DOTALL)
    match_obj = re.findall('.*name="_xsrf" value="(.*?)".*', response.text)
    if match_obj:
        print(match_obj[1])
        return (match_obj[1])

    else:

        return ""
        # _xsrf=


def zhihu_login(account, password):
    # 知乎登录
    if re.match('^1\d{10}', account):
        print("login by phone number")
        post_url = "https://www.zhihu.com/login/phone_num"
        captcha=get_captcha()

        post_data = {
            "_xsrf": get_xsrf(),
            "password": password,
            "phone_num": account,
            "captcha":captcha
        }
    else:#判断用户名是否为邮箱
        if "@" in account:
            print("login by email")
            post_url = "https://www.zhihu.com/login/phone_num"
            post_data = {
                "_xsrf": get_xsrf(),
                "password": password,
                "phone_num": account
            }
    response_text = session.post(post_url, data=post_data, headers=header)
    session.cookies.save()






#
zhihu_login("18665351170", "welcome1993")
# # get_index()
# is_login()
# get_captcha()