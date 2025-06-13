class Queue:
    def __init__(self):
        self.QueueArray=[-1 for _ in range(100)]
        self.HeadPointer=-1
        self.TailPointer=0
TheQueue=Queue()

def Enqueue(TheQueue,TheData):
    if TheQueue.HeadPointer==-1:
        TheQueue.QueueArray[TheQueue.TailPointer]=TheData
        TheQueue.HeadPointer=0
        TheQueue.TailPointer+=1
        return 1
    elif TheQueue.TailPointer>99:
        return -1
    else:
        TheQueue.QueueArray[TheQueue.TailPointer]=TheData
        TheQueue.TailPointer=TheQueue.TailPointer+1
        return 1
def ReturnAllData():
    global TheQueue
    values_string=""
    for index in range(TheQueue.HeadPointer,TheQueue.TailPointer+1):
        if TheQueue.QueueArray[index]==-1:
            continue
        values_string+=str(TheQueue.QueueArray[index]) + " " 
    return values_string

for _ in range(10):
    correct_input=False
    while not correct_input:
        value=int(input("Enter an integer value: "))
        if value>=0:
            correct_input=True
            result=Enqueue(TheQueue,value)
            if result==-1:
                print("The Queue is Full")
            else:
                print("The data item has been added to the queue")
print(ReturnAllData())

def Dequeue():
    global TheQueue
    if TheQueue.HeadPointer==-1:
        return -1
    else:
        Data_removed=TheQueue.QueueArray[TheQueue.HeadPointer]
        TheQueue.HeadPointer+=1
        return Data_removed
for _ in range(2): 
    result=Dequeue()
    if result==-1:
        print("Queue empty")
    else:
        print(result)

print(ReturnAllData())


