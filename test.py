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
    x = np.random.randint(10, size=size)
    y = function(p, x)+ np.random.randn(size)
    return x, y

def func(p,x):
    k,b=p
    return k*x+b
#求预测值与真实值的误差
#y为真实值

def error(p, x, y, s):
    return func(p, x)-y;

#test
p0 = [5, 6]
x, y = createData (20, func, p0)
print ("x序列")
print (x)
print ("y序列")
print (y)

s="Test the number of iteration"
Para = leastsq(error, p0, args=(x, y, s))
k, b = Para[0]
print ("差值")
print (error(Para[0], x, y, s))
print ("计算所得"+"k="+str(k)+"  b="+str(b))


plt.figure(figsize=(8, 6))
plt.scatter (x, y, s=6, color="red", label="samplt point", linewidth=1)
x=np.linspace(0,10,10)
y= func(p0, x)
plt.plot(x,y,color="orange",label="Fitting Line",linewidth=2) #画拟合直线


if __name__ == '__main__':
    plt.show()







