# K-means 聚类
## K-means 工作原理
* K-means是非监督学习，不用我们进行分类，自行进行聚类。
    1. 随机的再数据中选取K个点做类的中心点
    2. 将每个点分配到最近的K个中心点中，最后就行成了K类，然后再K个类中重新计算中心点
    3. 反复2步骤，当类不再变化或者达到最大分类次数，就说明分类完成。
* 数据归一化方式
    1. 线性函数归一化（min-max scaling）:等比缩放的方式对数据进行归一化
            
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/min_max.png) 
    2. 0均值标准化（z-score standardization）:数据分布属于高斯分布效果比较好。
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/standardization.png) 
* 高斯分布：高斯分布又称正态分布。所以一般符合正太分布的都比较适合用0均值标准化
* 使用场景
    * 线性化函数：不涉及距离量度，协方差计算，数据不符合正态分布的时候，比较适合用线性函数，比如图像处理中，将RGB图像转换为灰度图像后将其值限定在\[0 255\]的范围。
    * 0均值标准化：在分类和聚类算法中，需要距离还度量相似性的时候，或者使用PCA技术进行降维的时候，表现的更好。
* 概念补充：
    * 方差（Variance）：是度量一组数据的分散程度。方差是各个样本与样本均值的差的平方和的均值
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/variance.png) 
    
    * 协方差（Covariance）是度量两个变量的变动的同步程度，也就是度量两个变量线性相关性程度。如果两个变量的协方差为0，则统计学上认为二者线性无关。注意两个无关的变量并非完全独立，只是没有线性相关性而已。计算公式如下： 
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/Covariance.png) 
    
    * 协方差矩阵（Covariance matrix）：如果协方差大于0表示一个变量增大是另一个变量也会增大，即正相关，协方差小于0表示一个变量增大是另一个变量会减小，即负相关。 协方差矩阵（Covariance matrix）由数据集中两两变量的协方差组成。矩阵的第(i,j)(i,j)个元素是数据集中第ii和第jj个元素的协方差。例如，三维数据的协方差矩阵如下所示：
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/covariance_matrix.png) 
    
    * 特征向量和特征值
        * 特征向量可以理解为坐标系
        * 特征值可以理解为点
    * PCA降维过程有点复杂，[参考链接](https://xiangdong1987.github.io/python/2019/07/08/python-guess_lottery.html)
## K-means 实战
* 利用K-means 给亚洲球队分类
    * 加载数据
    * 选取特征并进行归一化处理
    * 利用k-means算法进行聚类，将聚类结果和原始数据进行拼接返回结果
* k-means图片分割
    * 加载图片,将图片看成一个向量空间，每个点都有RGB三色值，通过将图片的每个点进行提取三色值，存入待处理数据,通过归一化函数，将数据归一化。
    * 先用k-means进行聚类，在通过模型进行预测，到每个点的label，再将一维的结果在转化成图片的矩阵。
    * 通过灰度的方式将矩阵重新生成一张灰度图片