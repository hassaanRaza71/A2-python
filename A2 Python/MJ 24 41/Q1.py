#DECLARE DataStored:ARRAY [1:20] OF INTEGER
#NumberItems : INTEGER
global DataStored,NumberItems
DataStored=[]


def Intiialise():
    global DataStored,NumberItems
    current_input=False
    while not current_input:
        quantity=int(input("Enter the quantity of number you would like to enter between 1 and 20 inclusive: "))
        if quantity>=0 and quantity<=20:
            current_input=True
    for _ in range(quantity):
        num=int(input("Enter an integer: "))
        DataStored.append(num)
        NumberItems+=1

NumberItems=0
Intiialise()
print(DataStored)

def BubbleSort():
    global DataStored,NumberItems
    for x in range(NumberItems):
        for y in range(NumberItems-1-x):
            if DataStored[y]>DataStored[y+1]:
                temp=DataStored[y]
                DataStored[y]=DataStored[y+1]
                DataStored[y+1]=temp
BubbleSort()
print(DataStored)

def BinarySearch(DataToFind):
    global DataStored,NumberItems
    top=0
    bottom=NumberItems-1
    while bottom>=top:
        mid=int((top+bottom)/2)
        if DataStored[mid]==DataToFind:
            return mid
        elif DataStored[mid]>DataToFind:
            bottom=mid-1
        else:
            top=mid+1
    return -1


num=int(input("Enter a number: "))
print(BinarySearch(num))



    




