__descriptions = {
	'B': "Uninitialized data (global)",
	'b': "Uninitialized data",
	'D': "Initialized data (global)",
	'd': "Initialized data",
	'G': "Initialized small objects (global)",
	'g': "Initialized small objects",
	'i': "Indirect functions",
	'I': "Indirect references",
	'N': "Debugging symbols",
	'P': "Stack unwind symbols",
	'R': "Read-only data (global)",
	'r': "Read-only data",
	'S': "Unintialized small objects (global)",
	's': "Uninitialized small objects",
	'T': "Code (global)",
	't': "Code",
	'U': "Undefined",
	'u': "Unique global symbols",
	'V': "Weak objects",
	'v': "Weak objects",
	'W': "Weak symbols",
	'w': "Weak symbols",
	'-': "stabs symbols",
	'?': "Unknown symbols"
}

def get_types():
	return __descriptions.keys()

def get_description_for_type(type_letter):
	try:
		return __descriptions[type_letter]
	except:
		return "Unknown symbol"

def get_ram_symbols():
	return ['B', 'b', 'D', 'd']

def get_flash_symbols():
	return ['T', 't']