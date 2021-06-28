from matplotlib import pyplot

population_ages = [22, 23, 45, 55, 67, 64, 34, 55, 77, 64, 56, 80, 22, 13, 23, 31, 45, 67, 100, 99, 120]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]

pyplot.hist(population_ages,bins,histtype='bar',rwidth=0.8)
pyplot.xlabel("x")
pyplot.ylabel("y")
pyplot.title("HISTOGRAM")
pyplot.legend()
pyplot.show()