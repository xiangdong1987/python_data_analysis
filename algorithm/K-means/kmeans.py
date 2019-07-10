# coding: utf-8
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np

# 输入数据
data = pd.read_csv('data.csv', encoding='gbk')
print data
feature = data.columns[1:4]
train_x = data[feature]
df = pd.DataFrame(train_x)
kmeans = KMeans(n_clusters=3)
# 线性函数归一化
min_max_scaler = preprocessing.MinMaxScaler()
train_x = min_max_scaler.fit_transform(train_x)
# kmeans 算法
kmeans.fit(train_x)
predict_y = kmeans.predict(train_x)
# 合并聚类结果，插入到原数据中
result = pd.concat((data, pd.DataFrame(predict_y)), axis=1)
result.rename({0: u'聚类'}, axis=1, inplace=True)
print(result)
