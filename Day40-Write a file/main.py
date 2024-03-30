 #* Default mode is 'r' while opening a file
 #* 'w' is a write mode
 #* 'a' is an append mode


# text="Hello this is Nischal \n Watch my journey! "
# with open('Day40-Write a file/test.txt','w') as file:
#     file.write(text)


# text="This has been overwritten because we opened the file test.txt again in write mode "
# with open('Day40-Write a file/test.txt','w') as file:
#     file.write(text)


text="This will append the file while using the 'a' mode"
with open('Day40-Write a file/test.txt','a') as file:
    file.write(text)


