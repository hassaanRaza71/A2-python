global Queue
global HeadPointer,TailPointer
Queue=["" for _ in range(50)] #string
HeadPointer=-1
TailPointer=0


def Enqueue(DataToAdd):
    global Queue,HeadPointer,TailPointer
    if TailPointer==50:
        print("Queue is full")
    else:
        Queue[TailPointer]=DataToAdd
        TailPointer+=1
        if HeadPointer==-1:
            HeadPointer=0
def Dequeue():
    global Queue, HeadPointer, TailPointer
    
    if HeadPointer == -1:
        print("Queue is empty")
        return "Empty"
    
    DataRemoved = Queue[HeadPointer]
    
    if HeadPointer == TailPointer:  # If queue becomes empty
        HeadPointer = -1
        TailPointer = 0
    else:
        HeadPointer = HeadPointer + 1  # Circular wrap-around

    return DataRemoved
    

def ReadData():
    with open("QueueData.txt") as Data:
        for line in Data:
            Enqueue(line.strip())
        
class RecordData:
    def __init__(self,id,total):
        self.ID=id #string
        self.Total=total  #integer

global Records,NumberRecords
Records=[RecordData("",0) for _ in range(50)]
NumberRecords=0 #integer

def TotalData():
    global Records,RecordData,NumberRecords
    DataAccessed=Dequeue()
    Flag=False
    if NumberRecords==0:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total=1
        Flag=True
        NumberRecords+=1
    else:
        for x in range(NumberRecords):
            if Records[x].ID==DataAccessed:
                Records[x].Total+=1
                Flag=True
    if not Flag:
        Records[NumberRecords].ID=DataAccessed
        Records[NumberRecords].Total+=1
        NumberRecords+=1
    
def OutputRecords():
    global Records,NumberRecords
    for i in range(NumberRecords):
        print(f"ID {Records[i].ID} Total {Records[i].Total}")

ReadData()
while HeadPointer!=TailPointer:
    TotalData()
OutputRecords()
    
        
