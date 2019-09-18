'''
a=int(input("Please enter the value of A"))
b=int(input("Please enter the value of B"))

if a>b:
    c=a*50
    print ("A is greater",c)
else:
    c=b*10
    print ("B is greater",c)
'''

# more than one variable

a= int(input("Please enter the value of A"))
b= int(input("Please enter the value of B"))
c= int(input("Please enter the value of C"))
d= int(input("Please enter the value of D"))

if a>b:
    if a>c:
        if a>d:
            print ("A is greater")
        else:
            print ("D is greater than any value")
    else:
        print ("C is greater than any value")
else:
  if b>c:
     if b>d:
       print ("B is greater")
     else:
        print ("B is not geater than any value")

  else:
      if c>d:
        print ("C is greater")
      else:
          print ("D is greater")
          




        
