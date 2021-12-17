line = open('input', 'r').readline().rstrip()

packets = bin(int(line, 16))[2:].zfill(4*len(line))

all_packets = []

class Packet:
	def __init__(self, version, type_id, values_or_subpackets):
			self.version = version
			self.type_id = type_id
			if self.type_id == '100': # literal value
					self.values = values_or_subpackets
			else:
					self.subpackets = values_or_subpackets

	def __str__(self):
			if self.type_id == '100': # literal value
				return f'v:{self.version}, t:{self.type_id}, val:{self.values}'
			else:
				return f'v:{self.version}, t:{self.type_id}, s:{self.subpackets}'

	def __repr__(self):
		return self.__str__()		

def slice_list(list, where):
		return list[:where], list[where:]

# packet class, extracts the first relevant packet, and returns the rest of the packets
def process_packet(packet, fixed_size=False):

# [ H E A D E R ]
	start_len = len(packet)
#	print(f'Processing packet: {packet} ', end='')
	version, packet = slice_list(packet, 3)
	type_id, packet= slice_list(packet, 3)
#	print(f'with v:{version} and t:{type_id}')
	values = []
# [ H E A D E R   E N D]
	if(type_id == '100'): # type 4 - literal value
			last_bit = '1'
			while last_bit != '0':
					last_bit, packet = slice_list(packet, 1)
					new_value, packet = slice_list(packet, 4)
					values.append(new_value)
	else: # operator packet
			length_type_id, packet = slice_list(packet, 1)
			if(length_type_id == '0'):
				total_subpackets_len, packet = slice_list(packet, 15)
				total_subpackets_len = int(total_subpackets_len, 2)
				subpackets, packet = slice_list(packet, total_subpackets_len)
#				print(f'found subpackets: {subpackets}')
				while subpackets:
					new_packet, subpackets = process_packet(subpackets, fixed_size=True)
					values.append(new_packet)
	#				print(new_packet, subpackets)
			elif(length_type_id == '1'):
				number_of_subpackets, packet = slice_list(packet, 11)
				number_of_subpackets = int(number_of_subpackets, 2)
				for i in range(number_of_subpackets):
					new_packet, packet = process_packet(packet, fixed_size=True)
					values.append(new_packet)
	if not fixed_size:
		packet_len = start_len - len(packet)
		extra_bits = 4 - (packet_len % 4)
		useless_bits, packet = slice_list(packet, extra_bits)
	all_packets.append(Packet(version, type_id, values))
#	print(f'v:{version}, t:{type_id}, p:{packet}, v:{values}')
	return Packet(version, type_id, values), packet # new packet + what remains unprocessed

def get_version_sum(my_packet):
	if my_packet.type_id == '100':
		return int(my_packet.version, 2)
	else:
		my_sum = int(my_packet.version, 2)
		for pkt in my_packet.subpackets:
			my_sum += get_version_sum(pkt)
		return my_sum
	
def get_value(pkt):
	if pkt.type_id == '100': # is a literal
		dec_value = ''
		for val in pkt.values:
			dec_value += val
		return int(dec_value, 2)
	else: # operator
		s_vals = []
		for p in pkt.subpackets:
			s_vals.append(get_value(p))
		if pkt.type_id == '000': # sum subpackets
			return sum(s_vals)
		elif pkt.type_id == '001': # prod subpackets
			mult = 1
			for a in s_vals:
				mult *= a
			return mult
		elif pkt.type_id == '010':
			return min(s_vals)
		elif pkt.type_id == '011':
			return max(s_vals)
		elif pkt.type_id == '101':
			return 1 if s_vals[0] > s_vals[1] else 0
		elif pkt.type_id == '110':
			return 1 if s_vals[0] < s_vals[1] else 0
		elif pkt.type_id == '111':
			return 1 if s_vals[0] == s_vals[1] else 0

packet, remained = process_packet(packets)
print(get_version_sum(packet))
print(get_value(packet))
