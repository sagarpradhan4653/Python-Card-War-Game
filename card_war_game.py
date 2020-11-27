# English Card War Game for two components comp vs user

import itertools
import random

try:
    class Deck:
        deck = list(itertools.product(range(1, 14), [
                    'Spade', 'Heart', 'Diamond', 'Club']))
        random.shuffle(deck)
        player1 = input("Enter First Player's Name:  ")
        player2 = input("Enter Second Player's Name:  ")

        newCardList = []
        for i in range(52):
            t = (str(deck[i][0]) + " of " + deck[i][1])
            newCardList.append(t)
        comp = newCardList[0:26]
        user = newCardList[26:]
        print(f"\n{player1.upper()} have {len(comp)}\n")
        print(f"{player2.upper()} have {len(user)}\n")


    class Hand(Deck):
        def who_wins(self): 
            ask = input("Do you want to continue(Y/N) ?")
            if ask[0].lower() in 'y':      
                while (len(self.user) > 1 and len(self.comp) > 1):
                
                 
                    for (user_cards, comp_cards) in zip(self.user[:1], self.comp[:1]):
                        print("first one", user_cards, comp_cards)
                        if int(user_cards[:2]) > int(comp_cards[:2]):
                            # delete 2 items and store in user stack
                            self.user.append(self.comp.pop(0))
                            self.user.append(self.user.pop(0))
                            print(
                                f"\n {self.player1} HAVE--{len(self.user)}\n\n {self.player2} HAVE--{len(self.comp)} \n\n <---{self.player1} won--->")
                                
                        elif int(user_cards[:2]) < int(comp_cards[:2]):
                            self.comp.append(self.user.pop(0))
                            self.comp.append(self.comp.pop(0))

                            print(
                                f" \n {self.player1} HAVE--{len(self.user)}\n\n {self.player2} HAVE--{len(self.comp)} \n\n<---{self.player2} win--->")
                        else:
                            print(
                                f"USER:-{user_cards}\n\nCOMP:-{comp_cards} \n <---Tie between user and comp \n\n !!!-It is a WAR!!!")
                            for (user_cards_three, comp_cards_three) in zip(self.user[0:1], self.comp[0:1]):
                                if int(user_cards_three[:2]) > int(comp_cards_three[:2]):
                                    for i in self.comp[0:8]:
                                        self.user.append(i)
                                        self.comp.remove(i)
                                    print(
                                        f"\n {self.player1} HAVE--{len(self.user)}\n\n {self.player2} HAVE--{len(self.comp)}\n\n<---{self.player1} win---> \n\n")

                                    print("\nlength of user list1", len(self.user))
                                    print("\nlength of comp list1", len(self.comp))
                                elif int(user_cards_three[:2]) < int(comp_cards_three[:2]):
                                    for j in self.user[0:8]:
                                        self.comp.append(j)
                                        self.user.remove(j)
                                    print(
                                        f"\n {self.player1} HAVE--{len(self.user)}\n\nC{self.player2}HAVE--{len(self.comp)}\n\n<---{self.player2} win---> \n\n")
                                    print("\nlength of user list", len(self.user))
                                    print("\nlength of comp list", len(self.comp))
                                else:
                                    print(f"Forcefully made  {self.player1} Winner --->")
                                    for (first,last) in zip(self.user, self.comp):
                                        print("user\n",first)
                                        print("comp\n",last)
                                        self.user.append(last)
                                        self.comp.remove(last)
                                    print(f"COMP HAVE {len(self.comp)}  \nUSER HAVE  {len(self.user)} -------{self.player1.upper()} winn the game")

            else:
                print("Thanku for playing!!!!")



    class Win(Hand):
        def checkWhoWin(self):
            if len(self.comp) == 0:
                print(f"{self.player1} Won the Game!!!")
            elif len(self.user) == 0:
                print(f"{self.player2} Won the Game!!!")
            else:
                pass


    obj = Deck()
    obj1 = Hand()
    obj2 = Win()
    obj2.checkWhoWin()
    obj1.who_wins()


except:
    print("!!Something Went Error!!")
    print("Contact with your developer")

finally:
    print("<-----GAME IS OVER---->")


