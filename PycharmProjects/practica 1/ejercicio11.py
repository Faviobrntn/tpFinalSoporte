n=input("numero:")

def cantDigitos(a):
    c=0
    for numero in a:
        if (numero in '0123456789'):
            c+=1
    print(c)
    return(c)

cantDigitos(n)
