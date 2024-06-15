import matplotlib.pyplot as plt
import numpy as np

# Data from the table
methods = [
    "ODP", "ODP", "Greedy First-Fit", "Greedy First-Fit", 
    "Greedy First-Fit (keine $\\delta$)", "Greedy First-Fit (keine $\\delta$)",
    "Lokale Suche", "Lokale Suche", "Tabu Suche", "Tabu Suche"
]

labels = ["LZ", "LZ", "LZ", "QE", "LZ", "QE", "LZ", "QE", "LZ", "QE"]
SA_values = [41.4, 2174.8, 0.06, 0.07, 0.057, 0.07, 213.9, 0.01, 493.1, 0.01]
RA_values = [915.2, 32193.9, 0.00001, 0.05, 0.00001, 0.24, 91.1, 0.04, 495.8, 0.04]

# Convert percentages to decimal for consistency in QE
for i in range(len(labels)):
    if labels[i] == "QE":
        SA_values[i] *= 100
        RA_values[i] *= 100

# Create separate lists for each type (LZ and QE)
methods_lz = [methods[i] for i in range(len(labels)) if labels[i] == "LZ"]
SA_lz = [SA_values[i] for i in range(len(labels)) if labels[i] == "LZ"]
RA_lz = [RA_values[i] for i in range(len(labels)) if labels[i] == "LZ"]

methods_qe = [methods[i] for i in range(len(labels)) if labels[i] == "QE"]
SA_qe = [SA_values[i] for i in range(len(labels)) if labels[i] == "QE"]
RA_qe = [RA_values[i] for i in range(len(labels)) if labels[i] == "QE"]

x_lz = np.arange(len(methods_lz))
x_qe = np.arange(len(methods_qe))

fig, ax = plt.subplots(2, 1, figsize=(10, 12))

# Bar plot for LZ with log scale
width = 0.35
ax[0].bar(x_lz - width/2, SA_lz, width, label='SA')
ax[0].bar(x_lz + width/2, RA_lz, width, label='RA')

ax[0].set_xlabel('Methods')
ax[0].set_ylabel('Values')
ax[0].set_title('LZ Values (Log Scale)')
ax[0].set_xticks(x_lz)
ax[0].set_xticklabels(methods_lz, rotation=45, ha='right')
ax[0].legend()
ax[0].set_yscale('log')

# Bar plot for QE
ax[1].bar(x_qe - width/2, SA_qe, width, label='SA')
ax[1].bar(x_qe + width/2, RA_qe, width, label='RA')

ax[1].set_xlabel('Methods')
ax[1].set_ylabel('Values')
ax[1].set_title('QE Values')
ax[1].set_xticks(x_qe)
ax[1].set_xticklabels(methods_qe, rotation=45, ha='right')
ax[1].legend()

plt.tight_layout()
plt.show()
