line = open('input', 'r').readline().rstrip()

packets = bin(int(line, 16))[2:].zfill(4*len(line))

all_packets = []

class Packet:
    def __init__(self, version, type_id, value_or_subpackets):
        self.version = version
        self.type_id = type_id
        if self.typeId == '100': # literal value
            self.value = int(value_or_subpackets, 2)
        else:
            self.subpackets = value_or_subpackets

    def __str__(self):

        return


def slice_list(list, where):
    return list[:where], list[where:]

# packet class, extracts the first relevant packet, and returns the rest of the packets
def process_packet(packet):
    # process header
    start_len = len(packet)
    version, packet = slice_list(packet, 3)
    type_id, packet= slice_list(packet, 3)
    if(type_id == '100'): # type 4 - literal value
        last_bit = '1'
        values = []
        while last_bit != '0':
            last_bit, packet = slice_list(packet, 1)
            new_value, packet = slice_list(packet, 4)
            values.append(new_value)
    else:
        pass
    packet_len = start_len - len(packet)
    extra_bits = 4 - (packet_len % 4)
    useless_bits, packet = slice_list(packet, extra_bits)
    all_packets.a
    print(f'v:{version}, t:{type_id}, p:{packet}, v:{values}')


print(packets)
process_packet(packets)