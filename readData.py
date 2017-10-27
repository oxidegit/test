import pylab
import numpy as np
import scipy.stats as stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

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

def readfile(filename):
	data = []
	with open(filename,'r') as f:
		for line in f.readlines():
			linestr = line.strip()
			linestrlist = linestr.split("\t")
			linelist = list(map(float,linestrlist))# 方法一
			# linelist = [int(i) for i in linestrlist] # 方法二
			for i in linelist:
				data.append(i)
	return data


def isNormal(data):
	x = data[:len(data) - 1]
	y = data[1:]

	p0 = [4, 5]
	Para = leastsq(error, p0, args=(x, y))
	k, b = Para[0]
	errorList = getErrorList(x, y, k, b)
	print(errorList)

	stats.probplot(errorList, dist="norm", plot=pylab)
	pylab.show()

if __name__ == "__main__":

	#拟合直线的散点图
	p0 = (4, 5)
	for i in range (30):
		data = getColData(i, "C:\\Users\\f404-1\\Desktop\\data1.txt")
		x = data[:len(data) - 1]
		y = data[1:]
		p0 = (4, 5)
		Para = leastsq(error, p0, args=(x, y))
		k, b = Para[0]
		err = getErrorList(x, y, k, b)

		plt.figure(i)
		plt.scatter(range(len(err)), err)
	plt.show()
	#y=x 直线差值的散点图
	

	"""p0 = (4, 5)
	for i in range (30):
		data = getColData(i, "C:\\Users\\f404-1\\Desktop\\data1.txt")
		x = data[:len(data) - 1]
		y = data[1:]
		error = getError(x, y)
		plt.figure(i)
		plt.scatter(range(len(error)), error)
	plt.show()"""

	#拟合
	"""p0 = (4, 5)
	for i in range (20):
		data = getColData(i, "C:\\Users\\f404-1\\Desktop\\data1.txt")
		x = data[:len(data) - 1]
		y = data[1:]
		plt.figure(i)
		plt.scatter(x, y)
		Para = leastsq(error, p0, args=(x, y))
		k, b = Para[0]
		print (k, b)
		plt.plot(x, x, color="orange", label="Fitting Line", linewidth=2)  # 画拟合直
	plt.show()"""

	#（xi, xi+1）散点图
	"""for i in range(50):
		data = getColData(i, "C:\\Users\\f404-1\\Desktop\\data1.txt")
		#print (data)
		x = data[:len(data)-1]
		y = data[1:]
		f = plt.figure(i)
		plt.scatter(x, y)"""

	"""
	#某一列的散点图
	for i in range (30):
		testData = getColData(i, "C:\\Users\\f404-1\\Desktop\\data1.txt")

		plt.figure(i)
		plt.scatter(range(len(testData)), testData)

	plt.show()

	"""
	#画图













