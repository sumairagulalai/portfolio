# # class 
# class std:
#     name = "sumi"
# s1 = std()
# res = s1.name
# print(res)
# # cars 
# class cars:
#     color = "blue"
#     name = "mercedes"
# car1 = cars()
# print(cars.color)
# constructor 
# class student:
#     def __init__(self,fullname,marks):
#         self.name=fullname;
#         self.marks=marks;
# s1 = student("khan",11)
# print(s1.name)
# print(s1.marks)
# class std():
#     clgname = "abc"
#     cls = "five"
#     def __init__(self,marks,nic):
#         self.marks=marks
#         self.nic = nic
        


# s1 = std(33,17101)
# print(s1.marks,s1.nic)

# class cars():
#     company = "BMW"
#     def __init__(self,name,color):
#      self.carname=name
#      self.color=color

# car1=cars("cultus","black")
# print(car1.color)

# class std:
#     dept = "AI"
#     uni = "agriculture"
#     def __init__(self,name,rollno,marks):
#         self.name=name
#         self.rollno=rollno
#         self.marks=marks
#     def welcome(self):
#         print("welcom",self.name)
#     def get_marks(self):
#         return self.marks

# s1=std("khan",1,22)
# print(s1.name)   
# s1.welcome()    
# s2=std("sumi",2,11)
# s2.welcome()
# s2.get_marks()

# methods 
# # practice 
# class student:
#     @staticmethod
#     def hello():
#             print("hello")
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3
        
#     def cal_aveg(self):
#         sum=(self.marks1+self.marks2+self.marks3)
#         aveg=sum/3
#         print("hello",self.name,"your average score is",aveg)

# s1=student("khan",90,91,92)
# s1.cal_aveg()
# s1.hello()
    
# # abstraction 
# class car:
#     def __init__(self):
#         self.engine=False
#         self.brk=False
#     def start(self):
#         self.engine=True
#         self.brk=True
#         print("car started...")
        
# car1=car()
# car1.start()
# # practice 

# class account:
#     def __init__(self,acc,accno):
#         self.account=acc
#         self.accountno=accno
#     def debit(self,amount):
#         self.account-=amount
#         print("debited",amount)
#         print(self.get_account())
#     def credit(self,amount):
#         self.account+=amount
#         print("credted",amount)
#         print(self.get_account())
#     def get_account(self):
#         print(self.account)

# acc1=account(1000,1234)
# print(acc1.account)
# acc1.debit(200)
# acc1.credit(400)

# bank account 
# # encapsulation 
# class bank_acc:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no
#     def credit(self,amount):
#         self.balance += amount
#         # print(self.get_amount)
#     def debit(self,amount):
#         self.balance-=amount
#         # print(self.get_amount)
#     def get_amount(self):
#         print(self.balance)

# user1=bank_acc(10000,123)
# print(user1.balance)
# user1.credit(200)
# print(user1.balance)
# user1.debit(300)
# print(user1.balance)


# # delete an object 
# class car:
#     def __init__(self,name):
#         self.name=name
# car1=car("corolla")
# # print(car1.name)
# del car1

# # making private attribute 
# class person:
#     def __init__(self,name):
#         self.__name=name

# person1=person("sumi")
# print(person1.name)
# practice 
# 1. abstraction 
# 2. encapsulation 
# 3.delting object 
# 4. making private attribute 
# 5. static method 