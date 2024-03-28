import os #for file operations

# path="Day38-File Detection/test.txt"
path="Day38-File Detection/testfolder"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("This is a directory")

else:
    print("That location doesnot exists! ")