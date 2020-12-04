from flask import request, Flask
import base64
import cv2
import numpy as np
import tensorflow as tf
import termcolor
app = Flask(__name__)
class_names = ['cat', 'dog']

@app.route("/catdog", methods=['POST','GET'])
def get_frame():
    #解析图片数据
    img = base64.b64decode(str(request.form['image']))
    image_data = np.fromstring(img, np.uint8)

    img_np = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    test_img = img_np / 255.0
    # 加载件训练好的保存下来的模型
    model = tf.keras.models.load_model('models/catdog_model.h5')
    # 预测
    test_images = np.array([test_img])  # 将图片装进一个数组里面
    predictions = model.predict(test_images)
    argmax = np.argmax(predictions[0])
    # 保存一下图片
    cv2.imwrite('images_server/01.jpg', img_np)
    return class_names[argmax]
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5005)  # 127.0.0.1 #指的是本地ip
