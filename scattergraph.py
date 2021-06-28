from matplotlib import pyplot

x=[1,2,3,4,5,6,7,8]
y=[3,4,6,1,2,7,8,0]

pyplot.scatter(x, y,label="skitscat",color="r")


pyplot.title("INFORMATION")
pyplot.ylabel("Y-axis")
pyplot.xlabel("x-axis")
pyplot.legend()
pyplot.show()