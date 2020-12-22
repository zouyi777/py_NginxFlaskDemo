from flask import Flask,request

from predict_code import seq2seq_predict

app = Flask(__name__)


# 客户端用form表单形式POST提交
@app.route("/venala2ancnt", methods=["POST"])
def hello_post_form():
    seedwords = request.form.get("seedwords")
    pre_words = seq2seq_predict.predict_ancient(seedwords)
    print(pre_words)
    return pre_words

if __name__ == '__main__':
    app.run(host='10.5.7.232',port=5003)