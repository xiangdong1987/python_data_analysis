#_*_ coding:utf-8 _*_
import numpy as np
# array数组
a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
b[1,1] = 10
print a.shape
print b.shape
print a.dtype
print b
# format array
personType=np.dtype({
    'names':['name','age','chinese','math','english'],
    'formats':['S32','i','i','i','f']})
peoples=np.array([('zhangfei',32,75,100,90),('guanyu',24,85,96,88.5),('zhaoyun',28,85,92,96.8),('huangzhong',29,65,85,100)],dtype=personType)
ages=peoples[:]['age']
chineses=peoples[:]['chinese']
maths=peoples[:]['math']
englishes=peoples[:]['english']
print np.mean(ages)
print np.mean(chineses)
print np.mean(maths)
print np.mean(englishes)
# nfunc
a1=np.add.reduce([1,2,3])                  #1+2+3=6
a2=np.add.reduce([[1,2,3],[4,5,6]])        #[1+4,2+5,3+6]=[5,7,9]
a3=np.add.reduce([[1,2,3],[4,5,6]],axis=1) #[1+2+3,4+5+6]=[6,15]
a4=np.add.reduce([[1,2,3],[4,5,6]],axis=0) #[14,2+5,3+6]=[5,7,9]
print a1
print a2
print a3
print a4
# create array
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print x1
print x2
# arithmetic operation
x1 = np.arange(1,11,2)
x2 = np.linspace(1,9,5)
print np.add(x1, x2)
print np.subtract(x1, x2)
print np.multiply(x1, x2)
print np.divide(x1, x2)
print np.power(x1, x2)
print np.remainder(x1, x2)
# statistics func
import numpy as np
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print np.amin(a)
print np.amin(a,0)
print np.amin(a,1)
print np.amax(a)
print np.amax(a,0)
print np.amax(a,1)
# ptp max - min
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print np.ptp(a)
print np.ptp(a,0)
print np.ptp(a,1)
# percentile
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print np.percentile(a, 50)
print np.percentile(a, 50, axis=0)
print np.percentile(a, 50, axis=1)
# median() mean()
a = np.array([[1,2,3], [4,5,6], [7,8,9]])
print np.median(a)
print np.median(a, axis=0)
print np.median(a, axis=1)
print np.mean(a)
print np.mean(a, axis=0)
print np.mean(a, axis=1)
# average()
a = np.array([1,2,3,4])
wts = np.array([1,2,3,4])
print np.average(a)
print np.average(a,weights=wts)
# std() var()
a = np.array([1,2,3,4])
print np.std(a)
print np.var(a)
# exercise
personTypeNew=np.dtype({
    'names':['name','english','chinese','math'],
    'formats':['S32','i','i','i']})
peoples=np.array([('zhangfei',66,65,30),('guanyu',95,85,89),('zhaoyun',93,92,96),('huangzhong',90,88,77),('dianwei',80,90,90)],dtype=personTypeNew)
chineses=peoples[:]['chinese']
maths=peoples[:]['math']
englishes=peoples[:]['english']
print ('Average chinese is %f' %np.mean(chineses))
print ('Average maths is %f' %np.mean(maths))
print ('Average english is %f' %np.mean(englishes))
print ('Chinese is max %d and min %d' %(np.max(chineses),np.min(chineses)))
print ('Maths is max %d and min %d' %(np.max(maths),np.min(maths)))
print ('English is max %d and min %d' %(np.max(englishes),np.min(englishes)))
peoplesArray=np.array([(66,65,30),(95,85,89),(93,92,96),(90,88,77),(80,90,90)])
print ('Std is %f' %np.std(peoplesArray))
print ('Var is %f' %np.var(peoplesArray))
total = np.add(chineses,maths)
total = np.add(total,englishes)
print total
print np.sort(total)