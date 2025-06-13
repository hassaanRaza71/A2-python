#HighScores : 2D ARRAY OF STRING
HighScores=[]

def ReadData():
    global HighScores
    try:
        with open("HighScoreTable.txt") as data:
            for _ in range(7):
                player_id=data.readline().strip()
                level=data.readline().strip()
                score=data.readline().strip()
                HighScores.append([player_id,level,score])
            return HighScores
    except FileNotFoundError:
        print("File not found")

    
def OutputHighScoress(HighScores):
    for index in range(len(HighScores)):
        print(f"{HighScores[index][0]} reached level {HighScores[index][1]} with score of {HighScores[index][2]}")

        
def SortScores():
    global HighScores
    for i in range(len(HighScores)-1):
        for j in range(len(HighScores)-i-1):
            if int(HighScores[j][1])<int(HighScores[j+1][1]):
                temp=HighScores[j]
                HighScores[j]=HighScores[j+1]
                HighScores[j+1]=temp
    for i in range(len(HighScores)-1):
        for j in range(len(HighScores)-i-1):
            if int(HighScores[j][1])==int(HighScores[j+1][1]):
                if int(HighScores[j][2])<int(HighScores[j+1][2]):
                    temp=HighScores[j]
                    HighScores[j]=HighScores[j+1]
                    HighScores[j+1]=temp

    
    return HighScores

HighScores=ReadData()
print("Before")
OutputHighScoress(HighScores)
HighScores=SortScores()
print("After")
OutputHighScoress(HighScores)



