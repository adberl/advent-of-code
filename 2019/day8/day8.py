image = open('input.txt', 'r').read().rstrip()

layers = []
temp_layer = ''

for i in range(len(image)):
	if(i % 150 == 0):
		layers.append(temp_layer)
		temp_layer = '' + image[i]
	else:
		temp_layer += image[i]
		
print(layers)
del layers[0]
layer_id = 0
min_zeroes = 100

for i in range(len(layers)):
	zeroes = 0
	for pixel in layers[i]:
		if(pixel == '0'):
			zeroes += 1
	if(zeroes < min_zeroes):
		min_zeroes = zeroes
		layer_id = i
		
print(layers[layer_id])
ones = 0
twos = 0

for pixel in layers[layer_id]:
	if(pixel == '1'):
		ones += 1
	elif(pixel == '2'):
		twos += 1

print(ones * twos)

