history = [l.rstrip() for l in open("input").readlines()]

class File():
	def __init__(self, name, parent, mytype, size=0):
		self.name = name
		self.parent = parent
		self.size = size
		self.type = mytype # 0 = dir, 1 = file
		self.children = []
	
	def get_parent(self):
		return self.parent

	def add_child(self, child):
		self.children.append(child)

	def has_child(self, childname):
		for c in self.children:
			if c.name == childname:
				return True
		return False

	def get_child(self, childname):
		for c in self.children:
			if c.name == childname:
				return c		
		print("ERROR ERROR ERROR PARENT DOESNT HAVE CHILD!?!?!?")

	def process_str(self, lvl):
		res = f'{self.name} size:{self.get_size()}{"" if self.type else ":"}\n'
		for c in self.children:
			res += '  '*(lvl+1)
			res += c.process_str(lvl+1)
		return res

	def __str__(self):
		return self.process_str(0)

	def get_size(self):
		if self.type == 1:
			return self.size
		else:
			total_size = 0
			for c in self.children:
				total_size += c.get_size()
			return total_size

root_dir = None
current_dir = None
sizes = {}
for cmd in history:
	size, cmd_name, *filename = cmd.split(' ')
	#print(size, '|', cmd_name, '|', filename)
	if size == '$': # command here
		if(cmd_name) == 'cd':
			filename = filename[0]
			if(filename == '..'):
				current_dir = current_dir.get_parent()
			else:
				#print(filename)
				if current_dir and current_dir.has_child(filename):
					#print(filename)
					current_dir = current_dir.get_child(filename)
				else:
					current_dir = File(filename, current_dir, 0)
				if filename == '/':
					root_dir = current_dir
		else: # ls here
			continue
	else:
		filename = cmd_name
		if size == 'dir':
			current_dir.add_child(File(filename, current_dir, 0))
		else:
			current_dir.add_child(File(filename, current_dir, 1, int(size)))
		#print('file or dir!')

def is_dir(maybe_dir):
	return maybe_dir.type == 0

def add_all_subdir_sizes(my_dir):
	if is_dir(my_dir):
		total = 0
		for c in my_dir.children:
			child_size = c.get_size()
			if is_dir(c):
				add_all_subdir_sizes(c)
			total += child_size
		sizes[my_dir] = total

add_all_subdir_sizes(root_dir)		

final = 0
for v in sizes.values():
	if v <= 100000:
		final += v

#print(sizes)
#print(root_dir)
print(final)

total_disk_space = 70000000
disk_space_needed = 30000000

disk_space_used = sizes[root_dir]
unused_space = total_disk_space - disk_space_used
smallest_needed_delete = disk_space_needed - unused_space

for j in sorted(sizes.values()):
	if j > smallest_needed_delete:
		print(j)
		break
#print(smallest_needed_delete)
