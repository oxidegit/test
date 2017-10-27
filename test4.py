import pylab
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def decode(N, p, k):
    a, b = p
    x0 = N[0]
    result = [x0]

    for i in range(len(N)-1):
        i = i+1 # i从 1 到 len(N)-1

        if (abs(N[i]-N[i-1])>k):
            result.append(N[i])
        else:
            result.append(N[i]+func(p, result[i-1]))

    print (len(result))
    return result

#返回原始数据的编码序列和所拟合的 直线信息
def code(data, k, i):
    oldx = data[:len(data) - 1]
    oldy = data[1:]

    ziped = zip(oldx, oldy)
    oldxy = list(ziped)
    newxy = []

    #剔除异常点
    for x, y in oldxy:
        if (abs(y-x) <= k  ):
            newxy.append((x, y))
    #print ("new %d"%(len(newxy)))
    newx, newy = zip(*newxy)

    print ("第%d列中能够压缩的数据数%d"%(i, len(newxy)))
    """
    plt.figure(i)
    plt.scatter(newx, newy)
    plt.show()
    """

    #最小二乘求a, b
    p0 = [4, 5]
    Para = leastsq(error, p0, args=(newx, newy))
    a, b = Para[0]

    #求最后的序列N
    N = [oldx[0]] #x0 作为第一个flag,首先被添加
    #迭代的add最后i-1个差值
    p = (a, b)
    for x, y in oldxy:
        delta = y-func(p, x)
        if (abs(delta) <= k):
            N.append(delta)
        else:
            N.append(y)

    return (N, p)

def getColData(c, path):
	a = np.loadtxt(path)
	b = a[:, c]

	return b

def getError(x, y):
	return list(map(lambda x, y: x-y, x, y))

def getErrorList(x, y, k, b):
	return list(map(lambda x, y: (k*x+b)-y, x, y))

def func(p,x):
    k,b=p
    return k*x+b

def error(p,x,y):
	return list(map(lambda x,y:func(p, x)-y, x, y))


if __name__ == "__main__":


    for i in range(50):
        data = getColData(i, "C:\\Users\\f404-1\\Desktop\\data1.txt")
        N, p = code(data, 10, i)

        print("原始数据是：")
        print(list(data))
        print ("a=%f b=%f"%(p[0], p[1]))
        print ("经压缩后的数据是")
        #print (N)
        result = decode(N, p, 1)
        print ("解压缩后的数据是")
        print (result)

        #rint (len(N))
        plt.figure(i)
        plt.scatter(range(len(N)), N)
        plt.show()

