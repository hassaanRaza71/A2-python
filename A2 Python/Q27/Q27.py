class Vehicle:
    def __init__(self, Id, maxspeed, IncreaseAmount):
        self.__ID = Id
        self.__MaxSpeed = maxspeed
        self.__IncreaseAmount = IncreaseAmount
        self.__HorizontalPosition = 0
        self.__CurrentSpeed = 0

    def GetCurrentSpeed(self):
        return self.__CurrentSpeed

    def GetIncreaseAmount(self):
        return self.__IncreaseAmount

    def GetMaxSpeed(self):
        return self.__MaxSpeed

    def GetHorizontalPosition(self):
        return self.__HorizontalPosition

    def IncreaseSpeed(self):
        self.__CurrentSpeed = self.__CurrentSpeed + self.__IncreaseAmount #Checking
        if self.__CurrentSpeed >= self.__MaxSpeed:
            self.__CurrentSpeed = self.__MaxSpeed

        self.__HorizontalPosition += self.__CurrentSpeed

    def SetCurrentSpeed(self, speed):
        self.__CurrentSpeed = speed
    def SetHorizontalPosition(self, Hposition):
        self.__HorizontalPosition = Hposition


class Helicopter(Vehicle):
    def __init__(self, VerticalChange, MaxHeight, Id, maxspeed, IncreaseAmount):
        super().__init__(Id, maxspeed, IncreaseAmount)
        self.__MaxHeight = MaxHeight
        self.__VerticalPosition = 0
        self.__VerticalChange = VerticalChange

    def GetVerticalPosition(self):
        return self.__VerticalPosition

    def IncreaseSpeed(self):
        self.__VerticalPosition += self.__VerticalChange
        if self.__VerticalPosition >= self.__MaxHeight:
            self.__VerticalPosition = self.__MaxHeight
        super().IncreaseSpeed()
        #super().SetHorizontalPosition(super().GetCurrentSpeed())
        if super().GetCurrentSpeed() > super().GetMaxSpeed():
            super().SetCurrentSpeed(super().GetMaxSpeed())


def OutputCurrentPosition(x):
    if type(x) == Vehicle:
        print(f"Current position is {x.GetHorizontalPosition()}")
        print(f"Current speed is {x.GetCurrentSpeed()}")

    elif type(x) == Helicopter:
        print(f"Current horizontal position {x.GetHorizontalPosition()}")
        print(f"Current vertical position is {x.GetVerticalPosition()}")
        print(f"Current speed is {x.GetCurrentSpeed()}")


NewVehicle = Vehicle("Tiger", 100, 20)
NewHelicopter = Helicopter(3,  100, Id = "Lion", maxspeed= 350, IncreaseAmount=40)

NewVehicle.IncreaseSpeed()
NewVehicle.IncreaseSpeed()
OutputCurrentPosition(NewVehicle)

NewHelicopter.IncreaseSpeed()
NewHelicopter.IncreaseSpeed()
OutputCurrentPosition(NewHelicopter)