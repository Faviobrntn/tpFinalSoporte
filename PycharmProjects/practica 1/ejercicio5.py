list=[2,2,5,10]

def multList(a):
    res=1
    for num in a:
        res=res*num
    print(res)
    return(res)

multList(list)
