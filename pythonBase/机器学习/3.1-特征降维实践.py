# 使用pca对多个特征进行降维
import io
import os

import pandas


def feature_pca():
    file_dir = 'C:/Users/29983/Desktop/Python3天快速入门机器学项目资料\机器学xiday1资料/02-代码/instacart'
    os.chdir(file_dir)
    # ['aisles.csv', 'orders.csv', 'order_products__prior.csv', 'products.csv']
    aisles = pandas.read_csv('aisles.csv')
    orders = pandas.read_csv('orders.csv')
    order_products = pandas.read_csv('order_products__prior.csv')
    products = pandas.read_csv('products.csv')


if __name__ == '__main__':
    feature_pca()
