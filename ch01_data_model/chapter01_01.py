import collections

Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)]+list("JQKA")
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit)  for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self,position):
        return self._cards[position]

beer_card = Card('7','diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck)) # 52 반환
print(deck[0]) #
print(deck[-1])
print(deck)

from random import choice
print(choice(deck))

# special method의 장점
# 1. 임의 메서드명을 암기할 필요가 없다("항목 수를 알려면 어떻게 해야 하나? size를 어떻게 해야 하나 등등")
# 2. 파이썬 표준 라이브러리에서 제공하는 풍부한 기능을 별도로 구현할 필요 없이 바로 사용할 수 있다(random.choice()함수 처럼)
# 3. Silcing을 자동 지원한다

print(deck[12::13]) # index 12부터 13개씩 건너뛰어 에이스만 가져온다 12 -> 25 -> 38 -> 51
print(deck[12],deck[25],deck[38],deck[51])

# __getitem__() 특별 메소드 구현을 통해서 iterable하게 사용 가능하다
for card in deck:
    print(card)

# __contain__()연산자가 없다면 in연산자는 차례대로 검색된다.
print(Card('Q','hearts') in deck)
print(Card("Q",'beasts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1,clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index('A') # card.rank에 해당하는 index를 불러오는 코드(1-> 0, A -> 12)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck,key=spades_high): # club -> diamond -> hearts -> spades로 정렬
    print(card)

class A:
    aa='1234'
    def __init__(self):
        self.aa=self.aa*2
    def __len__(self):
        return len(self.aa)+1

a1=A()
print(len(a1))
print(a1.aa)