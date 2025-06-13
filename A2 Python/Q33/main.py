def IteractiveCalculate(Number):
    ToFind=Number
    Total=0
    while Number!=0:
        if ToFind%Number==0:
            Total+=Number
        Number-=1
    return Total

print(IteractiveCalculate(10))

def RecursiveCalculate(Number,ToFind):
    if Number==0:
        return 0
    else:
        if ToFind%Number==0:
            return Number + RecursiveCalculate(Number-1,ToFind)
        else:
            return RecursiveCalculate(Number-1,ToFind)

print(RecursiveCalculate(10,10))

