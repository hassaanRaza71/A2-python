def Unknown(X,Y):
    if X<Y:
        print(X+Y)
        return (Unknown(X+1,Y)*2)
    elif Y==X:
        return 1
    else:
        print(X+Y)
        return (int(Unknown(X,Y+1)//2))
    
print(Unknown(10,15))
print(Unknown(10,10))
print(Unknown(15,10))
def IterativeFunction(X,Y):
    result=1
    while X!=Y: 
        if X<Y:
            print(X+Y)
            X+=1
            result=result*2
        else:
            print(X+Y)
            Y+=1
            result=result//2
    return result
