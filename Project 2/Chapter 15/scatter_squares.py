import matplotlib.pyplot as plot

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plot.style.use("seaborn")
fig, ax = plot.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plot.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plot.show()
#plot.savefig("squares_plot.png", bbox_inches="tight")