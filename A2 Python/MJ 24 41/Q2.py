class Tree:
    #__TreeName as String
    #__HeightGrowth as Integer
    #__MaxHeight as Integer
    #__MaxWidth as Integer
    #__Evergreen as String
    def __init__(self,pTreeName,pHeightGrowth,pMaxHeight,pMaxWidth,pEvergreen):
        self.__TreeName=pTreeName
        self.__HeightGrowth=pHeightGrowth
        self.__MaxHeight=pMaxHeight
        self.__MaxWidth=pMaxWidth
        self.__Evergreen=pEvergreen

    def GetTreeName(self):
        return self.__TreeName
    
    def GetGrowth(self):
        return self.__HeightGrowth
    
    def GetMaxHeight(self):
        return self.__MaxHeight
    
    def GetMaxWidth(self):
        return self.__MaxWidth
    
    def GetEverGreen(self):
        return self.__Evergreen
    

def ReadData():
    TreeArray=[]
    try:
        with open("Trees.txt") as Data:
            for line in Data:
                info=line.strip().split(",")
                TreeArray.append(Tree(info[0],int(info[1]),int(info[2]),int(info[3]),info[4]))
            return TreeArray

    except FileNotFoundError:
        print("File not found")

def PrintTrees(tree_object):
    if tree_object.GetEverGreen()=="Yes":
        print(f"{tree_object.GetTreeName()} has a maximum height {tree_object.GetMaxHeight()} a maximum width {tree_object.GetMaxWidth()} and grows {tree_object.GetGrowth()} cm a year. It does not lose its leaves.")
    elif tree_object.GetEverGreen()=="No":
        print(f"{tree_object.GetTreeName()} has a maximum height {tree_object.GetMaxHeight()} a maximum width {tree_object.GetMaxWidth()} and grows {tree_object.GetGrowth()} cm a year. It loses its leaves each year.")

TreeArray=ReadData()
PrintTrees(TreeArray[0])



def ChooseTree(TreeArray):
    input_maxheight=int(input("Enter a required max height of a tree: "))
    input_maxwidth=int(input("Enter a required max width of a tree: "))
    input_evergreen=input("Do you want the tree to be evergreen?\n").lower()
    matching_trees=[]
    for tree in TreeArray:
        if tree.GetMaxHeight()<=input_maxheight and tree.GetMaxWidth()<=input_maxwidth and tree.GetEverGreen().lower()==input_evergreen:
            matching_trees.append(tree)
            PrintTrees(tree)
    if not matching_trees:
        print("No Tree comes under the user requirement")
    input_tree=input("Enter the name of the tree you would like to buy: ")
    input_height=int(input("Enter the height of this tree: "))
    for tree in matching_trees:
        if tree.GetTreeName()==input_tree:
            time=int((tree.GetMaxHeight()-input_height)/tree.GetGrowth())
            print("The tree will take",time,"years to grow to its max height")

ChooseTree(TreeArray)
    



    