import jieba
from sklearn import feature_extraction

"""
特征提取
数据和特征决定了机器学习的上限，而模型和算法只是逼近这个上限而已。

"""


def demo_feature_extraction():
    """
    1、字典特征值提取
    :return:
    """
    # 原始数据
    data = [
        {"city": "南京", 'value': 100},
        {"city": "扬州", 'value': 70},
        {"city": "北京", 'value': 10},
    ]
    # sparse=True 表示开启稀疏矩阵
    # 实例化一个特征转化器
    dictVectorizer = feature_extraction.DictVectorizer(sparse=False)
    # 调用fit_transform()
    data_new = dictVectorizer.fit_transform(data)
    print(f'特征名字：{dictVectorizer.get_feature_names_out()}')
    return data_new


def demo_text_feature_extraction():
    """
    2、文本特征值提取
    :return:
    """
    # 原始数据
    data = [
        "i like java and python !",
        "i dislike java and like vue and python too ，"
    ]
    #   创建文本特征提取对象
    countVectorizer = feature_extraction.text.CountVectorizer()
    #  提取特征值
    new_data = countVectorizer.fit_transform(data)
    print(f'特征值name：{countVectorizer.get_feature_names_out()}', new_data, sep='\n')
    return new_data


def cut_word(text):
    """
    分词
    :param text:
    :return:
    """
    return " ".join(list(jieba.cut(text)))


def demo_text_chinese_feature_extraction():
    """
    2.1、文本特征值提取
    为了解决中文不分词的问题我们使用jieba辅助完成特征提取  我定义了cut_word()方法
    :return:
    """
    # 原始数据
    data = [
        "我爱java但是java也爱我！",
        "我爱python但是python不爱我"
    ]
    # 分词操作
    cut_data = []
    for item in data:
        cut_data.append(cut_word(item))
    print(cut_data)
    #   创建文本特征提取对象
    countVectorizer = feature_extraction.text.CountVectorizer()
    #  提取特征值
    new_data = countVectorizer.fit_transform(cut_data)
    print(f'特征值name：{countVectorizer.get_feature_names_out()}', new_data, sep='\n')
    return new_data


def demo_tiidf():
    """
    TF-IDF的主要思想是：如果某个词或短语在一篇文章中出现的概率高，并且在其他文章中很少出现，
        则认为此词或者短语具有很好的类别区分能力，适合用来分类。
    TF-IDF作用：用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
    :return:
    """
    # 原始数据
    data = [
        "我爱java但是java也爱我！",
        "我爱python但是python不爱我"
    ]
    # 分词操作
    cut_data = []
    for item in data:
        cut_data.append(cut_word(item))
    # tiidf分词器
    tfidfVectorizer = feature_extraction.text.TfidfVectorizer()
    new_data = tfidfVectorizer.fit_transform(cut_data)
    print(f'特征值name：{tfidfVectorizer.get_feature_names_out()}', new_data, sep='\n')
    return new_data


# 字典特征提取
# new_data = demo_feature_extraction()
'''
# sparse=True 表示开启稀疏矩阵
  (0, 1)	1.0
  (0, 3)	100.0
  (1, 2)	1.0
  (1, 3)	70.0
  (2, 0)	1.0
  (2, 3)	10.0
  
  # sparse=False 表示关闭稀疏矩阵
 [
     [  0.   1.   0. 100.]
     [  0.   0.   1.  70.]
     [  1.   0.   0.  10.]
 ]
'''

# print(new_data)


# 2、文本特征提取
#     new_data_text = demo_text_feature_extraction()
"""
    原始数据：
    [
        "i like java and python !",
        "i dislike java and like vue and python too ，"
    ]
    特征：
    ['and' 'dislike' 'java' 'like' 'python' 'too' 'vue']
    
    矩阵数据：
    [
    [1 0 1 1 1 0 0]
    [2 1 1 1 1 1 1]
    ]
"""
# print('矩阵', new_data_text.toarray())

#  中文文本特征提取
"""
原始数据：
    data = [
        "我爱java但是java也爱我！",
        "我爱python但是python不爱我"
    ] 
    
特征值name：
    ['我爱java但是java也爱我' '我爱python但是python不爱我']
    
稀疏矩阵：
      (0, 0)	1
      (1, 1)	1
      
      
没有分词的效果,改造之后的====================

原始数据：
    [
        '我 爱 java 但是 java 也 爱 我 ！',
         '我 爱 python 但是 python 不爱 我'
    ]

特征值name：
    ['java' 'python' '不爱' '但是']
    
稀疏矩阵：
  (0, 0)	2
  (0, 3)	1
  (1, 3)	1
  (1, 1)	2
  (1, 2)	1
  
矩阵：  
    [
        [2 0 0 1]
        [0 2 1 1]
    ]

"""
# new_data = demo_text_chinese_feature_extraction()
# print(new_data.toarray())
# print(cut_word("我爱java但是java也爱我"))



"""
tiidf 
特征值name：
    ['java' 'python' '不爱' '但是']

  (0, 3)	0.33517574332792605
  (0, 0)	0.9421556246632359
  (1, 2)	0.42615959880289433
  (1, 1)	0.8523191976057887
  (1, 3)	0.3032160644503863

    [
        [0.94215562 0.         0.         0.33517574]
        [0.         0.8523192  0.4261596  0.30321606]
    ]
"""
print(demo_tiidf().toarray())