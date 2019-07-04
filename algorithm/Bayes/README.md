# 贝叶斯
## 贝叶斯原理
* 逆向概率：通过现象推测事物的本质。
* 三种概率
    * 先验概率：历史总结
    * 后验概率：结果发生后，推断原因的概率。是条件概率的一种
    * 条件概率：在A发生的条件下，X的概率是多少
    * 似然函数：
* 贝叶斯就是算后验概率，算出在A的情况下B发生的概率，在所有B的可能下找最大值  
# 朴素贝叶斯
* 前提假设：每个变量都是独立的，相互没有联系。
* 朴素贝叶斯的两种概率
    * 类型概率
    * 每个属性的条件概率
* 数据的类型
    * 离散型的数据
    * 连续型的数据    
* 朴素贝叶斯工作流程
    * 准备阶段：主要是确定属性，人工分类
    * 训练阶段：将分类后的数据进行训练
    * 应用阶段：使用模型就行分类
## sklearn机器学习包
* 三种贝叶斯算法
    * 高斯朴素贝叶斯：特征是连续的变量，符合高斯分布，比如人的身高和物体长度
    * 多项式朴素贝叶斯：特征变量是离散的，符合多项式分布，比如单词出现的次数，TF-IDF值等
    * 伯努利朴素贝叶斯：特征变量是0/1分布，比如单词是否出现。