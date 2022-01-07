import random

class Card:
    def __init__(self,face,suit,value):
        self.face = face
        self.suit = suit
        self.value = value

    def get_value(self):
        return self.value

    def get_face(self):
        return self.face

    def get_suit(self):
        return self.suit

class Deck:
    # index 0 corresponds to A
    face_to_values = [i for i in range(1,14)]
    face_to_values[0] = 14

    # abbreviation of suits: spades, hearts, diamonds, clubs
    suits = ['s', 'h', 'd', 'c']

    def __init__(self,master_num = 0,n = 2):
        self.cards = []
        self.face_to_values[master_num-1] = 15
        for i in range(n):
            for suit in self.suits:
                for face in range(13):
                    self.cards.append(Card(face+1,suit,self.face_to_values[face]))

            self.cards.append(Card(100,'J',100))
            self.cards.append(Card(99,'j',99))

    def shuffle(self):
        random.shuffle(self.cards)



