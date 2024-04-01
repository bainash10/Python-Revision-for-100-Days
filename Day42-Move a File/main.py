import os

source="Day42-Move a File/test.txt"
destination="Day42-Move a File/Moved_file_here/moved_test_file.txt"


try:
    if os.path.exists(destination):
        print("There is already a file there")

    else:
        os.replace(source,destination)
        print(source+" was moved")

except FileNotFoundError:
    print(source+" was not found")