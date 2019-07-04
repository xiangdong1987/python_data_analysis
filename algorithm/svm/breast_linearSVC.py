# encoding=utf-8
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn import metrics

# 加载数据集，你需要把数据放到目录中
data = pd.read_csv("./data.csv")
# ID 列没有用，删除该列
data.drop("id", axis=1, inplace=True)
# 将 B 良性替换为 0，M 恶性替换为 1
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
# 特征选择
features_remain = data.columns[1:31]

# 抽取 30% 的数据作为测试集，其余作为训练集
train, test = train_test_split(data, test_size=0.3)  # in this our main data is splitted into train and test
# 抽取特征选择的数值作为训练和测试数据
train_X = train[features_remain]
train_y = train['diagnosis']
test_X = test[features_remain]
test_y = test['diagnosis']

# 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
ss = StandardScaler()
train_X = ss.fit_transform(train_X)
test_X = ss.transform(test_X)

# 创建 SVM 分类器
model = svm.LinearSVC()
# 用训练集做训练
model.fit(train_X, train_y)
# 用测试集做预测
prediction = model.predict(test_X)
print('准确率: ', metrics.accuracy_score(prediction, test_y))
