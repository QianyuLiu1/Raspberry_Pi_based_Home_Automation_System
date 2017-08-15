def read():
	mapping={}
	for line in open("pin-config.txt"):  
   		array = line.split(',')
   		mapping[array[0]] = int(array[1])
   	return mapping
