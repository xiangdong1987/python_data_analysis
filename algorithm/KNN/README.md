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
    * 欧氏距离：就是两点之间的直线距离
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/Euclidean_distance.png)
    * 曼哈顿距离：
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/manhatton.png)
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/manhatton_example.jpg)
    * 闵可夫斯基距离：是一个距离组合
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/Minkowski.png)
        * p=1 是曼哈顿距离
        * p=2 是欧氏距离
        * p→∞ 是切比雪夫距离
    * 切比雪夫距离：max(|x1-y1|,|x2-y2|)
    * 余弦距离：是向量的夹角，一般用来做兴趣相关的比较。
 ## KD树
* KD树是用来存储和查找临近值的二叉树
* KD二叉树的构造方式：
    * 随着树的深度轮流选择轴当作分区面。（例如：在三维空间中根节点是 x 轴垂直分区面，其子节点皆为 y 轴垂直分区面，其孙节点皆为 z 轴垂直分区面，其曾孙节点则皆为 x 轴垂直分区面，依此类推。）
    * 点由垂直分区面之轴座标的中位数区分并放入子树
* KD二叉树的查找方式
    * 再二叉树上根据轴和待测节点的值进行选在去左节点或者右节点，当找到了子叶节点时，还要根据以子叶节点的距离为半径，回溯是否需要父节点的相反节点纳入回溯节点。
    * KD树
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/KD1.png)         
    * 不需要回溯兄弟节点
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/KD2.png)         
    
    * 需要回溯兄弟节点
    
    ![image](https://raw.githubusercontent.com/xiangdong1987/python_data_analysis/master/static/KD3.png)         
## KNN 做回归
* 分类：是指用特征预测分类
* 回归：用分类预测特征值
## 实战用KNN手写数字进行识别
* KNN分类函数相关参数
    * n_neighbor:K值的大小，一般选择5
    * weight:临近值权重
        * uniform  权重相同
        * distance 距离大小
        * 自定义函数
    * algorithm:计算临近值算法
        * auto      自动
        * kd_tree   kd树
        * ball_tree 球树
        * brute     暴力搜索
    * leaf_size:子叶数，默认30，子叶数的大小影响搜索速度和构造速度
* 步骤
    * 数据加载
    * 数据准备：查看数据集数量，查看图片情况，数据归一化，为数据模型数据做准备
    * 通过模型进行分类
               