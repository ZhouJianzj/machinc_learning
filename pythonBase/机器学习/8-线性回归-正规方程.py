"""
线性回归优化之正规方程

"""
from sklearn import datasets, preprocessing, model_selection

# 加载波士顿房价数据
boston = datasets.fetch_openml(name="boston", version='2')
# 数据拆分
boston
# model_selection.train_test_split(boston.value,boston.target)
# 特征工程-数据标准化

# 模型训练


# 模型评估
