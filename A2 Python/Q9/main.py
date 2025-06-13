#DECLARE StackVowel:ARRAY[0:99] OF CHAR
#DECLARE StackConsonantl:ARRAY[0:99] OF CHAR
#DECLARE VowelTop,ConsonantTop:INTEGER
StackVowel=[]
StackConsonant=[]
VowelTop=0
ConsonantTop=0

def PushData(letter):
    global StackVowel, StackConsonant, VowelTop, ConsonantTop
    if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        if VowelTop<99:
            StackVowel.append(letter)
            VowelTop+=1
        else:
            print("Stack is full")
    elif ConsonantTop<99:
        StackConsonant.append(letter)
        ConsonantTop+=1
    else:
        print("Stack is full")

def ReadData():
    myfile=open("StackData.txt")
    for index in range(100):
        letter=myfile.readline()[:1]
        PushData(letter)
    myfile.close
def PopVowel():
    global StackVowel, VowelTop
    if VowelTop>0:
        VowelTop-=1
        Data_popped=StackVowel[VowelTop]
        del StackVowel[VowelTop]
        return Data_popped
    else:
        return "Stack is empty"
def PopConsonant():
    global StackConsonant, ConsonantTop
    if ConsonantTop>0:
        ConsonantTop-=1
        Data_popped=StackConsonant[ConsonantTop]
        del StackConsonant[ConsonantTop]
        return Data_popped
    else:
        return "Stack is empty"
ReadData()
Letters=""
for index in range(0,5):
    Flag=False
    while Flag==False:
        choice=input("vowel or consonant: ").lower()
        if choice=="vowel":
            Data=PopVowel()
            if Data!="Stack is empty":
                Letters+=Data
                Flag=True
            else:
                print("No vowels left")
        else:
            Data=PopConsonant()
            if Data!="Stack is empty":
                Letters+=Data
                Flag=True
            else:
                print("No consonants left")
print(Letters)