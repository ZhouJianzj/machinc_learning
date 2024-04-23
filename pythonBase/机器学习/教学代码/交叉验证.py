from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# 加载数据集
iris = load_iris()
X, y = iris.data, iris.target

# 初始化模型
model = LogisticRegression()

# 进行5折交叉验证
scores = cross_val_score(model, X, y, cv=5)

# 输出交叉验证得分
print("Cross-validated scores:", scores)

# 输出平均得分
print("Average accuracy:", scores.mean())