NumberArray=[100,85,644,22,15,8,1]

def RecursiveInsertion(IntegerArray,NumberElements):
    if NumberElements<=1:
        return IntegerArray
    
    RecursiveInsertion(IntegerArray,NumberElements-1)
    LastItem=IntegerArray[NumberElements-1]
    CheckItem=NumberElements-2
    LoopAgain=True
    if CheckItem<0:
        LoopAgain=False
    else:
        if IntegerArray[CheckItem]<LastItem:
            LoopAgain=False

    while LoopAgain:
        IntegerArray[CheckItem+1]=IntegerArray[CheckItem]
        CheckItem-=1
        if CheckItem<0:
            LoopAgain=False
        else:
            if IntegerArray[CheckItem]<LastItem:
                LoopAgain=False

    IntegerArray[CheckItem+1]=LastItem
    return IntegerArray
SortedArray=RecursiveInsertion(NumberArray,len(NumberArray))
print("Recursive",SortedArray)

def IterativeInsertion(NumberElements):
    NumberArray=[100,85,644,22,15,8,1]
    for x in range(1,NumberElements):
        LastItem=NumberArray[x]
        TempPointer=x
        while TempPointer>0 and NumberArray[TempPointer-1]>LastItem:
            NumberArray[TempPointer]=NumberArray[TempPointer-1]
            TempPointer-=1
        NumberArray[TempPointer]=LastItem
    return NumberArray
Sorted2Array=IterativeInsertion(len(NumberArray))
print("Iterative",Sorted2Array)

def BinarySearch(IntegerArray,First,Last,ToFind):
    if First>Last:
        return -1
    else:
        Middle=int(((First+Last)/2))
        if IntegerArray[Middle]==ToFind:
            return Middle
        elif IntegerArray[Middle]>ToFind:
            return BinarySearch(IntegerArray,First,Middle-1,ToFind)

        else:
            return BinarySearch(IntegerArray,Middle+1,Last,ToFind)

result=BinarySearch(Sorted2Array,0,6,644)
if result==-1:
    print("Not Found")
else:
    print(result)