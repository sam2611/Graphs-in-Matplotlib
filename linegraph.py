from matplotlib import pyplot
from matplotlib import style
style.use("ggplot")
x = [2,4,6]
y = [4,7,8]

x2 = [4,5,7]
y2 = [16,12,6]


pyplot.plot(x, y,"g",label="line one",linewidth=5)
pyplot.plot(x2, y2,"r",label="line two",linewidth=5)

pyplot.title("INFORMATION")
pyplot.ylabel("Y-axis")
pyplot.xlabel("X-label")
pyplot.legend()
pyplot.grid(True,color="c")
pyplot.show()
