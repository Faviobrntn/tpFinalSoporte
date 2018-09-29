s=input("ingrese una cadena")
b=[0,2,5,4]


def calclong(s):
    if (type(s)==str or type(s)==list):
        print(len(s))
        return(len(s))

calclong(s)
calclong(b)
