a=["hola","cabaña","oso","dinosaurio"]


def masLarga(b):
    palLarga=''
    for palabra in b:
        if len(palabra)>len(palLarga):
            palLarga=palabra
    print(palLarga)
    return(palLarga)

masLarga(a)


