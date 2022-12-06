signal = open("input").readlines()[0].rstrip()

#pkt_size = 4
pkt_size = 14
for i in range(0, len(signal)-pkt_size):
	pkt = signal[i:i+pkt_size]
	if (len(set(pkt)) == pkt_size):
		print(f'start of msg (size: {pkt_size}): ', i+pkt_size)
		break
	#print(signal[i:i+pkt_size])