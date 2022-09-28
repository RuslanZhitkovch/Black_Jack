import random


class Card:
    def __init__(self,rank: str, suit:str) ->None:   # rank - значение #suit - масть
        self.rank = rank
        self.suit = suit

    def get_value(self) -> int:
        if self.rank in "ТВДК":
            return 10
        else:
            return " А23456789".index(self.rank)     # возвращаем значение

    def get_rank(self) ->str:
        return f"{self.suit}{self.rank}"


class DeskCard:
    def __init__(self) -> None:
        _rank  = "А23456789ТВДК"
        _suit = "ПБЧК"
        self.__cards = [Card(r,s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)

    def get_card(self) ->Card:
        return self.__cards.pop()

class Player:
    def __init__(self,name: str)-> None:
        self._hand = []
        self.count = 0
        self.name = name

    @property             # декоратор, т.к. данный метод будет как свойство
    def hand(self) ->str:
        return f"Карты в руке: {self._hand}; Очков - {self.count}"

    @hand.setter
    def hand(self,card: Card) ->None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())

class Dealer(Player):
   # def get_card(self, cards: DeskCard):
   #     while self.count < 18:
   #         self.hand =  cards.get_card()
    def get_card(self, cards: DeskCard):
        while self.count < 21:
           _card =  cards.get_card()
           if _card.get_value() + self.count <=21:
               self.hand = _card
           else:
               break






class Game:
    def __init__(self,player_name: str) ->None:
        self.cards = DeskCard()
        self.player = Player(name = player_name)
        self.dealer = Dealer(name = 'Dealer')


    def print(self) -> str:
        return f'\n{self.player.name} : {self.player.hand}\n{self.dealer.name} : {self.dealer.hand}'




    def check_count(self)->None:
        if self.player.count > 21:
            print(f"Вы проиграли", self.print())
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f"Поздравляю! {self.player.name} вы победили!", self.print())
        elif self.dealer.count == self.player.count:
            print(f"Ничья...", self.print())
        elif self.dealer.count > self.player.count:
            print(f"Вы проиграли", self.print())
        elif self.player.count > self.dealer.count:
            print(f"Поздравляю! {self.player.name} вы победили!", self.print())




    def start(self) -> None:

        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()

        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()


        print(self.player.hand)
        while self.player.count <21:
            answer = input("Хотите взять еще карту? да/нет ")
            if answer == 'да':
                self.player.hand = self.cards.get_card()
                print(self.player.hand)
            elif answer == "нет":
                self.dealer.get_card(self.cards)
                break
        self.check_count()








def main() ->None:
    print("Приветствую вас в игре Black Jack!")
    name = input("Ваше имя: ")
    print(f"Приятной игры {name}")
    game = Game(name)
    game.start()



if __name__ == '__main__':
    main()
