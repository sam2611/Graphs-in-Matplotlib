from matplotlib import pyplot

slices = [7, 2, 2, 13]
cols = ["c", "m", "r", "b"]
activities = ['sleeping', 'eating', 'playing', 'working']

pyplot.pie(slices,
           labels=activities,
           colors=cols,
           startangle=90,
           shadow=True,
           explode=(0, 0.1, 0, 0),
           autopct="%1.1f%%")

pyplot.title("pie chart")
pyplot.show()
