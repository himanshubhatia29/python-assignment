import os 
print("Directory entry name and their inode number") 
with os.scandir(path) as itr: 
	for entry in itr : 
		if not entry.name.startswith('.') : 
			print(entry.name, " :", entry.inode()) 
