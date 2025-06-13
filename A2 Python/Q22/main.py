class Picture:
    #Private Description String
    #Private Height Integer
    #Private Width Integer
    #Private FrameColour String
    def __init__(self,pDescription,pHeight,pWidth,pFrameColour):
        self.__Description=pDescription
        self.__Height=pHeight
        self.__Width=pWidth
        self.__FrameColour=pFrameColour
    
    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return self.__Height
    
    def GetWidth(self):
        return self.__Width
    
    def GetFrameColour(self):
        return self.__FrameColour
    
    def SetDescription(self,new_description):
        self.__Description=new_description
    

Pictures_Data=[Picture("",0,0,"") for _ in range(100)]

def ReadData():
    global Pictures_Data
    count=-1
    try:
        with open("Pictures.txt") as File:
            while True:
                description=File.readline().strip()
                if description=="":
                    break
                height=int(File.readline().strip())
                width=int(File.readline().strip())
                framecolour=File.readline().strip()
                picture_data=Picture(description,height,width,framecolour)
                count+=1
                Pictures_Data[count]=picture_data
            return count
    except FileNotFoundError:
        return -1
count=ReadData()

colour_required=input("Enter the colour of the frame for the required picture: ").lower()
width_required=int(input("Enter the max width required: "))
height_required=int(input("Enter the max height required: "))

for picture in Pictures_Data[:count]:

    if (picture.GetWidth()<=width_required and picture.GetHeight()<=height_required and picture.GetFrameColour()==colour_required):
        print(picture.GetDescription(),picture.GetHeight(),picture.GetWidth())
    
            


