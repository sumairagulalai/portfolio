# dictionaries 
# student = {
#     "name" : "sumaira",
#     "dept" : "AI",
#     "rollNo" : 8,

# }

# print(type(student))
# print(student["name"])
# student["name"] = "sumi"
# student["section"] = "A"
# student["marks"] = [10,20,30]
# print(student)
# #  creat a dic for book 
# book = {
#     "author" : "alama",
#     "title" : "english",
#     "price" :  200
# }
# print(book["title"])
# # for student 
# stdmarks = {
#     "name" : "ali",
#     "marks" : 30
# }
# if(stdmarks["marks"]>=50):
#     print("passs")
# else:
#     print("fail")
# # empty dic 
# empdic = {}
# empdic["name"]="sara"
# empdic["class"]="five"
# print(empdic)
# # nested 
# student1 = {
#     "name" : "rida",
#     "subjects" : {
#         "math" : 22,
#         "physics" : 33
#     }
# }
# print(student1["subjects"]["math"])



# practice 
# studdic = {
#     "name" : "sumaira",
#     "section" : "A",
#     "subjects" :{
#         "math" : 10,
#         "phy" : 21
#     }
# }
# print(studdic)
# print(studdic["name"])
# studdic["age"] = 21
# print(list((studdic)))
# print(studdic["subjects"]["math"])

# methods 
students = {
    "name" : "sumi",
    "age" : 21,
    "sub" : {
        "math" : 10,
        "physics" : 20
    }
} 
students.update({"age2":21})
print(students)
# res = students.items()
# print(list(res))
# print(students.get("age"))
# res = students.update({"age2":21})
# print(res)
# res = students.values()
# res = students.keys()
# print(tuple(res))
