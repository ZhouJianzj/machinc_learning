from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


def demo():
    # 获取新闻的数据，20个类别
    news = fetch_20newsgroups(subset='all')

    # 进行数据集分割
    x_train, x_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.3)

    # 对于文本数据，进行特征抽取
    tf = TfidfVectorizer()

    x_train = tf.fit_transform(x_train)

    # 不能调用fit_transform
    x_test = tf.transform(x_test)

    # estimator估计器流程
    mlb = MultinomialNB(alpha=1.0)

    mlb.fit(x_train, y_train)

    # 进行预测
    y_predict = mlb.predict(x_test)

    print("预测准确率为：", mlb.score(x_test, y_test))


def demo1():
    # 数据加载
    data = fetch_20newsgroups(subset="all")
    x_train, x_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.3)

    # 数据处理
    tfidf = TfidfVectorizer()
    x_train_tf = tfidf.fit_transform(x_train)
    x_test_tf = tfidf.transform(x_test)

    # 贝叶斯
    nb = MultinomialNB()
    nb.fit(x_train_tf, y_train)
    print(nb.score(x_test_tf, y_test))


if __name__ == '__main__':
    demo()
    demo1()
