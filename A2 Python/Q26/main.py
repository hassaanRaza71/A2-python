class Character:
    #Private Name String
    #Private XCoordinate Integer
    #Private YCoordinate Integer

    def __init__(self,PName,PXCoordinate,PYCoordinate):
        self.__Name=PName
        self.__XCoordinate=PXCoordinate
        self.__YCoordinate=PYCoordinate

    def GetName(self):
        return self.__Name
    
    def GetX(self):
        return self.__XCoordinate
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate+=XChange
        self.__YCoordinate+=YChange
 
characters=[Character("",0,0) for _ in range(10)]

with open("Characters.txt") as Data:
    for index in range(10):
        name=Data.readline().strip()
        X=int(Data.readline().strip())
        Y=int(Data.readline().strip())
        characters[index]=Character(name,X,Y)

found=False
while not found:
    character_input=input("Enter a Character Name: ").lower()
    count=-1
    for character in characters:
        count+=1
        if character.GetName().lower()==character_input:
            position=count
            found=True
            break
letters="AWSD"
valid=False
while not valid:
    letter=input("Enter a letter to move the charcter. Enter from 'AWSD': ")
    if letter in letters:
        valid=True

if letter=='A':
    characters[position].ChangePosition(-1,0)
elif letter=='W':
    characters[position].ChangePosition(0,1)
elif letter=='S':
    characters[position].ChangePosition(0,-1)
else:
    characters[position].ChangePosition(1,0)

print(f"{characters[position].GetName()} has changed coordinates to X = {characters[position].GetX()} and Y = {characters[position].GetY()}")
