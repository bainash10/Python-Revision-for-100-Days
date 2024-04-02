import os
import shutil

# path="Day43-Delete a file/test.txt"
# os.remove(path)

#! Createing code for exception handlings

path="Day43-Delete a file/test.txt"
# path="Day43-Delete a file/empty_dir" #* for folders named empty_dir

try:
    os.remove(path) #* for files
    # os.rmdir(path) #* wont delete folders with files in it
    # shutil.rmtree(path)  #* This is a very dangerous code, it can delete folders easily that contains files, so use it wisely


except FileNotFoundError:
    print("This file was not found")

except PermissionError:
    print("You do not have permission to delete that")

except OSError:
    print("You cannot delete that folder using that function")

else:
    print(path+" was deleted")