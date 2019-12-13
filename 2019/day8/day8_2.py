image = open('input.txt', 'r').read().rstrip()

row = 25
tall = 6
TOTAL_LAYER = row * tall

layers = []
temp_layer = ''

for i in range(len(image)):
	if(i % TOTAL_LAYER == 0):
		layers.append(temp_layer)
		temp_layer = '' + image[i]
	else:
		temp_layer += image[i]

layers.append(temp_layer)		
del layers[0]


image = ['m'] * TOTAL_LAYER

for i in range(TOTAL_LAYER):
	for layer in layers:
		if(layer[i] != '2'):
			image[i] = layer[i]
			break
	
for i in range(len(image)):
	if(i % row == 0):
		print('')
	print(image[i],end='')
print('')

#print(layers)
