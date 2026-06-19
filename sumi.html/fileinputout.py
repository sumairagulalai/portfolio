# file I/O 
# we can perform operations on differetnt files. using python 
# operations => read,write etc.
# f = open("coding.py","r")
# # two parameters => 1. file name 2. mode 
# data = f.read()
# print(data)
# f.close()
#  read line 
# f = open("coding.py","r")
# data = f.readline()
# print(data)
# data2 = f.readline()
# print(data2)
# write 
# f = open("coding1.py","w")
# data=f.write("my name is sumi")
# print(data)
# f.close()
# f = open("coding1.py","w")
# data=f.write("my name")
# print(data)
# f.close()
# f = open("text.txt","w")
# data=f.write("i am student")
# print(data)
# f.close()
# f = open("coding.py","a")
# data = f.write("my name is sumi")
# print(data)
# f.close()
# f = open("text.txt","w")
# f.write("i am student")
# f.close()
# f = open("a.py","w")
# data=f.write("my name")
# print(data)
# f.close()
# f=open("a.py","a")
# f.write("\n sumi")
# f.close()
# with open("a.py","w+") as f:
#     f.read()
#     f.write("teacher")
#     f.close()
# practice 
# with open("practice.txt","r") as f:
#     data=f.read()
#     newdata=data.replace("python","java")
#     print(newdata)

# with open("practice.txt","w") as f:
#     f.write(newdata)
# search for word 
word = "learning"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find(word)!=-1):
#         print("found")
#     else:
#         print("not found")
    
# other way 
# function check for word
word = "kali"
# with open("practice.txt","r") as f:
#     data = f.read()
#     if word in data:
#         print("found")
#     else:
#         print("not found")

# def check_for_word(word):
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if word in data:
#             print("found")
#         else:
#             print("not found")
# check_for_word("learning")
# check_for_word("way")
# 3 
# count numbers of even numbers in our file 
count = 0
# with open("practice.txt", "r") as f:
#     data = f.read()

# nums = data.split(",")
# for val in nums:
#     if(int(val) % 2 == 0):
#         count += 1

# print(count)

    
    
