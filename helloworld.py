
# #WAP to find the data types
# #can you perform the addition of string and integer
# #WAP to find the ascii value of afno naam.
# #wap to addition of first 20 numbers
# #WAP to show usecase of boolean data 
# #typeprint("hello from restart")
# #WAp to take input from the user and render hello + afno naam
# #WAP to print hello world 1000 timesin new line
# #wap to convert string data type to int

# # y = "Hello world"

# # print(type(y))

# # x,y,z="orange","apple","guava"

# # print(x,y,z)

# # fruits=["apple","banana","cherry"]

# # a,b,c = fruits
# # print(a,b,c)


# # for x in range(10):

# #     print("Hello",x)



# #can you perform the addition of string and integer

# # myStr="Dharmendra"
# # # MyInt=5
# # # print(myStr+MyInt)
# # myName=['d','h','a','r','m','e','n','d','r','a']

# # for x in range(9):
# #     print(ord(myName[x]))

# # #wap to addition of first 20 numbers
# # add = 0
# # for x in range(20):
        
# #         add=add+x
# #         print(add)

# # #usecase of boolean value

# # print(99>100)
# # a = 210
# # b = 22

# # if b > a:
# #   print("b is greater than a")
# # else:
# #   print("b is not greater than a")

# #WAp to take input from the user and render hello + afno naam
# # greet="hello"

# # username = input("enter username ")
# # print(greet +" "+ username)

# #wap to convert string data type to int

# # mygreettoint = int(greet)
# # print(type(mygreettoint))
# # a=6
# # b=5
# # print("{a} is greater than {b}")

# #WAP to show usecase of combination of return value and argument types

# #no argument no return types

# def greeting():
#   print("hello")

# greeting()

# #no argument with return types

# def multiply():
#     print("the value of multiplication is 5*5 is")
#     return 5*5

# print(multiply())

# #with argument no return type

# def greet(a):
#     # print("hello mr'"+a+"'")
#      print(f"hello mr.{a}")

# greet("dharmendra")

# #with argument with return type
# def add(a, b, c, d):
#       sum=a+b+c+d
#       return print(f"the added value is {sum}")

# add(2,3,4,5)

#wap to print even numbers between 2 and 50 also perform addition of those even numbers
# add = 0
# for x in range (2,51):
#   if(x%2==0):
#     print(x)
#     add =add+x
# print(f"the added value is {add}")

#WAP to print prime numbers

# print("enter the number")
# x = input()
# flag = False
# if x==1:
#     print("the number is not prime")
# elif x>1:
#     for i in range(2,x):
#       if(x%i==0):
#         flag= True
#         break
#     if flag:
#        print(x,"it is not prime")
#     else:
#       print(x,"it is prime")

# Program to check if a number is prime or not

# num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

    # check if flag is True
    # if flag:
    #     print(num, "is not a prime number")
    # else:
    #     print(num, "is a prime number")

# userName = input("enter the name")
# favColor = input("enter the fav color")
# print(f"hi {userName}! your favourite color is {favColor} ")

# sentence = input("enter the sentence")
# splittedby = sentence.split(" ")
# print(splittedby)
# print(len(splittedby))

# 

# inputName = input("enter the name")
# replacetxt = inputName.replace("hello","hi")
# print(replacetxt)
# my_list = ["mango","litchi","tomato","medicine"]

# my_list.append("potato")
# my_list.remove("litchi")
# print(my_list)

# numbers = [1,3,5,7,9]
# print(numbers[1])

# numbers[3]=10
# print(numbers)

# numbers.append("12")
# print(numbers)

# numbers.remove(5)
# print(numbers)

# sliced_list=numbers[2:4]
# print(sliced_list)

# combined_list=numbers+sliced_list
# print(combined_list)

# print(8 in combined_list)

#  combined_list.sort()
# print(combined_list.sort())

# txt = "my name is {1},i m {0}".format("john",36)
# txt = "my name is {1},i m {0}"
# print(txt)

# for  x in "mango":
#     print(f"{x}\n")

# myList =[2,3,4,5,6]
# myList.sort()


# tuple  


# my_tuple=(1,1,2,3,4)
# print(my_tuple[0])
# print(type(my_tuple))
# count1 = sorted(my_tuple)
# print(type(count1))

# my_tuple = (10,20,'a','b','true')
# print(my_tuple)

# my_tuple = (10,20,'a','b','true')
# print(my_tuple[2])

# tuple1 =  (1,2,3)
# tuple2 = ('x','y','z')
# concatenated_tuple = tuple1+tuple2
# print(tuple)

# threeX_tuple = my_tuple*3
# print(threeX_tuple)

# print(len(concatenated_tuple))
# sliced_tuple=my_tuple[2:]

# print(sliced_tuple)


#dictionary is a associated array

# my_Dict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year" : 1964

# }

# print(my_Dict.items())

# for x in my_Dict:
#     print(my_Dict[x])


# WAP to show multiplication table of 1st 20 prime numbers using nested for loop


# flag = False
# num =3
# Mlist=[]
# if num == 1:
#      print(num, "is not a prime number")
# elif num > 1:
     
#      for i in range(2,num):
#          if (num % i) == 0:
#              flag = True
            
             
#              break
         
      

     
#      if flag:
#          print(num, "is not a prime number")
         
#      else:
#          print(num, "is a prime number")
#          Mlist.append(num)
#          num = num+1

# def is_prime(number):
#      if number<2:
#           return False
#      for i in range(2,int(number**0.5)+1):
#             if number%i == 0:
#                 return False
#             return True
# count = 0
# number=1
# prime_list=[]
# while count<20:
#     if is_prime(number):
#             prime_list.append(number)
#             count = count+1
#     number = number+1
    
# print(prime_list)
# print(len(prime_list))

# list = []

# for j in range(20,30):
#     prime = 1
#     for i in range(2,j):
#          if j%i==0:
#             prime=0
#             break
#     if prime == 1:
#          list.append(j)
# print(list)

#wap to find Simple interest, perimeter of rectangular ground,
#to find volume of irregular body,to calculate volume of cube
#to find sqareroot of a number

#WAP to find error percentage

# x = int(input("enter the observe value"))
# y = int(input("enter the obtained value"))
# print(type(x)) 

# z = abs(x-y)
# errorpercentage = z/y*100
# print("the error percentage is",errorpercentage)

# wap take a string from user as a input and check whether the string is  rishab karki or not

inString = input("enter the string")
if(inString=="Rishab"):
    print("positive")