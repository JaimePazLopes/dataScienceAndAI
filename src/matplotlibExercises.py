import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,100)
y = x*2
z = x**2

# fig = plt.figure()
# axis = fig.add_axes([0.1,.1,.8,.8])
# axis.plot(x,y)
# axis.set_xlabel("x")
# axis.set_ylabel("y")
# axis.set_title("title")
# axis.legend()
# plt.show()

# fig = plt.figure()
# axis1 = fig.add_axes([0.1,.1,.8,.8])
# axis2 = fig.add_axes([0.2,.5,.2,.2])
# axis1.plot(x,y)
# axis2.plot(x,y)
# plt.show()

# fig = plt.figure()
# axis1 = fig.add_axes([0.15,.1,.75,.8])
# axis2 = fig.add_axes([0.25,.5,.3,.3])
# axis1.plot(x,z)
# axis1.set_xlabel("x")
# axis1.set_ylabel("z")
# axis2.plot(x,y)
# axis2.set_xlabel("x")
# axis2.set_ylabel("y")
# axis2.set_title("zoom")
# axis2.set_xlim([20, 22])
# axis2.set_ylim([30, 50])
# plt.show()

# fig, axes = plt.subplots(nrows=1, ncols=2)
# axes[0].plot(x,y, color="blue", lw=3, linestyle="--")
# axes[1].plot(x,z, color="red", lw=3)
# plt.tight_layout()
# plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,3))
axes[0].plot(x,y, color="blue", lw=3)
axes[1].plot(x,z, color="red", lw=3, linestyle="--")
plt.tight_layout()
plt.show()










