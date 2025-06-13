class HiddenBox:
    #Private BoxName String
    #Private DateHidden String
    #Private Creator String
    #Private GameLocation String
    #Private LastFinds [10][2] String
    #Private Active Boolean
    def __init__(self,boxname,creator,datehidden,gamelocation):
        self.__BoxName=boxname
        self.__Creator=creator
        self.__DateHidden=datehidden
        self.__GameLocation=gamelocation
        self.__LastFinds=[]
        self.__Active=False

    def GetBoxName(self):
        return self.__BoxName
    def GetGameLocation(self):
        return self.__GameLocation
    
TheBoxes=[HiddenBox("","","","") for _ in range(10000)]

def NewBox():
    global TheBoxes
    input_name=input("Enter Box Name: ")
    input_creator=input("Enter Player Name: ")
    input_datehidden=input("Enter the Date when box was created: ")
    input_gamelocation=input("Enter the location of the box: ")
    Box_Created=HiddenBox(input_name,input_creator,input_datehidden,input_gamelocation)
    TheBoxes.append(Box_Created)

NewBox()
    
class PuzzleBox(HiddenBox):
    #Private PuzzleText String
    #Private Solution String
    def __init__(self, boxname, creator, datehidden, gamelocation,NewPuzzleText,NewSolution):
        super().__init__(boxname, creator, datehidden, gamelocation)
        self.__PuzzleText=NewPuzzleText
        self.__Solution=NewSolution
