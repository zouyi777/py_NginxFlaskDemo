from net_model import net_model
from utils import pre_data_utils
import numpy as np
from py_common_dict import gen_com_dict

INUPT_LENGTH =16
OUTPUT_LENGTH = 17

# 获取字典
vocab_size,dict,dict_reverse = gen_com_dict.gen_dict1()

def sample(preds, temperature=1.0):
    '''
    当temperature=1.0时，模型输出正常
    当temperature小于1时时，模型输出比较保守,选择概率较大的值输出
    当temperature大于1时，模型输出比较open,选择概率较小的输出
    在训练的过程中可以看到temperature不同，结果也不同
    '''
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    # print('preds：',preds)
    probas = np.random.multinomial(1, preds, 1) # 甩骰子
    # print('probas：', probas)
    return np.argmax(probas)
# 预测
def predict_chinese(source,encoder_inference, decoder_inference, n_steps, features):
    #先通过推理encoder获得预测输入序列的隐状态
    _, enc_state_h, enc_state_c = encoder_inference.predict(source)
    state = [enc_state_h, enc_state_c]
    #第一个字符'\t',为起始标志
    predict_seq = np.array([[dict['\t']]])
    output = ''
    #开始对encoder获得的隐状态进行推理
    #每次循环用上次预测的字符作为输入来预测下一次的字符，直到预测出了终止符
    for i in range(n_steps):#n_steps为句子最大长度
        #给decoder输入上一个时刻的h,c隐状态，以及上一次的预测字符predict_seq
        yhat,h,c = decoder_inference.predict([predict_seq]+state)
        #注意，这里的yhat为Dense之后输出的结果，因此与h不同
        char_index = np.argmax(yhat[0,-1,:])
        # char_index = sample(yhat[0,-1,:])
        char = dict_reverse[char_index + 1]
        output += char
        state = [h,c]#本次状态做为下一次的初始状态继续传递
        predict_seq = np.array([[char_index + 1]])
        if char == '\n':#预测到了终止符则停下来
            break
    return output

def predict_ancient(texts):
    model_train = net_model.Seq2Seq(vocab_size)
    model_train.load_weights("model/ancient_poetry_weights.h5")
    encoder_infer = net_model.encoder_infer(model_train)
    decoder_infer = net_model.decoder_infer(model_train)
    encoder_input = pre_data_utils.gen_sequence_without_onehot([texts], dict, INUPT_LENGTH)
    out = predict_chinese(encoder_input, encoder_infer, decoder_infer, OUTPUT_LENGTH, vocab_size)
    return out;

if __name__ == '__main__':
    texts = "酿酒"
    out = predict_ancient(texts)
    print(texts)
    print(out)

