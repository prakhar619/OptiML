# %%
import gurobipy as gp

# %%
myjobTime = [4.5,7.8,3.6,2.9]
partnerjobTime =[4.9,7.2,4.3,3.1]

# %%
m = gp.Model()
#x1 == 1 means I will be doing the job1 whereas 0 means room mate will  be doing the job
x1 = m.addVar(vtype=gp.GRB.BINARY,name ='job1')
x2 = m.addVar(vtype=gp.GRB.BINARY,name='job2')
x3 = m.addVar(vtype=gp.GRB.BINARY,name='job3')
x4 = m.addVar(vtype=gp.GRB.BINARY,name='job4')
X = [x1,x2,x3,x4]

# %%
m.addConstr(x1+x2+x3+x4 == 2)
m.getConstrs()

# %%
k = 0
j = 0
for i in myjobTime:
    k += i*X[j]
    j +=1
j = 0
for i in partnerjobTime:
    k += i*(1 - X[j])
    j +=1
m.setObjective(k, gp.GRB.MINIMIZE)

# %%
m.optimize()

# %%
print("Optimising the time taken")
print("Optimal x1=",str(x1.x))
print("Optimal x2=",str(x2.x))
print("Optimal x3=",str(x3.x))
print("Optimal x4=",str(x4.x))

#x1 = 1 means I will be doing the job;
#x2 = 0 means Partner will be doing the job;

# %%
OptimalTime = m.ObjVal
print("Optimal Time to Complete the every chores",OptimalTime,"hrs")

# %%
myTime = 0
for i in range(len(myjobTime)):
    myTime += X[i].x*myjobTime[i]
partnerTime = 0
for i in range(len(partnerjobTime)):
    partnerTime += (1- X[i].x)*partnerjobTime[i]

# %%
print("Optimal Time taken by me",myTime)
print("Optimal Time taken by partner", partnerTime)

# %% [markdown]
# ### (c)

# %%
m = gp.Model()
#x1 == 1 means I will be doing the job1 whereas 0 means room mate will  be doing the job
x1 = m.addVar(vtype=gp.GRB.BINARY,name='job1')
x2 = m.addVar(vtype=gp.GRB.BINARY,name='job2')
x3 = m.addVar(vtype=gp.GRB.BINARY,name='job3')
x4 = m.addVar(vtype=gp.GRB.BINARY,name='job4')
z = m.addVar(name = "z")
X = [x1,x2,x3,x4]

# %%
m.addConstr(x1+x2+x3+x4 == 2)
k = 0
j = 0
for i in myjobTime:
    k += i*X[j]
    j +=1
j = 0
for i in partnerjobTime:
    k -= i*(1 - X[j])
    j +=1
m.addConstr(z >= k)
m.addConstr(z >= -k)
            
m.setObjective(z, gp.GRB.MINIMIZE)

# %%
m.optimize()

# %%
OptimalTime = m.ObjVal
print("Optimising the time difference")
print("Min Time differences between our chore work",OptimalTime,"hrs")

# %%
myTime = 0
for i in range(len(myjobTime)):
    myTime += X[i].x*myjobTime[i]
partnerTime = 0
for i in range(len(partnerjobTime)):
    partnerTime += (1- X[i].x)*partnerjobTime[i]

# %%
print("Optimal Time taken by me",myTime)
print("Optimal Time taken by partner", partnerTime)

# %%
print("Total Time Taken",myTime+partnerTime)

# %%


# %%



