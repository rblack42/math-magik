import hashlib

def get_hash(file_name):
    """Generate hash code for file path"""
	data = '' = 0
	try:
		with open(file_name) as fin:
    		data = fin.read()
	except:  # pragma: no cover
		pass
    hash = hashlib.md5(data).hexdigest()
	return hash


