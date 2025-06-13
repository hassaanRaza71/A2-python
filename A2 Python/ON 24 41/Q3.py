LinkedList=[]
for x in range(20):
    LinkedList.append([-1,x+1])
LinkedList[19][1]=-1
FirstEmpty=0
FirstNode=-1

def InsertData():
    global LinkedList,FirstNode,FirstEmpty
    for x in range(5):
        if FirstEmpty!=-1:
            integer=int(input("Enter an positive integer number: "))
            freelist=FirstEmpty
            FirstEmpty=LinkedList[FirstEmpty][1]
            LinkedList[freelist][0]=integer
            LinkedList[freelist][1]=FirstNode
            FirstNode=freelist


def OutputLinkedList():
    global LinkedList,FirstNode,FirstEmpty
    current_pointer=FirstNode
    while current_pointer!=-1:
        print(LinkedList[current_pointer][0])
        current_pointer=LinkedList[current_pointer][1]
InsertData()
OutputLinkedList()

def RemoveData(data_to_be_removed):
    global LinkedList,FirstNode,FirstEmpty
    current_pointer=FirstNode
    while current_pointer!=-1 and LinkedList[current_pointer][0]==data_to_be_removed:
        previous_pointer=current_pointer
        current_pointer=LinkedList[current_pointer][1]
    if current_pointer==FirstNode:
        FirstNode=LinkedList[current_pointer][1]
    else:
        LinkedList[previous_pointer][1]=LinkedList[current_pointer][1]
    
    LinkedList[current_pointer][0]=-1
    LinkedList[current_pointer][1]=FirstEmpty
    FirstEmpty=current_pointer

RemoveData(5)
print("After")
OutputLinkedList()
