#!/usr/bin/env python3
# 计算文本距离的第八个版本
# 将整个文件视为单个行
#
# Original version by Ronald L. Rivest on February 14, 2007
# based on code by Ronald L. Rivest (see docdist[1-7].py).
# Revision by Winslow Walker on October 18, 2024
#
# Usage: 
#    docdist8-py3.py filename1 filename2
#
# 这是一个计算两个文本文件距离的程序
# 作为他们文本向量间角度（使用弧度制）
#
# 每个输入文件 次品向量如下方法计算
# (1) 读取文件
# (2) 转化为单词的列表
#     单词指的是连续序列的字母数字字符
#     非字母数字字符被当做空格处理
#     大小写不敏感
# (3) 统计每个单词的出现次数
# (4) 将 单词/词频 列表按照字母顺序排序
# 
# 两个向量之间的距离是他们的夹角
# 比如：x = (x1, x2, ..., xn) 是第一个文本向量 (xi = 单词i的频率)
#       y = (y1, y2, ..., yn) 是第二个文本向量
# 他们之间的夹角是：
#     d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# 其中：
#     inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
#     norm(x) = sqrt(inner_product(x,x))

import math
# math.acos(x) 返回X的反余弦值
# math.sqrt(x) 返回X的平方根
import string

import sys

##################################
# 第一步：读取文本文件
##################################
def read_file(filename) :
    """
    从文件名 filename 中读取文本，
    return: 一个包含文件中行的列表
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except IOError:
        print(f"读取文件：{filename}失败")
        sys.exit()


##################################
# 第二步：对每一行文本进行分割，得到单词
##################################


# 全局变量,使用 string 进行快速解析
# 将大写字母转化为小写字母，将逗号改为空格
translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                    " "*len(string.punctuation)+string.ascii_lowercase)
def get_words_from_line_list(text):
    """
    将文本解析为单词
    line: str
    return: [str] str中的每个字符都是字母或者数字
    """
    text = text.translate(translation_table)
    word_list = text.split()

    return word_list

#######################################
# 步骤3：统计单词频率
#######################################
def count_frequency(word_list):
    """返回单词和词频的列表
    word_list: 单词列表    
    return: [(word1,freq1),(word2,freq2),...]
    """
    D ={}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D

###################################################
# 步骤5：计算输入文件中的单词频率
###################################################
def word_frequencies_for_file(filename):
    """
    return: {word1: freq1, word2: freq2 ...}
    """
    line_list = read_file(filename)
    word_list = get_words_from_line_list(line_list)
    freq_mapping = count_frequency(word_list)
    # insertion_sort(freq_mapping)

    print(f"文件{filename}:")
    print(f"行数：{len(line_list)}")
    print(f"单词数量：{len(word_list)}")
    print(f"词频表长度：{len(freq_mapping)}")

    return freq_mapping
def inner_product(D1, D2):
    """ 
    计算向量内积

    例如：inner_product({"and": 3,"of": 2,"the": 5},
                           {"and": 4,"in": 1,"of": 1,"this": 2}) = 14.0
    """
    # 这里相较于3也有了些变化，直接使用字典进行内积计算，并没有进行排序
    # 但是由于改了两个地方，所以效率的提升具体哪个部分明显？
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key]*D2[key]
    return sum

def vector_angle(D1, D2):
    """
    计算两个向量之间的夹角
    return: 夹角，弧度制 
    """
    numerator = inner_product(D1, D2)
    denominator = math.sqrt(inner_product(D1, D1)*inner_product(D2, D2))
    return math.acos(numerator/denominator)
def main():
    if len(sys.argv) !=3:
        print("请使用：docdist8-py3.py filename_1 filename_2")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
        print(f"两个文档间的文本相似度为：{distance:.6f}(弧度单位)")

if __name__ == "__main__":
    # import profile
    # profile.run("main()")
    import cProfile
    cProfile.run("main()")
    # 如果该 cProfile 无法使用，请使用 profile