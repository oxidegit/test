#实验一下y=ax1+bx2+cx3+d这种预测方案
import pylab
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

def decode(N, p, k):
    a, b, c = p
    x0 = N[0]
    x1 = N[1]
    result = [x0, x1]

    for i in range(len(N) - 2):
        i = i + 2  # i从 1 到 len(N)-1

        if (abs((N[i]-N[i-1])-(N[i-1]-N[i-2])) > k):
            result.append(N[i])
        else:
            result.append(N[i] + func(p, result[i - 2], result[i-1]))
    return result

def code(data, k, i):
    oldx1 = data[:len(data)-3]
    oldx2 = data[1:len(data)-2]
    oldx3 = data[2:len(data)-1]
    oldy = data[2:len(data)]

    ziped = zip(oldx1, oldx2, oldx3, oldy)
    oldxyz = list(ziped)
    #用来保存去除突变点后的训练点
    newxyz = []

    """
    # 剔除异常点
    for x, y, z in oldxyz:
        if (abs((z-y)-(y-x)) <= k):
            newxyz.append((x, y, z))
    # print ("new %d"%(len(newxy)))
    newx, newy, newz = zip(*newxyz)

    print("第%d列中能够压缩的数据数%d" % (i, len(newxyz)))
    """
    p0 = [2, -1, 0, 4]
    Para = leastsq(error, p0, args=(oldx1, oldx2, oldx3, oldy))
    a, b, c, d= Para[0]

    N = [oldx1[0], oldx2[0], oldx3[0]]

    p = (a, b, c, d)
    count = 0
    for x1, x2, x3, x4 in oldxyz:
        delta = x4-func(p, x1, x2, x3)
        delta = abs(delta)
        if ((delta-(k))<=0):
            N.append(delta)
            count = count+1
        else:
            N.append(x4)

    return (N, p, count)

def getColData(c, path):
	a = np.loadtxt(path)
	b = a[:, c]
	return b

def func(p,x1, x2, x3):
    a, b, c, d = p
    return a * x1 + b * x2 + c*x3+d

def error(p,x1,x2,x3, y):
    return list(map(lambda x1, x2,x3, y: func(p, x1, x2, x3) - y, x1, x2,x3, y))

if __name__ == "__main__":
    for i in range(10):
        i = i+3
        data = getColData(i, "C:\\Users\\lenovo-pc\\Desktop\\data.txt")
        N, p, count = code(data, 4.0, i)
        print(count)
        print(N)
        """
        print("原始数据是：")
        print(list(data))
        print("a=%f b=%f c=%f" % (p[0], p[1], p[2]))
        print("经压缩后的数据是")
        print (N)
        result = decode(N, p, 5)
        print("解压缩后的数据是")
        print(result)
        """
