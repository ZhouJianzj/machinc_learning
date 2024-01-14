# 特征值的预处理：无量纲化
import pandas
from sklearn.preprocessing import MinMaxScaler,StandardScaler


def demo_minmaxscaler():
    """
    归一化：
    通过一些转换函数将特征数据转换成更加适合算法模型的特征数据过程
    特征的单位或者大小相差较大，或者某特征的方差相比其他的特征要大出几个数量级，容易影响（支配）目标结果，
    使得一些算法无法学习到其它的特征
    :return:
    """
    # panda读取文件数据
    data = pandas.read_csv('dating.txt')
    # 只保留前三列，全部行
    print(data.iloc[:, :3])
    # 通过对原始数据进行变换把数据映射到(默认为[0,1])之间，这个feature_range可以指定
    minMaxScaler = MinMaxScaler(feature_range=(0, 1))
    # 只保留前三列，全部行 效果雷同
    print(data[["milage", 'Liters', 'Consumtime']])
    print("*" * 180)
    data_new = minMaxScaler.fit_transform(data.iloc[:, :3])
    return data_new


def demo_standardScaler():
    """
    标准化：通过对原始数据进行变换把数据变换到均值为0,标准差为1范围内
    :return:
    """
    data = pandas.read_csv('dating.txt')
    standartScaler = StandardScaler()
    data_new = standartScaler.fit_transform(data.iloc[:,:3])
    print("*" * 180)
    print(f'标准化之后的值：{data_new}')
    print(f'每一列的平均值：{standartScaler.mean_}')
    print(f'每一列的方差：{standartScaler.var_}')

    return None


if __name__ == '__main__':

    # data_new = demo_minmaxscaler()
    # print("归一化之后的数据：",data_new)

    print(demo_standardScaler())
