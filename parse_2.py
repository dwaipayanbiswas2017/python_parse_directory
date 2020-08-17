import glob, os, json

# update the working directory
root_dir = "<working_dir>"

main_dict = dict()
details_dict_list = list()
file_details_list = list()

def parse_dir(directory_name):
	os.chdir(directory_name)

	count = 0
	total_size = 0
	is_total_size_GB = False

	details_dict['Sub_folder_name'] = directory_name.split('/')[-1]

	for file in glob.glob('*.*'):
		file_details = dict()
		get_sizes = os.path.getsize (file)
		if get_sizes < 1000:
			size = str(get_sizes) + 'KB'
		else:
			size = str(round ((get_sizes/(1000*1000)),1)) + 'MB'
		file_name = os.path.basename (file)
		count += 1
		print(str(count)+") File name : "+file_name + "\n\tSize : " + size)

		file_details['file_title'] = file_name
		file_details['file_size'] = size

		file_details_list.append(file_details)

		total_size += float(size[:-2])

	details_dict['files'] = file_details_list

	if(total_size > 1000):
		total_size /= 1000
		is_total_size_GB = True

	total_size = round(total_size, 1)

	if(is_total_size_GB):
		print("Total Number of files : ",count,"\nTotal Size : ",total_size," GB")
		details_dict['total_file_count'] = count
		details_dict['total_file_size'] = str(total_size)+"GB"
	else:
		print("Total Number of files : ",count,"\nTotal Size : ",total_size,"MB")
		details_dict['total_file_count'] = count
		details_dict['total_file_size'] = str(total_size)+"MB"


Subject_dir = input("Enter Main dir name to parse : ")
main_dict['Main'] = Subject_dir

subfolders = [ f.path for f in os.scandir(root_dir+Subject_dir) if f.is_dir() ]
for x in subfolders:
	print("\n\n\t\tScanning directory : "+x+"\n\n")
	details_dict = dict()
	parse_dir(x)
	details_dict_list.append(details_dict)

main_dict["Sub_folders"] = details_dict_list

json_object = json.dumps(main_dict, indent = 4)

with open(root_dir+"files.json", "w") as outfile:
	outfile.write(json_object)

print("Json file dump completed...")
