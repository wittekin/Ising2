import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
data = []
f = open("data/raw_positions.txt")
i = 0


def hinton(matrix, i, max_weight=None, ax=None):
	"""Draw Hinton diagram for visualizing a weight matrix."""
	ax = ax if ax is not None else plt.gca()

	if not max_weight:
		max_weight = 2**np.ceil(np.log(np.abs(matrix).max())/np.log(2))

	ax.patch.set_facecolor('gray')
	ax.set_aspect('equal', 'box')
	ax.xaxis.set_major_locator(plt.NullLocator())
	ax.yaxis.set_major_locator(plt.NullLocator())

	for y in range(0,len(data)):
		for x in range(0,len(data[0])):
			color = 'black'
			if data[y][x] > 0.1:
				color = 'white'
			size = 1
			rect = plt.Rectangle([x - size / 2, y - size / 2], size, size,
				             facecolor=color, edgecolor=color)
			ax.add_patch(rect)

	ax.autoscale_view()
	plt.savefig('images/SpinData'+str(i)+'.png', bbox_inches='tight')

    
for line in f:
	if line != "TIME!\n":
		data_aux = []
		for z in line.split():
			data_aux.append(int(z))
		data.append(data_aux)
	else:
		hinton(data,i)
		i+=1
		data = []


	
f.close()





