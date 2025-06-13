
#DECLARE data: INTEGER
#DECLARE nextNode : INTEGER
class node:
    def __init__(self,Pdata,PnextNode):
        self.data=Pdata
        self.nextNode=PnextNode

linkedlist=[node(-1,-1) for _ in range(10)]
linkedlist[0].data=1
linkedlist[1].data=5
linkedlist[2].data=6
linkedlist[3].data=7
linkedlist[4].data=2
linkedlist[5].data=0
linkedlist[6].data=0
linkedlist[7].data=56
linkedlist[8].data=0
linkedlist[9].data=0
linkedlist[0].nextNode=1
linkedlist[1].nextNode=4
linkedlist[2].nextNode=7
linkedlist[4].nextNode=2
linkedlist[5].nextNode=6
linkedlist[6].nextNode=8
linkedlist[7].nextNode=3
linkedlist[8].nextNode=9
startPointer=0
emptyList=5

def OutputNodes(linkedlist,startPointer):
    print(linkedlist[startPointer].data)
    next_node=linkedlist[startPointer].nextNode
    while next_node!=-1:
        print(linkedlist[next_node].data)
        next_node=linkedlist[next_node].nextNode



def addNode(linkedlist,startPointer,emptyList):
    if emptyList==-1:
        return False
    else:
        newdata=int(input("Enter the new data: "))
        linkedlist[emptyList].data=newdata
        current_pointer=startPointer
        while current_pointer!=-1:
            previous_pointer=current_pointer
            current_pointer=linkedlist[current_pointer].nextNode
        linkedlist[previous_pointer].nextNode=emptyList
        temp=emptyList
        emptyList=linkedlist[emptyList].nextNode
        linkedlist[temp].nextNode=-1
        return True

OutputNodes(linkedlist,startPointer)
result=addNode(linkedlist,startPointer,emptyList)
if result:
    print("New data added in the linked list")
else:
    print("linked list is full")
OutputNodes(linkedlist,startPointer)
        
