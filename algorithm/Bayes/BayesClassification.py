# encoding=utf-8
# 读取文件，进行分词
import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import io

# 读取全部文件 并返回所有分词以及分类
def load_file(file_dir, label):
    """
    将路径下的所有文件加载
    :param file_dir: 保存txt文件目录
    :param label: 文档标签
    :return: 分词后的文档列表和标签
    """
    file_list = os.listdir(file_dir)
    words_list = []
    labels_list = []
    for file in file_list:
        file_path = file_dir + '/' + file
        words_list.append(cut_words(file_path))
        labels_list.append(label)
    return words_list, labels_list


# 切分单词
def cut_words(file_path):
    """
    对文本进行切词
    :param file_path: txt文本路径
    :return: 用空格分词的字符串
    """
    text_with_spaces = ''
    text = io.open(file_path, 'r', encoding='gb18030').read()
    textcut = jieba.cut(text)
    for word in textcut:
        text_with_spaces += word + ' '
    return text_with_spaces


# 训练数据处理
train_word_list1, train_labels1 = load_file('D:\\data\\python\\test\\algorithm\\Bayes\\train\\woman', 'woman')
train_word_list2, train_labels2 = load_file('D:\\data\\python\\test\\algorithm\\Bayes\\train\\sport', 'sport')
train_word_list3, train_labels3 = load_file('D:\\data\\python\\test\\algorithm\\Bayes\\train\\literature', 'literature')
train_word_list4, train_labels4 = load_file('D:\\data\\python\\test\\algorithm\\Bayes\\train\\school', 'school')
# 整合数据
train_word_list = train_word_list1 + train_word_list2 + train_word_list3 + train_word_list4
train_labels = train_labels1 + train_labels2 + train_labels3 + train_labels4
# 测试数据处理
test_word_list1, test_labels1 = load_file('D:/data/python/test/algorithm/Bayes/test/woman', 'woman')
test_word_list2, test_labels2 = load_file('D:/data/python/test/algorithm/Bayes/test/sport', 'sport')
test_word_list3, test_labels3 = load_file('D:/data/python/test/algorithm/Bayes/test/literature', 'literature')
test_word_list4, test_labels4 = load_file('D:/data/python/test/algorithm/Bayes/test/school', 'school')
# 整合数据
test_word_list = test_word_list1 + test_word_list2 + test_word_list3 + test_word_list4
test_labels = test_labels1 + test_labels2 + test_labels3 + test_labels4

# 加载停用词
stop_words = io.open('stop/stopword.txt', 'r', encoding='utf-8').read()
stop_words = stop_words.encode('utf-8').decode('utf-8-sig')  # 列表头部\ufeff处理
stop_words = stop_words.split('\n')  # 根据分隔符分隔

# 计算分词权重
tf = TfidfVectorizer(stop_words=stop_words, max_df=0.5)
# 特征抽取
train_features = tf.fit_transform(train_word_list)
test_features = tf.transform(test_word_list)

# 多项式贝叶斯分类器
clf = MultinomialNB(alpha=0.001).fit(train_features, train_labels)
predicted_labels = clf.predict(test_features)
print predicted_labels
# 计算准确率
print('准确率为：', metrics.accuracy_score(test_labels, predicted_labels))