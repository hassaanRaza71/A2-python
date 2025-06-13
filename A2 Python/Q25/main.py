class Card:
#    Number as integer
#    Colour as string
    def __init__(self,number,colour):
        self.__Number=number
        self.__Colour=colour

    def GetNumber(self):
        return self.__Number
    def GetColour(self):
        return self.__Colour
    
one_red=Card(1,"red")
two_red=Card(2,"red")
three_red=Card(3,"red")
four_red=Card(4,"red")
five_red=Card(5,"red")
one_blue=Card(1,"blue")
two_blue=Card(2,"blue")
three_blue=Card(3,"blue")
four_blue=Card(4,"blue")
five_blue=Card(5,"blue")
one_yellow=Card(1,"yellow")
two_yellow=Card(2,"yellow")
three_yellow=Card(3,"yellow")
four_yellow=Card(4,"yellow")
five_yellow=Card(5,"yellow")

class Hand:
    #DECLARE Cards:ARRAY[0:9] OF Card
    #FirstCard as INTEGER
    #NumberCards as INTEGER
    def __init__(self,card1,card2,card3,card4,card5):
        self.__Cards=[]
        self.__Cards.append(card1)
        self.__Cards.append(card2)
        self.__Cards.append(card3)
        self.__Cards.append(card4)
        self.__Cards.append(card5)
        self.__FirstCard=0
        self.__NumberCards=5

    def GetCard(self,index):
        return self.__Cards[index]
    
Player1=Hand(one_red,two_red,three_red,four_red,one_yellow)
Player2=Hand(two_yellow,three_yellow,four_yellow,five_yellow,one_blue)

def CalculateValue(player_hand):
    score=0
    for count in range(4):
        card_got=player_hand.GetCard(count)
        if card_got.GetColour=="red":
            score+=5
        elif card_got.GetColour=="blue":
            score+=10
        elif card_got.GetColour=="yellow":
            score+=15
        score+=card_got.GetNumber()
    return score

player1_score=CalculateValue(Player1)
player2_score=CalculateValue(Player2)
if player1_score>player2_score:
    print("Player 1 has the highest score")
elif player2_score>player1_score:
    print("Player 2 has the highest score")
else:
    print("Its a Draw. Both players have same score")

