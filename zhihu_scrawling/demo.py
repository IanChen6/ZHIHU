import re
import requests

agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
header = {
    "HOST": "www.zhihu.com",
    "Referer": "https://www.zhihu.com/",
    "User-Agent": agent

}

url = "https://www.zhihu.com/"
response = requests.get(url=url, headers=header)  # 使用get获取时，
# header为python2或python3，会导致出错,所以要传入headers
# print(response.text)
text='<input type="hidden" name="_xsrf" value="7e24c07ff5d9da1badf28710f5af2bea"/>'

# match_obj=re.match('.*name="_xsrf" value="(.*?)".*',response.text,re.DOTALL)
match_obj=re.findall('.*name="_xsrf" value="(.*?)".*',response.text)
if match_obj:
    print(match_obj[1])

# _xsrf=

#
# #!/usr/bin/env python
# # encoding: utf-8
# import requests
#
# session = requests.session()
# url = "https://www.zhihu.com/"
# agent = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
# resp = requests.get(url, headers=agent)
#
# print(resp.text)
