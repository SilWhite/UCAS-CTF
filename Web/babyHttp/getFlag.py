# coding:utf8
import requests
import base64

# reference: https://github.com/Crazy-13754/UCAS_CTF_WriteUp/blob/master/Web/BabyHttp.md


url = "http://124.16.75.117:51007"  # 目标URL
s = requests.Session()  # 获取 Session
response = s.get(url)  # 打开链接
head = response.headers  # 获取响应头
print(head)
# flag = base64.b64decode(head['Password']).split(':')[1] # 获取相应头中的Flag
flag = base64.b64decode(head["Password"]).decode("utf-8")
print(flag)
extracted_flag = flag[5:-1]  # 取中括号中的内容
print(extracted_flag)
postData = {"password": extracted_flag}  # 构造 Post 请求体
result = s.post(url=url, data=postData)  # 利用 Post 方式发送请求
# (注意要在同一个 Session 中 , 有的时候还需要设置 Cookies , 但是此题不需要)
print(result.text)  # 打印响应内容
