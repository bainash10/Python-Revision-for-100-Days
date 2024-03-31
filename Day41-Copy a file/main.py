 #* copyfile() =  copies contents of a file
 #* copy() =       copyfile() + permission mode + destination can be a directory
 #* copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('Day41-Copy a file/test.txt','Day41-Copy a file/using_copy_file.txt') 
shutil.copy('Day41-Copy a file/test.txt','Day41-Copy a file/using_copy.txt') 
shutil.copy('Day41-Copy a file/test.txt','Day41-Copy a file/using_copy2.txt') 
#! 'source','destination'

