class Character:
    #self.__Name string
    #self.__XPosition integer
    #self.__YPosition integer

    def __init__(self,name,xposition,yposition):
        self.__Name=name
        self.__XPosition=xposition
        self.__YPosition=yposition

    def GetXPosition(self):
        return self.__XPosition


    def GetYPosition(self):
        return self.__YPosition

    def SetXPosition(self,Value):
        self.__XPosition+=Value
        if self.__XPosition>10000:
            self.__XPosition=10000
        elif self.__XPosition<0:
            self.__XPosition=0
    
    def SetYPosition(self,Value):
        self.__YPosition+=Value
        if self.__YPosition>10000:
            self.__YPosition=10000
        elif self.__YPosition<0:
            self.__YPosition=0
    
    def Move(self,direction):
        if direction=="up":
            self.SetYPosition(10)
        elif direction=="down":
            self.SetYPosition(-10)
        elif direction=="right":
            self.SetXPosition(10)
        elif direction=="left":
            self.SetXPosition(-10)

Jack=Character("Jack",50,50)

class BikeCharacter(Character):
    def __init__(self, name, xposition, yposition):
        super().__init__(name, xposition, yposition)

    def Move(self,direction):
        if direction=="up":
            super().SetYPosition(20)
        elif direction=="down":
            super().SetYPosition(-20)
        elif direction=="right":
            super().SetXPosition(20)
        elif direction=="left":
            super().SetXPosition(-20)


Karla=BikeCharacter("Karla",100,50)
character_select=input("Which character you would like to move? Jack or Karla: ").lower()
while character_select!="jack" and character_select!="karla":
    character_select=input("Inavlid try again: ")
direction_select=input(f"In which direction do you want to move {character_select}? 'up', 'down', 'left' or 'right': ").lower()
while direction_select!="up" and direction_select!="down" and direction_select!="left" and direction_select!="right":
    direction_select=input("Invalid try again")
if character_select=="karla":
    Karla.Move(direction_select)
    print(f"Karla's new position is X= {Karla.GetXPosition()} Y= {Karla.GetYPosition()}")
else:
    Jack.Move(direction_select)
    print(f"Jacks's new position is X= {Jack.GetXPosition()} Y= {Jack.GetYPosition()}")
