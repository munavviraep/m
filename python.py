# a=90
# b=95
# c=99
# total=a+b+c
# average=total/3
# percentage=total/300*100
# print(total)
# print(average)
# print(percentage)


# 
# x=5
# print(type(x))
# x=5.4
# print(type(x))
# x="hello"
# print(type(x))
# x=True
# print(type(x))
# x=None
# print(type(x))
# x=input()
# print(type(x))
# 


# name=input("enter the name")
# x=int(input("enter the mark in maths"))
# y=int(input("enter the mark in science"))
# z=int(input("enter the mark in english"))
# total=x+y+z
# average=total/3
# percentage=total/300*100
# print(total)
# print(average)
# print(percentage)


# age=int(input("enter your age"))
# if(age>=18):
#    print("eligible")
# else:
#    print("not eligible")


# x=int(input("enter a number"))
# print(x)
# if (x%2==0):
#    print("even")
# else:
#    print("odd")   
  

# a=int(input("enter a number"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# print(a,b,c)
# if a>b and a>c:
#     print("a is the largest")
# elif b>a and b>c:
#     print("b is the largest")
# elif c>a and c>b:
#     print("c is the largest")
# else:
#     print("all are equal")            


# x=float(input("enter a number"))
# print(x)
# if (x>0 and x<8):
#     print("kids")
# elif (x>9 and x<12):
#     print("junior")    
# elif (x>13 and x<19):
#     print("teenager")
# elif (x>20 and x<50):
#     print("adult")
# else:
#     print("senior")           


# a=int(input("enter anumber"))
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# d=int(input("enter a number"))
# print(a,b,c,d)
# if (a>b and a>c and a>d):
#     print("a is the largest")
# elif (b>a and b>c and b>d):
#     print("b is the largest")
# elif (c>a and c>b and c>d):
#     print("c is the largest")
# elif (d>a and d>b and d>c):
#     print("d is the largest")
# else:
#     print("all are equal")  



# name=input("enter the name")
# x=int(input("enter the mark in maths"))
# y=int(input("enter the mark in science"))
# z=int(input("enter the mark in english"))
# print(x,y,z)
# total=x+y+z
# average=total/3
# percentage=total/300*100
# print(total)
# print(average)
# print(percentage)
# if (x>45 and y>45 and z>45):
#     print("mr munna is pass")
# elif (x<45 and y<45 and z<45):
#     print("mr munna is fail")
# else:
#     print("none")    

#how
# for i in range (1,11):
#     print(i)



# for i in range(1,101):
#     if i%2==0:
#         print(i)


# i=1
# while i <= 10:
#     print(i)
#     i += 1

 

# i=1
# while 1<=10:
#     if i % 2==0:
#        print(i)
#     i += 1    


# def add_numbers (a,b):
#          return a+b
# result = add_numbers(3,2) 
# print("the sum is",result)


# def celsius_to_fahrenheit(celsius):
#     fahrenheit= (celsius * 9/5) + 32
#     return fahrenheit
# celsius_val = 25
# fahrenheit_val = celsius_to_fahrenheit(celsius_val)
# print(f"{celsius_val} degreecelsius is equal to {fahrenheit_val} degreefahrenheit")


# def sum_of_primes(limit):
#     prime_sum = 0  
#     for num in range(2, limit + 1):
#         if all(num % i !=0 for i in range(2, int(num**0.5) + 1)):
#             prime_sum += num
#     return prime_sum
# print(f"the sum is:{sum_of_primes(100)}")        


# num=5
# count=0
# for factor in range (1,num+1):
#     if num %factor==0
#     count = count + 1
#     if count==2:
#         print("prime")
#     else:
#         print("not prime")
# # range =100
# def sum_of_primes(limit):
#     list=[]
#     sum=0
#     for number in range (1,range+1):
#         count=0
#         for factor in range (1,number+1):
#             if number%factor == 0:
#                count = count + 1
#             if count==2:
#                 list_append (number)
#                 sum=sum+number
#     return sum_of_primes
# print("sum",) 
            
# x=lambda a,b: a+b
# print(x(2,3))
 
# x=lambda a: a**0.5
# print(x(4))

# x=lambda a: "even" if a%2==0 else "odd"
# print(x(4))


# x=lamda a:

# class Student:
#        def __init__(self,name,age,mark):
#            self.name=name
#            self.age=age
#            self.mark=mark
       
# s1= Student("john",21,84)
# s2= Student("james",23,94)
#print(s1.name,s1.age,s1.mark)
#print(s2.name,s2.age,s2.mark)



# 

# class Car:
#   def __init__(self, brand, model, year):
#     self.brand = brand
#     self.model = model
#     self.year = year

#   def display_info(self):
#     print(f"{self.year} {self.brand} {self.model}")

# car1 = Car("Toyota", "Corolla", 2020)
# car1.display_info()


# class Person:
#   def __init__(myobject, name, age):
#     myobject.name = name
#     myobject.age = age

#   def greet(abc):
#     print("Hello, my name is " + abc.name)

# p1 = Person("Emil", 36)
# p1.greet()

class Student:
       def __init__(self,name,age,mark):
           self.name=name
           self.age=age
           self.mark=mark
       def info (self):
             return f"my name is {self.name} and my age is {self.age} and my mark is {self.mark}"   
s1= Student("john",21,84)
s2= Student("james",23,94)
print(s1.name,s1.age,s1.mark)
print(s2.name,s2.age,s2.mark)
print(s1.info())
print(s2.info())