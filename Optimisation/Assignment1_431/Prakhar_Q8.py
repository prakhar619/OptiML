# %%
import numpy as np 
import matplotlib.pyplot as plt
import math 
from mpl_toolkits.mplot3d import axes3d

# %%
def rosenbrock(x1,x2):
    return (1- x1)**2 + 100*(x2 - x1**2)**2

# %%
#df(x1,x2)/dx1 =  2(1-x1)*-1 + 100*2(x2 - x1^2)*-2x1
#df(x1,x2)/dx2 = 100*2(x2 - x1^2)
def d_rosenbrock(x1,x2):
    d_x1 = 2*(1- x1)*(-1) + 100*2*(x2 - x1**2) *(-2*x1)
    d_x2 = 100*2*(x2 - x1**2)
    return (d_x1,d_x2)

# %%
def dd_rosenbrock(x1,x2):
    d_x1x1 = 2 + 100*2*(-2)*(x2 - 3 * x1** 2)
    d_x1x2 = 100*2*(-2)*x1
    d_x2x2 = 100*2
    return (d_x1x1,d_x1x2,d_x2x2)

# %%
x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x, y)

# %%
plt.title("Rosenbrock Function")
plt.contour(X,Y,rosenbrock(X,Y))
plt.clabel(plt.contour(X, Y, rosenbrock(X,Y), levels=[0.5,2,5,10,50,100,200,400,800]), fontsize=5)

# %%



