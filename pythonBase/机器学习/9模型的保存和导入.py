"""
训练好的模型将他保存起来，下次使用的时候直接load
这里K 邻近为例
"""
from sklearn import datasets, model_selection, preprocessing, neighbors
import joblib

# 1.加载数据集
iris = datasets.load_iris()

# 2.数据集划分
train_feature, test_feature, train_target, test_target = model_selection.train_test_split(iris.data,
                                                                                          iris.target,
                                                                                          random_state=6)
# 3.数据集处理 标准化
fit_train_feature = preprocessing.StandardScaler().fit_transform(train_feature)
fit_test_feature = preprocessing.StandardScaler().fit_transform(test_feature)

# 4.模型选择
#  k邻近算法评估器  n_neighbors:取最近的几个
# estimator = neighbors.KNeighborsClassifier(n_neighbors=2)
# 计算数据 标准化之后的特征值和 为处理的目标值
# 7.导入模型使用
estimator = joblib.load("my_KNeighbor.pkl")
# estimator.fit(fit_train_feature, train_target)


# 5.模型评估
# 可以直接使用score()方法测算训练的数据和测试数据的匹配度，传入标准化之后的测试特征值和没有处理的测试目标值
score = estimator.score(fit_test_feature, test_target)
# 0.8947368421052632
print(score)
# 6.模型保存
# joblib.dump(estimator, "my_KNeighbor.pkl")
