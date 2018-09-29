a=input("cadena 1")
b=input("cadena 2")

def superposicion(a,b):
    for letter1 in a:
        for letter2 in b:
            if letter1==letter2:
                print("True")
                return("True")
    print("False")
    return("False")


superposicion(a,b)
