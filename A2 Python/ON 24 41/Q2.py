class Horse:
    #__Name STRING
    #__MaxFenceHeight INTEGER
    #__PercentageSuccess INTEGER
    def __init__(self,PName,PMaxFenceHeight,pPercentageSuccess):
        self.__Name=PName
        self.__MaxFenceHeight=PMaxFenceHeight
        self.__PercentageSuccess=pPercentageSuccess

    def GetName(self):
        return self.__Name

    def GetMaxFenceHeight(self):
        return self.__MaxFenceHeight

    def Success(self,height,risk):
        if self.__MaxFenceHeight < height:
            return self.__PercentageSuccess*0.20
        else:
            if risk==5:
                modifier=0.6
            elif risk==4:
                modifier=0.7
            elif risk==3:
                modifier=0.8
            elif risk==2:
                modifier=0.9
            elif risk==1:
                modifier=1.0
            return self.__PercentageSuccess*modifier

Horses=[Horse("",0,0) for _ in range(2)]
Horses[0]=Horse("Beauty",150,0.72)
Horses[1]=Horse("Jet",160,0.65)

print(Horses[0].GetName())
print(Horses[1].GetName())

class Fence:
    def __init__(self,pHeight,pRisk):
        self.__Height=pHeight
        self.__Risk=pRisk

    def GetHeight(self):
        return self.__Height
    def GetRisk(self):
        return self.__Risk

Course=[]
for _ in range(4):
    correct_input=False
    while not correct_input:
        height=int(input("Enter a height of the fence in cm between 70 and 180 inclusive: "))
        if height>=70 and height<=180:
            correct_input=True
    correct_input = False
    while not correct_input:
        risk = int(input("Enter the whole number for risk between 1 and 5 inclusive: "))
        if risk>=1 and risk<=5:
            correct_input = True
            Course.append(Fence(height,risk))

fence1=Horses[0].Success(Course[0].GetHeight(),Course[0].GetRisk())
fence2=Horses[0].Success(Course[1].GetHeight(),Course[1].GetRisk())
fence3=Horses[0].Success(Course[2].GetHeight(),Course[2].GetRisk())
fence4=Horses[0].Success(Course[3].GetHeight(),Course[3].GetRisk())
avg_horse1=(fence1 + fence2 + fence3 + fence4)/4
print(f'''The horse {Horses[0].GetName()} at fence 1 has a {int(fence1*100)}% chance of success
The horse {Horses[0].GetName()} at fence 2 has a {int(fence2*100)}% chance of success
The horse {Horses[0].GetName()} at fence 1 has a {int(fence3*100)}% chance of success
The horse {Horses[0].GetName()} at fence 1 has a {int(fence4*100)}% chance of success
''')
print(f"The horse {Horses[0].GetName()} has a {int(avg_horse1*100)}% chance of jumping all over the fence")



fence1=Horses[1].Success(Course[0].GetHeight(),Course[0].GetRisk())
fence2=Horses[1].Success(Course[1].GetHeight(),Course[1].GetRisk())
fence3=Horses[1].Success(Course[2].GetHeight(),Course[2].GetRisk())
fence4=Horses[1].Success(Course[3].GetHeight(),Course[3].GetRisk())
avg_horse2=(fence1 + fence2 + fence3 + fence4)/4

print(f'''The horse {Horses[1].GetName()} at fence 1 has a {int(fence1*100)}% chance of success
The horse {Horses[1].GetName()} at fence 2 has a {int(fence2*100)}% chance of success
The horse {Horses[1].GetName()} at fence 1 has a {int(fence3*100)}% chance of success
The horse {Horses[1].GetName()} at fence 1 has a {int(fence4*100)}% chance of success
''')

print(f"The horse {Horses[1].GetName()} has a {int(avg_horse2*100)}% chance of jumping all over the fence")

if avg_horse1>avg_horse2:
    print(f"The horse {Horses[0].GetName()} has a highest average chance of success")
else:
    print(f"The horse {Horses[1].GetName()} has a highest average chance of success")