from matplotlib import pyplot

pyplot.bar([1,4,5],[4,5,6],label="Example one",color="r")
pyplot.bar([2,6,3],[1,8,10],label="Example two",color="c")
pyplot.legend()
pyplot.ylabel("y axis")
pyplot.xlabel("x axis")
pyplot.title("info")
pyplot.show()