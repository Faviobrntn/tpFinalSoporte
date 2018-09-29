a=input("ingrese caracter")
n=int(input("ingrese numero"))

def generar_n_caracteres(n,a):
    x=''
    for i in range(n):
        x=x+a[:1]
    print(x)
    return(x)

generar_n_caracteres(n,a)
