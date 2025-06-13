#DECLARE QueueData: ARRAY[1:20] OF STRING
#DECLARE QueueHead,QueueTail : INTEGER
global QueueHead,QueueTail
QueueHead=-1
QueueTail=-1
QueueData=[-1 for _ in range(20)]


def Enqueue(newdata):
    global QueueHead,QueueTail,QueueData
    if QueueTail>20:
        return False
    else:
        if QueueHead==-1:
            QueueTail=0
            QueueData[QueueTail]=newdata
            QueueHead=QueueTail
            return True
        else:
            QueueTail+=1
            QueueData[QueueTail]=newdata
            return True

def Dequeue():
    global QueueHead,QueueTail,QueueData
    if QueueHead==-1:
        return "false"
    else:
        QueueHead+=1
        return QueueData[QueueHead-1]

def StoreItems():
    count=0
    for x in range(10):
        input_string=input("Enter a 7-character string: ")
        product1=int(input_string[:1])*1 + int(input_string[2:3])*1 + int(input_string[4:5])*1
        product2=int(input_string[1:2])*3 + int(input_string[3:4])*3 + int(input_string[5:6])*3
        checkdigit=str(int((product1+product2)/10))
        if checkdigit=="10":
            checkdigit="X"
        if checkdigit==input_string[6:7]:
            input_string=input_string[:6]
            result=Enqueue(input_string)
            if result:
                print("Item is inserted")
            else:
                print("Queue is full")
        else:
            count+=1
    print(count)
StoreItems()
result=Dequeue()
if result=="false":
    print("Queue is empty")
else:
    print(result)



        

