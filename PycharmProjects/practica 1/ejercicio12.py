n=int(input("ingrese un numero"))

def sumaN(n):
    total=0
    for num in range(1,n+1):
        total=total+num
    print(total)
    return(total)
sumaN(n)

