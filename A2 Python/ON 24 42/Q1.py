
class EventItem:
    #__EventName : STRING
    #__Type : STRING
    #__Difficulty : INTEGER
    def __init__(self,Peventname,Ptype,Pdifficulty):
        self.__EventName=Peventname
        self.__Type=Ptype
        self.__Difficulty=Pdifficulty

    def GetEventName(self):
        return self.__EventName
    
    def GetType(self):
        return self.__Type
    
    def GetDifficulty(self):
        return self.__Difficulty
    
Group=[]
Group.append(EventItem("Bridge","jump",3))
Group.append(EventItem("Water wade","swim",4))
Group.append(EventItem("100 mile run","run",5))
Group.append(EventItem("Gridlock","drive",2))
Group.append(EventItem("Wall on wall","jump",4))


class Character:
    #__CharacterName:STRING
    #__Jump:INTEGER
    #__Swim:INTEGER
    #__Run:INTEGER
    #__Drive:INTEGER
    def __init__(self,PCharacterName,PJump,PSwim,PRun,PDrive):
        self.__CharacterName=PCharacterName
        self.__Jump=PJump
        self.__Swim=PSwim
        self.__Run=PRun
        self.__Drive=PDrive
    def GetName(self):
        return self.__CharacterName
    def CalculateScore(self,event_type,difficulty):
        Chance=0
        if event_type=="jump":
           Chance=self.__Jump
        elif event_type=="swim":
           Chance=self.__Swim
        elif event_type=="run":
           Chance=self.__Run
        elif event_type=="drive":
           Chance=self.__Drive
        if Chance>=difficulty:
            return 100
        else:
            difference=difficulty-Chance
            if difference==1:
                return 80
            elif difference==2:
                return 60
            elif difference==3:
                return 40
            elif difference==4:
                return 20
            else:
                return 0
            
Tarz=Character("Tarz",5,3,5,1)
Tarz_event1=Tarz.CalculateScore(Group[0].GetType(),Group[0].GetDifficulty())
Tarz_event2=Tarz.CalculateScore(Group[1].GetType(),Group[1].GetDifficulty())
Tarz_event3=Tarz.CalculateScore(Group[2].GetType(),Group[2].GetDifficulty())
Tarz_event4=Tarz.CalculateScore(Group[3].GetType(),Group[3].GetDifficulty())
Tarz_event5=Tarz.CalculateScore(Group[4].GetType(),Group[4].GetDifficulty())
Gene=Character("Gene",2,2,3,4)
Gene_event1=Gene.CalculateScore(Group[0].GetType(),Group[0].GetDifficulty())
Gene_event2=Gene.CalculateScore(Group[1].GetType(),Group[1].GetDifficulty())
Gene_event3=Gene.CalculateScore(Group[2].GetType(),Group[2].GetDifficulty())
Gene_event4=Gene.CalculateScore(Group[3].GetType(),Group[3].GetDifficulty())
Gene_event5=Gene.CalculateScore(Group[4].GetType(),Group[4].GetDifficulty())

Tarz_points=0
Gene_points=0
if Tarz_event1 > Gene_event1:
    Tarz_points += 1
    print("Tarz you win this event")
elif Tarz_event1 < Gene_event1:
    Gene_points += 1
    print("Geni you win this event")

if Tarz_event2 > Gene_event2:
    Tarz_points += 1
    print("Tarz you win this event")
elif Tarz_event2 < Gene_event2:
    Gene_points += 1
    print("Geni you win this event")

if Tarz_event3 > Gene_event3:
    Tarz_points += 1
    print("Tarz you win this event")
elif Tarz_event3 < Gene_event3:
    Gene_points += 1
    print("Geni you win this event")

if Tarz_event4 > Gene_event4:
    Tarz_points += 1
    print("Tarz you win this event")
elif Tarz_event4 < Gene_event4:
    Gene_points += 1
    print("Geni you win this event")

if Tarz_event5 > Gene_event5:
    Tarz_points += 1
    print("Tarz you win this event")
elif Tarz_event5 < Gene_event5:
    Gene_points += 1
    print("Geni you win this event")

# Final result
if Tarz_points > Gene_points:
    print(f"Tarz you have won with {Tarz_points}")
elif Tarz_points < Gene_points:
    print(f"Geni you have won with {Gene_points}")
else:
    print("It was a draw overall")


