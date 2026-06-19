# function 
# def sum (a,b):
#     sum = a + b 
#     return sum 
# print(sum(6,7))
# print(sum(8,9))
# # average of three numbers 
# def average (a,b,c):
#     ave = (a+b+c)/3
#     print(ave)
# average(6,7,8)
# # print length of list 
# num = [1,2,3,4,5,6]
# def print_items(list):
#     for ele in list:
#         print(ele,end=" ")
# print_items(num)
    
# def print_length(list):
#     print(len(list))
# print_length(num)
# sum of all numbers 
# num = 1
# sum = 0
# for i in range(1,5+1):
#     sum += num
#     num += 1
# print(sum)
# factorial 

# factorial = 1
# for i in range(1,6):
#     factorial*=i
# print(factorial)
# in function 
# def cal_factorial(x):
#     factorial = 1
#     for i in range(1,x+1):
#         factorial*=i
#     print(factorial)
# cal_factorial(6)
# # doller converter 
# def doller_converter(dollar):
#     rupees = 280*dollar
#     print(rupees)
# doller_converter(2)
# user_number = int(input("enter a number"))
# if(user_number%2==0):
#     print("even")
# else:
#     print("odd")

# def detector(user_number):
#     if(user_number%2==0):
#         print("even")
#     else:
#         print("odd")
        
# detector(66)
# sum of n numbers 
# num = 10
# sum = 0
# for i in range(1,num+1):
#     sum += i
# print(sum)
# factorail
# num = 5
# factorial = 1
# for i in range (1,num+1):
#     factorial*=i
# print(factorial)
# def sum_fun(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum+=i
#     print(sum)
# sum_fun(5)
# factorial 
# def factorial_fun(n):
#     factorial = 1
#     for i in range(1,n+1):
#         factorial*=i
#     print(factorial)
# factorial_fun(6)

# recursion 
# def printnum(n):
#     if n == 0:
#         return
#     print(n)
#     printnum(n-1)
# printnum(5)

# def count(n):
#     if n == 0:
#         return
#     print(n)
#     count(n-1)
# count(10)

# factorial 
# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return fact(n-1)*n
# print((fact(5)))
# sum 
def sum_n(n):
    if n == 1:
        return 1
    return sum_n(n-1)+n
print(sum_n(5))


