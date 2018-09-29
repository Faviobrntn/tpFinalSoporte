num=int(input("ingrese numero"))

def esPrimo(c):
    for i in range(2,c):
        if c%i==0:
            print("no es primo")
            return ("false")
    print("True")
    return("true")

esPrimo(num)

