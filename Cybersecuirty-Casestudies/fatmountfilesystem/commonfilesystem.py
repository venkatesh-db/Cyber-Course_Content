

# fat32  common usb file system 
# ntfs windows external drives 
#ext4 linux partions 


logs=[
    "timestamp=10:10 host =server1 process=mount device=/dev/sdb1 filesystem=fat32 path=/mnt/usb",
    "timestamp=10:15 host =server1 process=mount device=/dev/sdb1 filesystem=ntfs path=/mnt/usb",
    "timestamp=10:20 host =server1 process=mv source=/dev/customer.db dest=/mnt/usb/customer.db",
]

mounteddevice=None
filesystem=None
supicious_move=[]

for log in logs:
    
    if "process=mount" in log:

       if "filesystem=fat32" in log:
           
          mounted_device= log.split("device=")[1].split()[0]
          filesystem="fat32"
          mount_path= log.split("path=")[1]
          
          print(f"Mounted device: {mounted_device} with filesystem: {filesystem} at path: {mount_path}")
          
          
    elif "process=mv" in log:
        
        supicious_move.append(log)
        
        
if supicious_move:
    
    for move in supicious_move:
      
      print("suspicious move detected:", move)