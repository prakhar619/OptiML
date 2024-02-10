# %%
import math
import matplotlib.pyplot as plt
import numpy as np

# %%
def f(x):
    return x**5 + 5 * (math.e**(-3*x))

# %%
def df(x):
    return 5* x**5 + 5*math.e**(-3*x) * -3

# %%
def ddf(x):
    return 20* x**3 + 5*math.e**(-3*x) * 9

# %%
def f_0Ordr(x,h):
    return f(x)

# %%
def f_1Ordr(x,h):
    return f_0Ordr(x,h) + h * df(x)

# %%
def f_2Ordr(x,h):
    return f_1Ordr(x,h) + (h**2 * ddf(x))/2

# %%
region = np.linspace(-0.2,0.2,100)
x0 = 1
x1 = 2

# %%
x0_ = x0 + region
x1_ = x1 + region

# %%
plt.title("Q7 Around x="+str(x0))
plt.plot(x0_,f(x0_), color='r')
plt.plot(x0_,f_1Ordr(x0_,region), color='g' )
plt.plot(x0_,f_2Ordr(x0_,region))

# %%
plt.title("Q7 Around x="+str(x1))
plt.plot(x1_,f(x0_), color='r')
plt.plot(x1_,f_1Ordr(x0_,region), color='g' )
plt.plot(x1_,f_2Ordr(x0_,region))

# %%



