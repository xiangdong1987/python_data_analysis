# encoding=utf-8
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.preprocessing import StandardScaler


# 猜数字
def get_number(data, name, my_num):
    # print name
    # 特征选择
    features_source = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17',
                       '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33']
    features_result = [name]
    # 抽取 30% 的数据作为测试集，其余作为训练集
    train, test = train_test_split(data, test_size=0.1)  # in this our main data is splitted into train and test
    # 抽取特征选择的数值作为训练和测试数据
    train_X = train[features_source]
    train_y = train[features_result]
    test_X = test[features_source]
    test_y = test[features_result]
    # 采用 Z-Score 规范化数据，保证每个特征维度的数据均值为 0，方差为 1
    ss = StandardScaler()
    train_X = ss.fit_transform(train_X)
    test_X = ss.transform(test_X)
    my_num = ss.transform(my_num)

    # 创建 SVM 分类器
    model_1 = svm.SVC()
    # 用训练集做训练
    model_1.fit(train_X, train_y)
    # 用测试集做预测
    # prediction_1 = model_1.predict(test_X)
    result = model_1.predict(my_num)
    # print result
    # print('准确率: ', metrics.accuracy_score(prediction_1, test_y))
    return result


# 加载数据集，你需要把数据放到目录中
data = pd.read_csv("./lottery.csv")
# 数据探索
# 因为数据集中列比较多，我们需要把 dataframe 中的列全部显示出来
pd.set_option('display.max_columns', None)
# 数据清洗
# 将特征字段分成 3 组
# 数据清洗
# ID 列没有用，删除该列
data.drop("lottery_id", axis=1, inplace=True)
my_num = [
    [4, 4, 9, 10, 2, 4, 15, 2, 5, 23, 8, 1, 13, 9, 1, 4, 11, 4, 1, 1, 3, 2, 15, 6, 8, 9, 3, 26, 1, 5, 2, 1, 2]]
num = []
for i in range(0, 33):
    num.append(get_number(data, 'r' + str(i + 1), my_num)[0])
print num
