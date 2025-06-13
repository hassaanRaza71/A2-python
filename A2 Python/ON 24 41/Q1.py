def ReadData():
    DataArray=[]
    with open("Data.txt") as Data:
        for line in Data:
            DataArray.append(line.strip())

    return DataArray

def FormatArray(DataArray):
    data_string=""
    for data in DataArray:
        data_string+=str(data) + " "
    return data_string

DataArray=ReadData()
print(FormatArray(DataArray))

def CompareStrings(string_1,string_2):
    for index in range(len(string_1)):
        if string_1[index:index+1]>string_2[index:index+1]:
            return 2
        elif string_1[index:index+1]<string_2[index:index+1]:
            return 1

def Bubble(DataArray):
    for x in range(len(DataArray)-1):
        for y in range(len(DataArray)-x-1):
            compare=CompareStrings(DataArray[y],DataArray[y+1])
            if compare==2:
                temp=DataArray[y]
                DataArray[y]=DataArray[y+1]
                DataArray[y+1]=temp
    return DataArray
DataArray=Bubble(DataArray)
print(FormatArray(DataArray))



