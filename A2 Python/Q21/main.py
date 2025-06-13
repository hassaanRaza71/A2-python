class TreasureChest:
    def __init__(self,pQuestion,pAnswer,pPoints):
        self.__question=pQuestion
        self.__answer=pAnswer
        self.__points=pPoints
    
    def getQuestion(self):
        return self.__question
    def CheckAnswers(self,user_answer):
        if user_answer==self.__answer:
            return True
        else:
            return False
    def getPoints(self,no_attempts):
        if no_attempts==1:
            return self.__points
        elif no_attempts==2:
            return (self.__points)/2
        elif no_attempts==3 or no_attempts==4:
            return (self.__points)/4
        else:
            return 0
def readData():
   
   arrayTreasure=[]    
   try:
       with open("TreasureChestData.txt") as Data:
        for question in range(5):
           question=Data.readline().strip()
           answer=int(Data.readline().strip())
           points=int(Data.readline().strip())
           Question_Check=TreasureChest(question,answer,points)
           arrayTreasure.append(Question_Check)
        return arrayTreasure
   except FileNotFoundError:
      print("File not found!")

arrayTreasure=readData()
question_number=int(input("Enter a question number between 1 and 5 Inclusive: "))-1
print(arrayTreasure[question_number].getQuestion())
answer=int(input("Enter your answer: "))
check=arrayTreasure[question_number].CheckAnswers(answer)
count=1
while not check:
    print(arrayTreasure[question_number].getQuestion())
    answer=int(input("Enter your answer: "))
    check=arrayTreasure[question_number].CheckAnswers(answer)
    count+=1
points_gained=arrayTreasure[question_number].getPoints(count)
print(points_gained)
        