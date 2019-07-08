# 双色球预测到放弃
## 起因
我一直有个发财梦，就是靠技术能计算出双色球的走势，从而实现财富自由走向人生巅峰，这个梦一直魂牵梦绕着我，直到最新开始学大数据分析开始，我坚信只要有梦想早晚一天会破碎。
## 过程
学习过程历时2周，从python语言基础到，大数据分析工具的使用。过程参考下面的github
* [https://github.com/xiangdong1987/python_data_analysis](https://github.com/xiangdong1987/python_data_analysis "https://github.com/xiangdong1987/python_data_analysis")

课程是根据极客时间的下面的课程
* [数据分析实战45讲](https://time.geekbang.org/column/intro/147 "数据分析实战")

总体感受，老师讲的挺实战的，不过如果讲原理也太多太深的数学知识也很难消化，比如我自己也展开的看了看，不过太难了，还是需要的时候看吧

对于大数据分析无外乎三个阶段

* 数据获取与加载（80%的时间）
* 数据清洗与加工（15%的时间）
* 模型生成与预测（5%的时间）

使用的数据算法包含如下几种（还有几种还没学完，想看关注github）：

* [贝叶斯算法](https://github.com/xiangdong1987/python_data_analysis/tree/master/algorithm/Bayes "贝叶斯算法")
* [决策树算法](https://github.com/xiangdong1987/python_data_analysis/tree/master/algorithm/decisionTree "决策树算法")
* [SVM算法](https://github.com/xiangdong1987/python_data_analysis/tree/master/algorithm/svm "SVM算法")
* [KNN算法](https://github.com/xiangdong1987/python_data_analysis/tree/master/algorithm/KNN "KNN算法")

通过用不同的算法对不同的数据类型就行预测，而得到我们想要预测的模型，这个整个过程就是大数据分析，大数据关键问题就是数据。
## 简单的过程描述
1. 我的数据获取是用爬虫对[http://datachart.500.com/ssq/?expect=100](http://datachart.500.com/ssq/?expect=100) 的历史数据进行爬去，代码实践请看git。
2. 我对数据进行了处理，讲获取的历史数据错开期数进行排序，用当期的数据预测下期的结果。
3. 利用svm 多项式回归，对结果进行预测结果越接近1 就是下期出现某数。
## 犯过的愚蠢错误
用整个训练集中的一条进行预测，结果发现100% 中奖我以为我发了，好吧是我太蠢了。
## 总结
通过预测的结果显示，中一个数据的概率非常小，所有的中奖概率每一期都是8亿分之1，每一次都是独立的事件，是无法根据历史数据来预测的，对于可预测时间必须是一种能线性或者真实存在的某种规律才能进行预测。好吧我的发财梦碎了，老实的板砖吧！
