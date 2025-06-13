#DECLARE StackData:ARRAY [0:9] OF INTEGER
global StackData
global StackPointer #INTEGER
StackData=[0]*10
StackPointer=0
def PrintArray():
  global StackData,StackPointer
  print(StackPointer)
  for x in range(0,10):
    print(StackData[x])


def Push(integer_value):
  global StackData,StackPointer
  if StackPointer==10:
    print("Stack is full")
    return False
  else:
    StackData[StackPointer]=integer_value
    StackPointer+=1
    return True
for i in range(0,11):
  input_number=int(input("Enter a number: "))
  result=Push(input_number)
  if result==True:
    print("Number is added to the stack")
  else:
    print("Stack is full! Number not added")
print(StackData)

def Pop():
  global StackData,StackPointer
  if StackPointer==0:
    return -1
  else:
    StackPointer-=1
    Popped_data=StackData[StackPointer]
    del StackData[StackPointer]
    return Popped_data
Pop()
Pop()
print(StackData)