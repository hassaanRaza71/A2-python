class SaleData:

    def __init__(self,Saleid,quantity):
        self.SaleID=Saleid
        self.Quantity=quantity
    

CircularQueue=[SaleData("",-1) for i in range(5)]
global Head
global Tail
global NumberOfItems
NumberOfItems=0
Head=0
Tail=0

def Enqueue(RecordToAdd):
    global Tail, NumberOfItems, Head
    if NumberOfItems>4:
        return -1
    else:
        CircularQueue[Tail]=RecordToAdd
        if Tail==4:
            Tail=0
        else:
            Tail+=1
        NumberOfItems+=1
        return 1

def Dequeue():
    global Tail, NumberOfItems, Head
    if NumberOfItems==0:
        return CircularQueue[0]
    else:
        RecordRemoved=CircularQueue[Head].SaleID + " " + str(CircularQueue[Head].Quantity)
        NumberOfItems-=1
        if Head==4:
            Head=0
        else:
            Head+=1
    return RecordRemoved

def EnterRecord():
    Id=input("Enter ID")
    quantity=int(input("Enter Quantity"))
    Record=SaleData(Id,quantity)
    result=Enqueue(Record)
    if result==-1:
        print("Full")
    else:
        print("Stored")

for i in range(6):
    EnterRecord()
result=Dequeue()
print(result)
EnterRecord()
for x in range(0, 5):
 print(CircularQueue[x].SaleID, " ", CircularQueue[x].Quantity)


        
