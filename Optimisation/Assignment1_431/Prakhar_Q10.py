# %%
# Input needs to be list of vertex and list of all transitions
V = ['S','A','B','C','D','E','F','G','H','I','J','T']
E = [('S','A',10),('S','D',5),('S','C',2),('S','E',4),('A','B',4),('A','G',2),('A','C',2),('C','G',8),('C','E',5),('E','G',7),('E','F',2),('D','J',2),('D','E',3),('J','F',1),('J','I',5),('F','T', 6),('F','I',10),('G','F',2),('G','H',2),('B','H',3),('I','T',7),('H','T',9),('T','G',6)]

# %%
for i in V:
    connectionCount = 0
    for tu in E:
        if tu[0] == i or tu[1] == i:
            connectionCount += 1
    print("Vertex:",i,"Connections:",connectionCount)

# %%
c = {}
for i in V:
    x1 = {}
    for tu in E:
        if i == tu[0]:
            x1[tu[1]] = tu[2]
    if x1 != {}:
        c[i] = x1


# %%
c

# %%
from gurobipy import *

# %%
m = Model()
x = {}
for i in c:
    x1 = {}
    for j in c[i]:
        varname = str('var'+i+j)
        x1[j] = m.addVar(lb = 0, name=varname)
    x[i] = x1
v = m.addVar(lb = 0, name="maxFlow")


# %%
for i in x:
    sum_= 0
    sum = 0
    for j in x[i]:
        sum += x[i][j]
        m.addConstr(x[i][j] <= c[i][j])
    for j in x:
        if i in x[j]:
            sum_ += x[j][i]
    if(i == 'S'):
            m.addConstr(sum - sum_ == v) 
    elif(i == 'T'):
            m.addConstr(sum - sum_ == -v)
    else:
        m.addConstr(sum - sum_ == 0)


# %%
m.setObjective(v,GRB.MAXIMIZE)

# %%
m.optimize()

# %%
OptimalTime = m.ObjVal
print("MaxFlow:",OptimalTime)

# %%
v.x

# %% [markdown]
# ### Method2

# %%
from gurobipy import *

# %%
n = Model()
y = {}
for i in c:
    x1 = {}
    for j in c[i]:
        varname = str('var'+i+j)
        x1[j] = n.addVar(lb = 0, name=varname)
    y[i] = x1

# %%
u = {}
for i in c:
    u[i] = n.addVar(name="u"+i)

# %%
for i in y:
    for j in y[i]:
        n.addConstr(u[i] - u[j] + y[i][j] >= 0)
n.addConstr(-u['S'] + u['T'] == 1)

# %%
sum = 0
for i in y:
    for j in y[i]:
        sum += c[i][j]*y[i][j]
print(sum)
n.setObjective(sum,GRB.MINIMIZE)

# %%
n.optimize()

# %%
n.ObjVal

# %%


u['T']

# %%
u['S']


# %%


# %%



