import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import  leastsq

###采样点(Xi,Yi)###
#Xi=np.array([8.19,2.72,6.39,8.71,4.7,2.66,3.78])
#Yi=np.array([7.01,2.78,6.47,6.71,4.1,4.23,4.05])

###需要拟合的函数func及误差error###
#p 包含初始的k和b
#求预测的y值

def createData(size, function, p):
    data = np.random.randint(30, size=size)
    x = data[:size-1]
    y = data[1:]
    return data, x, y

def func(p,x):
    k,b=p
    return k*x+b
#求预测值与真实值的误差
#y为真实值

def error(p, x, y, s):
    return func(p, x)-y

#test
p0 = [5, 6]
data, x, y = createData (30, func, p0)

print ("len(x)=%d, len(y)=%d"%(len(x), len(y)))
print ("原始数据:")
for d in range(len(data)):
    print (data[d], end=" ")
print ("\n所需拟合的数据对")
for x1, y1 in zip(x, y):
    print ("x=%d y=%d"%(x1, y1))

s="Test the number of iteration"
Para = leastsq(error, p0, args=(x, y, s))
k, b = Para[0]
print ("差值")
print (error(Para[0], x, y, s), end=" ")
print ("计算所得"+"k="+str(k)+"  b="+str(b))


plt.figure(figsize=(8, 6))
plt.scatter (x, y, s=6, color="red", label="samplt point", linewidth=1)
a=np.linspace(0,30,30)
b= func(Para[0], a)
plt.plot(b,color="orange",label="Fitting Line",linewidth=2) #画拟合直线


if __name__ == '__main__':
    plt.show()







