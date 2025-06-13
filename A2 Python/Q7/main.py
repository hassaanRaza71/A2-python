#Q7a
#DECLARE DataArray : ARRAY [0:99] OF INTEGER
DataArray=[]

#Q7b
def ReadFile(DataArray):
    myfile=open("IntegerData.txt")
    for index in range(0,100):
        info=myfile.readline()
        DataArray.append(int(info))
    myfile.close()




#Q7c
def FindValues(DataArray):
    count=0
    in_range=False
    while not in_range:
        search_number=int(input("Enter a number between 1 and 100 to search: "))
        if search_number>=1 and search_number<=100:
             in_range=True
        else:
             print("Number out of range")
    for index in range(0,100):
        if DataArray[index]==search_number:
            count+=1
    return count


#Q7d(i)
ReadFile(DataArray)

print("Number of occurrences:",FindValues(DataArray))

#Q7e
def BubbleSort(DataArray):
    for  i in range(0,100):
        for j in range(0,99-i):
            if DataArray[j]>DataArray[j+1]:
                temp=DataArray[j]
                DataArray[j]=DataArray[j+1]
                DataArray[j+1]=temp
    
BubbleSort(DataArray)
print(DataArray)
       

