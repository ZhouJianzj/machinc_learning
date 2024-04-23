from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
# 加载数据集
iris = load_iris()
X, y = iris.data, iris.target

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
