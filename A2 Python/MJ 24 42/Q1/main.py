WordArray=[]
NumberWords=0




def Play():
    global WordArray
    global NumberWords
    print(WordArray[0])
    print(NumberWords)
    answer=input("Enter a word: ").lower()
    count=0
    while answer!="no":
        Correct=False
        for _ in range(1,len(WordArray)):
            if WordArray[_]==answer:
                Correct=True
                WordArray[_]=-1
                count+=1
                
        if Correct:
            print("Correct Answer")
        else:
            print("Wrong Answer")

        answer=input("Enter a word: ").lower()
    percentage=(count/NumberWords)*100
    print(percentage,"%")
    if percentage<100:
        print("The words you missed are")
        for word in WordArray[1:]:
            if word!=-1:
                print(word)
        
def ReadWords(file_name):
    global WordArray
    global NumberWords
    count=-1
    with open(file_name) as data:
        for word in data:
            count+=1
            WordArray.append(word.strip())
        NumberWords=count
    Play()
user_input=input("'easy', 'medium' or 'hard'?").lower()
if user_input=="easy":
    ReadWords("Easy.txt")
elif user_input=="medium":
    ReadWords("Medium.txt")
else:
    ReadWords("Hard.txt")
    

