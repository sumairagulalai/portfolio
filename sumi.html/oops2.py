# inheritence 
# get properties from parent class 
# class parent:
#     def motherskill(self):
#         print("cooking")
#     def fatherskill(self):
#         print("driving")
# class child(parent):
#     pass
# child1class car:
# =child()
# child1.motherskill()
# child1.fatherskill()

# # multilevel inheritence 
# class car:
#     @staticmethod
#     def start():
#         print("car started")
#     def stop():
#         print("car stoped")
# class toyota(car):
#     def __init__(self,brand):
#         self.brand=brand
# child1=toyota("good")
# child1.start()
# print(child1.brand)

# # multiple inheritence 
# class mother():
#     skill1 = "cooking"
# class father():
#     skill2 = "driving"
# class child(mother,father):
#     pass
# child1=child()
# print(child1.skill1)
# print(child1.skill2)

# super function 
# class parent:
#     def __init__(self,name):
#      self.name=name
# class child(parent):
#     def __init__(self,dep,name):
#         super().__init__(name)
#         self.dep=dep
# ch1=child("AI","sumi")
# print(ch1.name)

# static method 
# class method 
# 1. static methd 
# class pra:
#     @staticmethod
#     def skill():
#         print("cooking")
# child=pra()
# child.skill()

# 2. class method 
# is used to change the data and variable inside the class 
class std:
    name="sumi"
    @classmethod
    def change_name(cls,name):
        cls.name=name
s1=std()
print(s1.name)
s1.change_name("khan")
print(s1.name)
print(std.name)
