import os
import math
import json

file_types = [".php", ".c", ".cpp", ".html", ".js", ".css", ".txt", ".c++", ".py"]

def convert_size(size_bytes):
	if size_bytes == 0:
		return "0B"
	size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
	i = int(math.floor(math.log(size_bytes, 1024)))
	p = math.pow(1024, i)
	s = round(size_bytes / p, 2)
	return "%s %s" % (s, size_name[i])

def path_to_dict(path):
	d = {'name': os.path.basename(path)}
	if os.path.isdir(path):
		d['type'] = "directory"
		d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir(path)]
	else:
		d['size'] = convert_size(os.path.getsize(path))
		d['file_type'] = os.path.splitext(path)[1]
		if(d['file_type'] in file_types):
			d['loc'] = sum(1 for line in open(path))
	return d

Subject_dir = input("Enter directory name to parse : ")

with open('MANIFEST.JSON', 'w', encoding='utf-8') as f:
	json.dump(path_to_dict(Subject_dir), f, ensure_ascii=False, indent=4)