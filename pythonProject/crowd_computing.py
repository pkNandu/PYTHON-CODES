# Trim and find mean of a range of values
import matplotlib.pyplot as plt
from scipy import stats
from statistics import mean
Estimate = [1000, 1234, 1345, 1542, 1732, 2456]
Estimate.sort()
y=[]
for i in range(len(Estimate)):
    y.append(5)
tr = int(0.1*len(Estimate))
Estimate = Estimate[tr:]
Estimate = Estimate[:len(Estimate)-tr]
print(mean(Estimate))
# -- using scipy library to trim --
# plt.plot(Estimate, y)
# m=stats.trim_mean(Estimate, 0.1)
# print(m)
