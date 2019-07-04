# KNN(K-nearest Neighbor)
## KNN 原理
* KNN原理比较简单，相当于近朱者赤近墨者黑的原则，实现方式如下：
    1. 计算待分类物体与其他物体的距离
    2. 统计最近的K个邻居
    3. K个邻居属于哪个分类，这个待分类物体就是哪个分类
* K值的选择
    * 如果K值选的太小会造成过拟合
    * 反之K值选的太大会造成欠拟合
* 计算距离的方式选择
    * 欧氏距离：直线距离
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/Euclidean_distance.png)
    * 曼哈顿距离：
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/manhatton.png)
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/manhatton_example.jpg)
    * 闵可夫斯基距离
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/Minkowski.png)
    * 切比雪夫距离
    * 余弦距离
        