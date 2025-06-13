#DECLARE ArrayeNode:2D Array [0:20] FOR INTEGER
#DECLARE RootPointer,FreeNode : INTEGER


ArrayNodes=[[0,0,0] for _ in range(20)]
RootPointer=-1
FreeNode=0

def AddNode(ArrayNodes,RootPointer,FreeNode):
    NodeData=int(input("Enter the data"))
    if FreeNode<=19:
        ArrayNodes[FreeNode][0]=-1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer==-1:
            RootPointer=FreeNode
        else:
            Placed=False
            CurrentNode=RootPointer
            while Placed==False:
                if NodeData< ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2]==-1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        Placed=True
                    else:
                        CurrentNode=ArrayNodes[CurrentNode][2]
        FreeNode=FreeNode+1
    else:
        print("Tree is Full")
    return FreeNode,RootPointer,ArrayNodes

def PrintAll():
    print("LeftPointer    Data    RightPointer")
    for node in ArrayNodes:
        print(f"{node[0]}    {node[1]}    {node[2]}")

for _ in range(10):
    FreeNode,RootPointer,ArrayNodes = AddNode(ArrayNodes, RootPointer, FreeNode)
PrintAll()

def InOrder(ArrayNodes, CurrentNode):
    if CurrentNode == -1:
        return  # Base case: if the current node is -1, do nothing
    # Traverse the left child
    if ArrayNodes[CurrentNode][0] != -1:  # If left child exists
        InOrder(ArrayNodes, ArrayNodes[CurrentNode][0])
    # Print the current node data
    print(str(ArrayNodes[CurrentNode][1]))
    # Traverse the right child
    if ArrayNodes[CurrentNode][2] != -1:  # If right child exists
        InOrder(ArrayNodes, ArrayNodes[CurrentNode][2])
    
if RootPointer != -1:
    print("\nInOrder Traversal:")
    InOrder(ArrayNodes, RootPointer)
else:
    print("\nTree is empty!")





