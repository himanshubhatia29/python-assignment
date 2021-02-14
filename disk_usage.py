	
# importing shutil module 
import shutil 

# disk Path 
path = "D://"

# Get the disk usage 
stat = shutil.disk_usage(path) 

# Print disk usage data 
print("Disk usage data:") 
print(stat) 
