class Card:
#    DECLARE Number:INTEGER
#    DECLARE Colour:STRING

    def __init__(self,Number,Colour):
        self.__number=Number
        self.__colour=Colour

    def GetNumber(self):
        return self.__number
    
    
    def GetColour(self):
        return self.__colour

cards_array=[Card(-1,"") for _ in range(30)]


with open("CardValues.txt") as data:
    for _ in range(0,30):
        num=int(data.readline().strip())
        col=data.readline().strip()
        cards_array[_].__number=num
        cards_array[_].__colour=col

selectedcards=[]
def ChooseCard():
    new_selection=False
    already_selected=False
    while new_selection==False:
        card_number=int(input("Enter a number between 1 and 30 inclusive: "))
        if card_number>=1 and card_number<=30:
            for card in selectedcards:
                already_selected=False
                if card_number==card:
                    print("taken")
                    already_selected=True
            if already_selected==False:
                print("valid")
                new_selection=True
                selectedcards.append(card_number)
    return card_number

PLayer1=[Card(-1,"") for _ in range(4)]
for _ in range(4):
    num=ChooseCard()
    PLayer1[_].__number=cards_array[num-1].__number
    PLayer1[_].__colour=cards_array[num-1].__colour

for _ in range(4):
    print(PLayer1[_].__number)
    print(PLayer1[_].__colour)