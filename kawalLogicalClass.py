#logical operator

'''#fixed value
a=20
b=10

if a>b:
    print("A is GT")
else:
    print("B is GT")


#user input    
a=int(input("Please enter the first value"))
b=int(input("Please enter the Second value"))

if a>b:
    
    c=a/b
    print("A is GT",c)
else:
    
    c=a*b
    print("B is GT",c)

'''

a=50
b=40
c=30

if a>b:
    #true part 1
    if a>c:
        print("A is GT")
    else:
        print("C is GT")
else:
    #false part 1
    if b>c:
        print("A is GT")
    else:
        print("C is GT")



#Question B2: WAP to input the age of a person and check that he is eligible for license for not.

age=int(input("please enter the age"))
if age>18:
   print("persion is eligible for licence")
else:
    print("persion is Not eligible for licence")



















            











