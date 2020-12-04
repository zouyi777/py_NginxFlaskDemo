import requests
import base64

#将图片数据转成base64格式
with open('images_native/test6.jpg', 'rb') as f:
    img = base64.b64encode(f.read()).decode()
image = []
image.append(img)
res = {"image":image}
#访问服务
response = requests.post("http://120.24.147.111:80/catdog",data=res)
print('response.text:',response.text)
