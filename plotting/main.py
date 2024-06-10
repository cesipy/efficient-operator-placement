import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['ODP', 'Lokale Suche', 'Tabu Suche', 'Greedy First-Fit', 'Greedy First-Fit (keine δ)']
BF_LZ = [0.1, 0.68, 0.31, 454.40, 454.40]
BF_SA = [41.4, 150.54, 65.91, 56e4, 56e4]
BF_RA = [915.2, 353.07, 64.93, 12e6, 12e6]
BF_Avg = [None, 215.81, 83.53, 11e6, 11e6]

QE_LZ = [None, 0, 0, 0, 34]
QE_SA = [None, 1, 1, 7, 7]
QE_RA = [None, 4, 4, 5, 24]
QE_Avg = [None, 1, 1, 11, 19]

# Bar plot for BF
x = np.arange(len(methods))
width = 0.2

fig, ax1 = plt.subplots(figsize=(12, 8))

rects1 = ax1.bar(x - 1.5*width, BF_LZ, width, label='LZ')
rects2 = ax1.bar(x - 0.5*width, BF_SA, width, label='SA')
rects3 = ax1.bar(x + 0.5*width, BF_RA, width, label='RA')
rects4 = ax1.bar(x + 1.5*width, BF_Avg, width, label='Average')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax1.set_xlabel('Methods')
ax1.set_ylabel('Values')
ax1.set_title('BF (Best Fit) Metrics')
ax1.set_xticks(x)
ax1.set_xticklabels(methods)
ax1.legend()

fig.tight_layout()

# Line plot for QE
fig, ax2 = plt.subplots(figsize=(12, 8))

ax2.plot(methods[1:], QE_LZ[1:], marker='o', label='LZ')
ax2.plot(methods[1:], QE_SA[1:], marker='o', label='SA')
ax2.plot(methods[1:], QE_RA[1:], marker='o', label='RA')
ax2.plot(methods[1:], QE_Avg[1:], marker='o', label='Average')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax2.set_xlabel('Methods')
ax2.set_ylabel('Percentage')
ax2.set_title('QE (Quality Estimation) Metrics')
ax2.legend()

plt.show()
