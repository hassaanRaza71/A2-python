#Q8a
FileData=[[""] * 2 for i in range(11)]

#8b
def ReadHighScore():
    global FileData
    myfile=open("HighScore.txt","r")
    for i in range(0,10):
        FileData[i][0]=myfile.readline()[:3]
        FileData[i][1]=myfile.readline().rstrip("\n")
    myfile.close

#8c
def OutputHighScores():
    global FileData
    print("High Scores:")
    for i in range(0,10):
        print(FileData[i][0],FileData[i][1])
#Q8d
ReadHighScore()       
OutputHighScores()

#Q8e(i)
Y=False
while Y==False:
    newplayer_name=input("Enter a 3-character player name: ")
    if len(newplayer_name)==3:
        Y=True
    else:
        print("Invalid name. Please enter a 3-character name")
X=False
while X==False:
    newplayer_score=int(input("Enter a player score between 1 and 10000: "))
    if newplayer_score>=1 and newplayer_score<=10000:
        X=True
    else:
        print("Entered score not in range!")

#Q8eii
def NewHighScore(newplayer_name,newplayer_score):
    FileData[10][0]=newplayer_name
    FileData[10][1]=str(newplayer_score)
    for i in range(0,11):
        for j in range(0,10-i):
            if int(FileData[j][1])<int(FileData[j+1][1]):
                temp=FileData[j]
                FileData[j]=FileData[j+1]
                FileData[j+1]=temp
    FileData.pop(10)

#8eiii and iv
print(FileData)
NewHighScore(newplayer_name,newplayer_score)
print(FileData)

#Q8f
def WriteTopTen():
    global FileData
    myfile=open("NewHighScore.txt","w")
    for i in range(0,10):
        myfile.write(FileData[i][0]+"\n")
        myfile.write(str(FileData[i][1])+"\n")
    myfile.close
WriteTopTen()





