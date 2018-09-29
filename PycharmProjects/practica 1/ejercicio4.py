
a=(input("ingrese letra"))

def esVocal(a):
    print(a[:1].lower() in 'aeiou')
    return(a[:1].lower() in 'aeiou')

esVocal(a)
