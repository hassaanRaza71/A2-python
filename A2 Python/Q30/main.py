import datetime
class Character:
    # CharacterName as STRING
    # DataOFBirth as DATE
    # __ as REAL
    # __ as INTEGER
    def __init__(self, charactername, dateofbirth, intelligence, speed):
        self.__CharacterName = charactername
        self.__DateOfBirth = dateofbirth
        self.__Intelligence = intelligence
        self.__Speed = speed
    def GetIntelligence(self):
        return self.__Intelligence
    
    
    def GetName(self):
        return self.__CharacterName

    
    def SetIntelligence(self,Value):
        self.__Intelligence=Value
    
    
    def Learn(self):
        self.__Intelligence=self.__Intelligence + self.__Intelligence*0.1
    def ReturnAge(self):
        Year=self.__DateOfBirth.year
        return 2023-Year
# Creating an instance
FirstCharacter = Character("Royal", datetime.datetime(2019, 1, 1), 70, 30)

# Calling the Learn method to update intelligence
FirstCharacter.Learn()

# Correctly accessing private attributes using getters
print(f'''Name: {FirstCharacter.GetName()}
Intelligence: {FirstCharacter.GetIntelligence()}
Age: {FirstCharacter.ReturnAge()}''')


class MagicCharacter(Character):
    #self.__Element string
    def __init__(self,element, charactername, dateofbirth, intelligence, speed):
        super().__init__(charactername, dateofbirth, intelligence, speed)
        self.__Element=element
    def Learn(self):
        if self.__Element=="fire" or "water":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif self.__Element=="earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*1.1)

FirstMagic=MagicCharacter("fire","Light",datetime.datetime(2018,3,3),75,22)
FirstMagic.Learn()
print(f"{FirstMagic.GetName()} has the age of {FirstMagic.ReturnAge()} and the intelligence of {FirstMagic.GetIntelligence()}")
