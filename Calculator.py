#functions
def add():
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a+b
        print("Addition of {} and {} is : ".format(a,b),c)  

def sub():
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a-b
        print("Subtraction of {} and {} is : ".format(a,b),c)

def mul():
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a*b
        print("Multiplication of {} and {} is : ".format(a,b),c)

def div():
        a=int(input('Enter the 1st number'))
        b=int(input('Enter the 2nd number'))
        c=a/b
        print("Division of {} and {} is : ".format(a,b),c)    

#main function         
print("This Is A Calculator")
while True:
  #options
  print("The Following Task Can Be Done:")
  print("--------------------------------")
  print("Press 1 For Addition")
  print("Press 2 For Substraction")
  print("Press 3 For Muliplication")
  print("Press 4 For Divison")
  print("Press 5 For Calculating Trignometric Ratioes")
  print("Press 6 To Quit")
  print("---------------------------------------------")
  choice=int(input("Please Choose Any"))
  #choice
  if choice == 'Q':
    break;
  elif choice==1:
    add()
  elif choice==2:
    sub()
  elif choice==3:
    mul()
  elif choice==4:
    div()
  elif choice==5:
    trigonometry()  
  else:
    print("Invalid Option")
