
'''x= int(input("please given the value for loop limit"))
for i in range(0,x):
    print(i)
    

for r in range(0,5):  
    print()  
    for c in range(0,r+1):  
        print("*",end="")




for i in range(0,10):
    print(i)
    if i==6:
        #break;
        continue;


 

i=0
while(i<10):
    print(i)
    i=i+1

    
 '''       
    
#function


#10 +20
#30+40



''' function
            four types of function
             =>no arguments no return.
             =>with arguments no return
             =>with arguments with return
             =>no arguments with return

      arguments: argumments is a value which is given by user on run time
      return:after terminate/complete the proccess then given some out put

      '''

# basic structure of any function

''' def functionName(arguments1,arguments2....):
            logic

            return ;

'''


# no arguments no return function

#Create a function

def show():
    print("Hello Kawal Good Morning")



#use/call a function    

show()
show()
show()
show()


#with arguments no return

def add(a,b):
    c= a+b
    print("add value of",a,"and", b , "=" ,c)



add(20,30)

add(30,30)

add(40,30)


#with arguments with return


def addByvalue(a,b,c):
    d=(a+b)/c
    return d;



print(addByvalue(20,50,2))

returnValue=addByvalue(20,50,2)
print(returnValue)

#no arguments with return


def gm():
    x="Good Morning"
    return x




print("hi Kumar",gm())
























    
    
