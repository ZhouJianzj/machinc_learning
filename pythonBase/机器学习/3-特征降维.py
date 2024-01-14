# 在特征预处理和提取过后会有多个特征，为了更好的训练模型我们需要将多个特征进行提取，提取关键的互相没有相关性的特折
import pandas
from scipy.stats import pearsonr
from sklearn.feature_selection import VarianceThreshold
import matplotlib.pyplot as plt


def feature_dimensionality_variance_selection():
    """
    特性选择----过滤式----方差选择法
    :return:
    """
    data = pandas.read_csv('factor_returns.csv')
    # 可以设定需要被过滤掉的特征方差阈值
    variance_threshold = VarianceThreshold(threshold=1)
    # 9列 也就是9个特征
    print(data.keys(), '\n', data.iloc[:10, 1:-2])
    # 我们只要我们需要的数据列-----取1到倒数第3列
    data_new = variance_threshold.fit_transform(data.iloc[:10, 1:-2])
    # 减少了一个 8列了 8个特征了
    print("删除低方差的结果:", data_new, '\n', data_new.shape)
    print("*" * 180)
    # print(variance_threshold.inverse_transform(data_new))


def feature_dimensionality_pearsonr():
    """
    皮尔逊相关系数；反应指标（特征值）之间的关系程度
    |r| 越接近 0表示特征值之间越无相关性
    :return:
    """
    data = pandas.read_csv('factor_returns.csv')
    factor = ['pe_ratio', 'pb_ratio', 'market_cap',
              'return_on_asset_net_profit', 'du_return_on_equity', 'ev',
              'earnings_per_share', 'revenue', 'total_expense']
    # 需要将上面的数组中每一个元素相互比较
    for i in range(len(factor)):
        for j in range(len(factor) - 1 - i):
            print(f'{factor[i]}------{factor[j + 1 + i]}==========皮尔逊相关系数=======>'
                  f' {pearsonr(data[factor[i]], data[factor[j + 1 + i]])}')

    plt.figure(figsize=(20, 8), dpi=100)
    plt.scatter(data['revenue'], data['total_expense'])
    plt.show()
    # pearsonr()


from sklearn.decomposition import PCA


def feature_PCA():
    """
    特征降维-----主成分分析
    :return:
    """
    data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    # n_components: 小数：表示保留百分之多少的信息  整数：减少到多少特征
    # 原先4个特性(4维)，现在需要降到三个（3维）
    pca = PCA(n_components=3)
    data_new = pca.fit_transform(data)
    print(f'主成分分析：{data_new}')


if __name__ == '__main__':
    # feature_dimensionality_variance_selection()

    # feature_dimensionality_pearsonr()

    feature_PCA()
