def max(a,b,c):
    if (a>=b and a>=c):
        print(a)
        return(a)
    elif (b>=a and b>=c):
        print(b)
        return(b)
    elif (c>=a and c>=b):
        print(c)
        return(c)


num1=int(input("numero 1"))
num2=int(input("numero 2"))
num3=int(input("numero 3"))
max(num1,num2, num3)

