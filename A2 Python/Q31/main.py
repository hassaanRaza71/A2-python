def IteravtiveVowels(Value):
    Total=0
    LengthString=len(Value)
    for x in range(LengthString):
        FirstCharacter=Value[:1]
        if FirstCharacter in"aeiou":
            Total+=1
        Value=Value[1:LengthString]
    return Total

# print(IteravtiveVowels("house"))

def RecursiveVowel(Value):
    LenghtString=len(Value)
    if LenghtString==0:
        return 0
    else:
        if Value[0:1] in "aeiou":
            return 1 + RecursiveVowel(Value[1:len(Value)])
        else:
            return RecursiveVowel(Value[1:len(Value)])
        
print(RecursiveVowel("imagine"))



