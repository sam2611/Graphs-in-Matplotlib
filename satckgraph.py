from matplotlib import pyplot
days=[1,2,3,4,5]
sleeping=[1,2,3,4,5]
eating=[3,4,6,1,2]
playing=[6,8,3,4,7]
working=[3,4,8,5,4]

pyplot.plot([],[],label="sleeping",color="r",linewidth=5)
pyplot.plot([],[],label="eating",color="c",linewidth=5)
pyplot.plot([],[],label="playing",color="m",linewidth=5)
pyplot.plot([],[],label="working",color="g",linewidth=5)

pyplot.stackplot(days,sleeping,eating,playing,working,colors=["r","c","m","g"])

pyplot.title("INFORMATION")
pyplot.ylabel("Y-axis")
pyplot.xlabel("x-axis")
pyplot.legend()
pyplot.show()