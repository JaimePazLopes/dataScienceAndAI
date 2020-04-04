import matplotlib.pyplot as plot
import numpy

#plt.show()

x = numpy.linspace(0,5,11)
y = x**2

# plot.plot(x,y)
# plot.xlabel("X Label")
# plot.xlabel("Y Label")
# plot.xlabel("Title")
# #plot.show()
#
# plot.subplot(1,2,1)
# plot.plot(x,y,"r")
# plot.subplot(1,2,2)
# plot.plot(y,x,"b")
# #plot.show()

# fig = plot.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel("X Label")
# axes.set_ylabel("Y Label")
# axes.set_title("Title")
# #plot.show()

# fig = plot.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.2,0.6,0.6])
# axes3 = fig.add_axes([0.3,0.3,0.4,0.4])
# axes4 = fig.add_axes([0.4,0.4,0.2,0.2])
# axes1.plot(x,y)
# axes2.plot(y,x)
# axes3.plot(x,x)
# axes3.set_title("Hue")
# axes4.plot(y,y)
# plot.show()

# fig, axes = plot.subplots(nrows=3, ncols=3)
# for axeX in range(3):
#     for axeY in range(3):
#         axes[axeX][axeY].plot(x,y)
# plot.tight_layout()
# fig.savefig("..\\files\\myFig.png", dpi=200)
# plot.show()

fig = plot.figure()
axes = fig.add_axes([0.1,0.1,.8,.8])
axes.plot(x,y, label="x,y", color = "orange", lw=0.5, linestyle="-.", marker="1")
axes.set_xlim([1,5])
axes.plot(y,x, label="y,x", color="yellow", linewidth=5, ls="steps", marker="o", markersize=20,markerfacecolor="purple",
          markeredgewidth=10,markeredgecolor="green")
axes.plot(y,y, label="y,y", color="r", alpha=0.3, linestyle=":", marker="+")
axes.legend(loc=10)
plot.show()












