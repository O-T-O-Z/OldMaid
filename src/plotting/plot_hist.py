import matplotlib.pyplot as plt
import numpy as np

condition0 = [[1552, 1655, 1618, 1638, 1663], [1858, 1749, 1779, 1760, 1791], [1590, 1596, 1603, 1602, 1546]]
condition1 = [[1631, 1525, 1569, 1624, 1572], [1845, 1907, 1833, 1814, 1811], [1524, 1568, 1598, 1562, 1617]]
condition2 = [[1743, 1688, 1716, 1754, 1730], [1670, 1637, 1706, 1671, 1656], [1587, 1675, 1578, 1575, 1614]]

condition0_means = [np.mean(condition0[0]), np.mean(condition0[1]), np.mean(condition0[2])]
condition1_means = [np.mean(condition1[0]), np.mean(condition1[1]), np.mean(condition1[2])]
condition2_means = [np.mean(condition2[0]), np.mean(condition2[1]), np.mean(condition2[2])]

condition0_sds = [np.std(condition0[0]), np.std(condition0[1]), np.std(condition0[2])]
condition1_sds = [np.std(condition1[0]), np.std(condition1[1]), np.std(condition1[2])]
condition2_sds = [np.std(condition2[0]), np.std(condition2[1]), np.std(condition2[2])]


data_means = [condition0_means, condition1_means, condition2_means]
data_sds = [condition0_sds, condition1_sds, condition2_sds]
X = np.arange(3)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.bar(X + 0.00, data_means[0], yerr=data_sds[0],  color = 'b', width = 0.25)
ax.bar(X + 0.25, data_means[1], yerr=data_sds[1], color = 'g', width = 0.25)
ax.bar(X + 0.50, data_means[2], yerr=data_sds[2], color = 'r', width = 0.25)
ax.legend(labels=['Logic vs Random', 'Epistemic vs Random', 'Epistemic vs Logic'])
ax.set_xticks(X + 0.25)
ax.set_xticklabels(['Agent 1', 'Agent 2', 'Agent 3'])
ax.set_yticks([0, 500, 1000, 1500, 2000])
ax.set_title('Performance per Condition in 5000 Games over 5 Runs')
ax.set_ylim(1000, 2000)
ax.set_ylabel('Lost games out of 5000')
plt.savefig('barplot.png')
plt.show()