
myfile = open("original.txt")
print(myfile.read())
# print(myfile.readlines(5))

# file cursor
print(myfile.read()) # it won't print , as the cursor already reached the EOF
# instead we can save the content in the variable and print as many times as possible
# content = myfile.read()
# closing a file
myfile.close()

# number of occurances of a character inside the file

def occurances(inputChar, filePath):
    myFile = open(filePath)
    content = myFile.read()
    return content.count(inputChar)


# the better wayy to do the file operations open, read, close is using with
content1 = ""
with open("original.txt") as myfile1:
    content1 = myfile1.read()

print("content1 \n", content1)
# no need of writing close if you are using with

# with open("original.txt", "a+") as myfile1:
#     myfile1.write("\ntomatto")
#     # if you want to print the content
#     print("print inside a+")
#     content = myfile1.read()
#     print(content) # it won't print anything as the cursor already reached the EOF, so to bring it back to the beginning of the file
#     myfile1.seek(0)
#     content = myfile1.read()
#     print(content)
    # 'r'       open for reading (default)
    # 'w'       open for writing, truncating the file first
    # 'x'       create a new file and open it for writing
    # 'a'       open for writing, appending to the end of the file if it exists
    # 'b'       binary mode
    # 't'       text mode (default)
    # '+'       open a disk file for updating (reading and writing)
    # 'U'       universal newline mode (deprecated)


# read and write to the same file

