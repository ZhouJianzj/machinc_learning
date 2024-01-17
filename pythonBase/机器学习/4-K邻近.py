"""
使用 鹰尾花数据集 iris
"""
import sklearn.model_selection
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


def demo_KNeighbor():
    """
    1、加载数据集
    2、数据集划分（训练集、测试集）
    3、特征提取处理（iris数据集就是）
    4、特征数据预处理（无量纲化）
    5、降维（iris数据集4个特征）
    6、模型选择
    :return:
    """
    # 加载数据集
    iris = datasets.load_iris()
    # print(f'特征数据---{iris.data}\n 目标值数据------{iris.target}')
    # 数据集划分
    train_feature, test_feature, train_target, test_target = sklearn.model_selection.train_test_split(iris.data,
                                                                                                      iris.target,
                                                                                                      random_state=6)
    # 标准化
    fit_train_feature = sklearn.preprocessing.StandardScaler().fit_transform(train_feature)
    fit_test_feature = sklearn.preprocessing.StandardScaler().fit_transform(test_feature)

    #  k邻近算法评估器  n_neighbors:取最近的几个
    estimator = KNeighborsClassifier(n_neighbors=2)
    # 计算数据 标准化之后的特征值和 为处理的目标值
    estimator.fit(fit_train_feature, train_target)

    # 可以直接使用score()方法测算训练的数据和测试数据的匹配度，传入标准化之后的测试特征值和没有处理的测试目标值
    score = estimator.score(fit_test_feature, test_target)
    print(score)

    #使用predict()预测测试特征数据的预测目标值,输入标准化之后的测试特征值，得到预测的测目标值，然后和真实的测试目标值对比
    predict_test_target = estimator.predict(fit_test_feature)
    print('KNeighbors算法预测的测试目标数据集为----', predict_test_target, test_target == predict_test_target)

if __name__ == '__main__':
    demo_KNeighbor()
