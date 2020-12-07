import os
data_path = "py_common_dict/data/common_word_list.txt"
realpath = os.path.realpath(data_path)
# 读取数据
def read_data():
    content = "\t\n"
    with open(realpath, "r", encoding='utf-8', ) as f:
        for line in f:
            word = line.replace('\n', '')  # 去掉换行符
            word = word.replace(' ', '') # 去掉空格
            content = content + word
    return content

# 生成词典,下标从0开始
def gen_dict():
    texts = read_data()
    characters = sorted(list(set(texts)))
    char_len = len(characters)
    dict = {char: index for index, char in enumerate(characters)}
    dict_reverse = {index: char for index, char in enumerate(characters)}
    return char_len,dict,dict_reverse
# 生成词典，下标从1开始
def gen_dict1():
    texts = read_data()
    characters = sorted(list(set(texts)))
    char_len = len(characters)
    dict = {char: index+1 for index, char in enumerate(characters)}
    dict_reverse = {index+1: char for index, char in enumerate(characters)}
    return char_len,dict,dict_reverse

if __name__ == '__main__':
    print(len(read_data()))
    char_len,dict,dict_reverse = gen_dict()
    print("char_len:",char_len)
    print("dict:",dict)
    # print("dict_reverse:",dict_reverse)