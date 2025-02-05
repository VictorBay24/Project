import matplotlib.pyplot as plt 
import numpy as np

wavelengths={5: 74, 6: 26}
x=[]
y=[]
for i in wavelengths:
    x.append(i)
    y.append(wavelengths[i])

""" plt.bar(x,y)
plt.show()   """



species = ("Find solution", "Find optimal solution", "Runtime")
penguin_means = {
    'Find solution': (100, 0),
    'Find optimal solution': (37, 0),
    'Runtime': (0.007231100993230939, 9.9591610279819),
}

x = np.arange(len(species))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

# Unpack the measurements for comparison
labels = ['SA', 'QA']

# Transpose the data to loop over individual metrics
measurements = list(zip(*penguin_means.values()))

# Scale runtime values for better comparison (optional)
scaled_measurements = [list(m) if i < 2 else [v * 1000 for v in m] for i, m in enumerate(measurements)]

for idx, measurement in enumerate(scaled_measurements):
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=labels[idx])
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title, and custom x-axis tick labels, etc.
ax.set_ylabel('Percent (time is in seconds)')
ax.set_title('Comparison of QA and SA success rates and time taken')
ax.set_xticks(x + width / 2)
ax.set_xticklabels(species)
ax.legend(loc='upper right', title="Method")
ax.set_ylim(0, 150)

plt.show()   