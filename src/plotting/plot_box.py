import matplotlib.pyplot as plt
import numpy as np

condition0 = [0.3104, 0.331, 0.3236, 0.3276, 0.3326]
condition1 = [0.3262, 0.305, 0.3138, 0.3248, 0.3144]
condition2 = [0.3486, 0.3376, 0.3432, 0.3508, 0.346]

data = [condition0, condition1, condition2]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.boxplot(data)

ax.set_title('Loss Rate per Condition in 5000 Games over 5 Runs')
ax.set_ylabel('Loss rate')
ax.set_xticklabels(['Logic vs Random', 'Epistemic vs Random', 'Epistemic vs Logic'])

print(f"Condition 0: mean {np.mean(condition0)}, sd {np.std(condition0)}")
print(f"Condition 1: mean {np.mean(condition1)}, sd {np.std(condition1)}")
print(f"Condition 2: mean {np.mean(condition2)}, sd {np.std(condition2)}")

plt.savefig('../../docs/assets/img/boxplot.png')
plt.show()