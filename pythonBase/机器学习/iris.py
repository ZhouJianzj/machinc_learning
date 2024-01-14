from sklearn import datasets, model_selection

'''
加载数据
:return 加载iris数据集
'''


def load_data():
    return datasets.load_iris()


if __name__ == '__main__':
    print(type(load_data()))
    iris = load_data()
    # print(iris.values())
    # dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
    # print(iris.keys())
    # print('目标值name：', iris.get('target_names'))
    # print('目标值value：', iris.get('target'))
    # print('特征值name：', iris.get('feature_names'))
    # print('特征值value：', iris.get('data'))
    # print('数据集描述：', iris.get('DESCR'))

    #     拿到数据集了将其拆分为训练集和测试集,入参 特征值value、目标值value、test_size大小等
    train_data, test_data, train_target, test_target = model_selection.train_test_split(iris.data, iris.target,
                                                                                        test_size=0.2)
    print(f"训练特征值value：{train_data.shape}", train_data)
    print(f'训练目标值value{train_target.shape}:{train_target}')
    print(f'测试特征值value{test_data.shape}:{test_data}')
    print(f'测试目标值value{test_target.shape}:{test_target}')


