import json

def get_value(name):
	'''Get the value from a json config file
		# Args:
			name: name of key
	'''
    with open('config.json', 'r') as f:
        config = json.load(f)
    
		return config[name]
