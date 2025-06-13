class Node:
    #self.__Data integer
    #self.__RightPointer integer
    #self.__LeftPointer integer
    def __init__(self,data):
        self.__Data=data
        self.__RightPointer=-1
        self.__LeftPointer=-1

    def GetLeft(self):
        return self.__LeftPointer
    
    def GetData(self):
        return self.__Data
    
    def GetRight(self):
        return self.__RightPointer
    
    def SetLeft(self,Value):
        self.__LeftPointer=Value

    def SetRight(self,Value):
        self.__RightPointer=Value

    def SetData(self,Value):
        self.__Data=Value

class TreeClass:
    def __init__(self):
        self.__Tree=[Node(-1) for _ in range(20)]
        self.__FirstNode=-1
        self.__NumberNodes=0
    
    def InsertNode(self, NewNode):
        if self.__FirstNode == -1:
            self.__Tree[self.__NumberNodes] = NewNode
            self.__FirstNode = self.__NumberNodes
            self.__NumberNodes += 1
        else:
            NodeAccess = self.__FirstNode
            Direction = ""

            while NodeAccess != -1:
                Previous = NodeAccess
                if self.__Tree[NodeAccess].GetData() > NewNode.GetData():
                    Direction = "left"
                    NodeAccess = self.__Tree[NodeAccess].GetLeft()
                else:
                    Direction = "right"
                    NodeAccess = self.__Tree[NodeAccess].GetRight()

            if Direction == "left":
                self.__Tree[Previous].SetLeft(self.__NumberNodes)
            else:
                self.__Tree[Previous].SetRight(self.__NumberNodes)

            self.__Tree[self.__NumberNodes] = NewNode
            self.__NumberNodes += 1

    def OutputTree(self):
        if self.__FirstNode!=-1:
            for i in range(self.__NumberNodes):
                print(self.__Tree[i].GetLeft(), " " ,self.__Tree[i].GetData(), " " ,self.__Tree[i].GetRight())
        else:
            print("No Nodes")

TheTree=TreeClass()

TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(7))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()


    

    

        
    