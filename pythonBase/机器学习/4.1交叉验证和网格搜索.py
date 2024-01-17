import sklearn.model_selection
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


def demo_crossValidate_GridSearch():
    """
    交叉验证和网格搜索
    交叉验证：将数据集划分为训练集和测试集两大类不变，边的是将k折化，
    |train|train|train|test|
    |1    |2    |3    |4   |
    |4    |2    |3    |1   |
    |4    |1    |3    |2   |
    |4    |1    |2    |3   |
    :return:
    """
    # 加载数据集
    iris = datasets.load_iris()
    # 拆分
    train_feature, test_feature, train_target, test_target = sklearn.model_selection.train_test_split(iris.data,
                                                                                                      iris.target)
    # 标准化
    standard_train_feature = sklearn.preprocessing.StandardScaler().fit_transform(train_feature)
    standard_test_feature = sklearn.preprocessing.StandardScaler().fit_transform(test_feature)
    # k邻近分类器
    estimator = KNeighborsClassifier()
    # 交叉验证和网格搜索器
    gridSearchCV = sklearn.model_selection.GridSearchCV(estimator, param_grid={'n_neighbors': [1, 2, 3, 4, 5, 6, 7, 8]},
                                                        cv=5)
    # 计算
    gridSearchCV.fit(standard_train_feature, train_target)

    predict_test_target = gridSearchCV.predict(standard_test_feature)
    print(predict_test_target == test_target)
    # 估分
    score = gridSearchCV.score(standard_test_feature, test_target)
    print(f'估分：{score}')
    print("最佳的分", gridSearchCV.best_score_)
    print("最佳k值", gridSearchCV.best_params_)
    print("最佳评估器", gridSearchCV.best_estimator_)
    print(gridSearchCV.cv_results_)


if __name__ == '__main__':
    demo_crossValidate_GridSearch()
