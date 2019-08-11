#!/usr/bin/env python
#Top trumps game

from random import randint as rr
from random import choice as rc

def clear():
      for i in range(50):
            print("\n")
            
def menu():
      selection = raw_input("1. Play Game\n2. Help\n3. Quit\n>>> ")
      selection = selection.lower()
      if selection == 'play game' or selection == '1':
            clear()
            game()
      elif selection == 'help' or selection == '2':
            clear()
            print("Welcome to this Top Trumps game!\n\nHelp and Instructions:\nWhen in the main menu, press 1 to\nplay the game, 2 to view this again\nor 3 to quit.\nAlternatively you can type\nPlay Game, Help or Quit.\nThis is case insensitive.\nIf you chose 1 or Play Game, you\ncan type 1 or minions to use the\nminions card set (5 cards each),\n2 or footballers to use the\nfootballers card set (10 cards each),\nor 3 or celebrities to use the\ncelebrities card set (15 cards each).\nThese cards will have random attributes.\nEg - Intelligence will be from 1 to\n20, Leadership will be from 1 to 10\nand Excitement will be from 1 to 100.\nOnce you have done this, you can\ntype Intelligence, Excitement or\nLeadership to select that category.\nIf your score is higher, you win\nand get both cards, if you draw,\nyou keep your card, and if you\nlose, the computer gets both cards.\nThe game ends when either you, or\nthe computer has all the cards\nand has won.\n")
            raw_input("Press RETURN to return to the menu\n>>> ")
            clear()
            menu()
      elif selection == 'quit' or selection == '3':
            clear()
            raw_input("Press RETURN to quit\n>>> ")
            clear()
            quit()
      else:
            clear()
            print("Invalid Input - Please try again...\n")
            menu()
            
def game():
      f=open("cards.pyt", "r")#open dogs.txt in read mode
      if f.mode == 'r': #if opened correctly in read mode, do
            contents = f.read()
            minions,footballers,celebrities = contents.split(";")
            min1,min2,min3,min4,min5,min6,min7,min8,min9,min10 = minions.split(",")
            fb1,fb2,fb3,fb4,fb5,fb6,fb7,fb8,fb9,fb10,fb11,fb12,fb13,fb14,fb15,fb16,fb17,fb18,fb19,fb20 = footballers.split(",")
            ce1,ce2,ce3,ce4,ce5,ce6,ce7,ce8,ce9,ce10,ce11,ce12,ce13,ce14,ce15,ce16,ce17,ce18,ce19,ce20,ce21,ce22,ce23,ce24,ce25,ce26,ce27,ce28,ce29,ce30 = celebrities.split(",")
            start_intel,stop_intel,start_lead,stop_lead,start_excite,stop_excite = 1,20,1,10,1,100
            m1,m2,m3,m4,m5,m6,m7,m8,m9,m10 = {"name":min1,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min2,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min3,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min4,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min5,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min6,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min7,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min8,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min9,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":min10,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)}
            f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20 = {"name":fb1,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb2,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb3,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb4,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb5,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb6,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb7,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb8,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb9,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb10,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb11,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb12,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb13,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb14,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb15,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb16,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb17,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb18,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb19,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":fb20,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)}
            c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30 = {"name":ce1,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce2,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce3,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce4,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce5,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce6,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce7,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce8,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce9,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce10,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce11,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce12,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce13,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce14,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce15,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce16,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce17,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce18,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce19,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce20,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce21,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce22,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce23,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce24,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce25,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce26,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce27,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce28,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce29,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)},{"name":ce30,"intelligence":rr(start_intel,stop_intel),"leadership":rr(start_lead,stop_lead),"excitement":rr(start_excite,stop_excite)}
            minions = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
            footballers = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]
            celebrities = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29,c30]

      while True:
            selection = raw_input("What would you like to play?\n1. Minions (5 cards each)\n2. Footballers (10 cards each)\n3. Celebrities (15 cards each)\n>>> ")
            selection = selection.lower()
            if selection == 'minions' or selection == '1':
                  clear()
                  cards_used = minions
                  break
            elif selection == 'footballers' or selection == '2':
                  clear()
                  cards_used = footballers
                  break
            elif selection == 'celebrities' or selection == '3':
                  clear()
                  cards_used = celebrities
                  break
            else:
                  clear()
                  print("Invalid Input - please try again...\n")
      
      player_cards = []
      computer_cards = []
      allocated_cards = []
      
      while True:
            if len(player_cards) < (len(cards_used)/2):
                  card_picked = rr(1,len(cards_used))
                  if card_picked not in allocated_cards:
                        if card_picked == 1:
                              player_cards.append(cards_used[0])
                              allocated_cards.append(1)
                        elif card_picked == 2:
                              player_cards.append(cards_used[1])
                              allocated_cards.append(2)
                        elif card_picked == 3:
                              player_cards.append(cards_used[2])
                              allocated_cards.append(3)
                        elif card_picked == 4:
                              player_cards.append(cards_used[3])
                              allocated_cards.append(4)
                        elif card_picked == 5:
                              player_cards.append(cards_used[4])
                              allocated_cards.append(5)
                        elif card_picked == 6:
                              player_cards.append(cards_used[5])
                              allocated_cards.append(6)
                        elif card_picked == 7:
                              player_cards.append(cards_used[6])
                              allocated_cards.append(7)
                        elif card_picked == 8:
                              player_cards.append(cards_used[7])
                              allocated_cards.append(8)
                        elif card_picked == 9:
                              player_cards.append(cards_used[8])
                              allocated_cards.append(9)
                        elif card_picked == 10:
                              player_cards.append(cards_used[9])
                              allocated_cards.append(10)
                        elif card_picked == 11:
                              player_cards.append(cards_used[10])
                              allocated_cards.append(11)
                        elif card_picked == 12:
                              player_cards.append(cards_used[11])
                              allocated_cards.append(12)
                        elif card_picked == 13:
                              player_cards.append(cards_used[12])
                              allocated_cards.append(13)
                        elif card_picked == 14:
                              player_cards.append(cards_used[13])
                              allocated_cards.append(14)
                        elif card_picked == 15:
                              player_cards.append(cards_used[14])
                              allocated_cards.append(15)
                        elif card_picked == 16:
                              player_cards.append(cards_used[15])
                              allocated_cards.append(16)
                        elif card_picked == 17:
                              player_cards.append(cards_used[16])
                              allocated_cards.append(17)
                        elif card_picked == 18:
                              player_cards.append(cards_used[17])
                              allocated_cards.append(18)
                        elif card_picked == 19:
                              player_cards.append(cards_used[18])
                              allocated_cards.append(19)
                        elif card_picked == 20:
                              player_cards.append(cards_used[19])
                              allocated_cards.append(20)
                        elif card_picked == 21:
                              player_cards.append(cards_used[20])
                              allocated_cards.append(21)
                        elif card_picked == 22:
                              player_cards.append(cards_used[21])
                              allocated_cards.append(22)
                        elif card_picked == 23:
                              player_cards.append(cards_used[22])
                              allocated_cards.append(23)
                        elif card_picked == 24:
                              player_cards.append(cards_used[23])
                              allocated_cards.append(24)
                        elif card_picked == 25:
                              player_cards.append(cards_used[24])
                              allocated_cards.append(25)
                        elif card_picked == 26:
                              player_cards.append(cards_used[25])
                              allocated_cards.append(26)
                        elif card_picked == 27:
                              player_cards.append(cards_used[26])
                              allocated_cards.append(27)
                        elif card_picked == 28:
                              player_cards.append(cards_used[27])
                              allocated_cards.append(28)
                        elif card_picked == 29:
                              player_cards.append(cards_used[29])
                              allocated_cards.append(29)
                        elif card_picked == 30:
                              player_cards.append(cards_used[29])
                              allocated_cards.append(30)
            else:
                  break
                  
      while True:
            if len(computer_cards) < (len(cards_used)/2):
                  card_picked = rr(1,len(cards_used))
                  if card_picked not in allocated_cards:
                        if card_picked == 1:
                              computer_cards.append(cards_used[0])
                              allocated_cards.append(1)
                        elif card_picked == 2:
                              computer_cards.append(cards_used[1])
                              allocated_cards.append(2)
                        elif card_picked == 3:
                              computer_cards.append(cards_used[2])
                              allocated_cards.append(3)
                        elif card_picked == 4:
                              computer_cards.append(cards_used[3])
                              allocated_cards.append(4)
                        elif card_picked == 5:
                              computer_cards.append(cards_used[4])
                              allocated_cards.append(5)
                        elif card_picked == 6:
                              computer_cards.append(cards_used[5])
                              allocated_cards.append(6)
                        elif card_picked == 7:
                              computer_cards.append(cards_used[6])
                              allocated_cards.append(7)
                        elif card_picked == 8:
                              computer_cards.append(cards_used[7])
                              allocated_cards.append(8)
                        elif card_picked == 9:
                              computer_cards.append(cards_used[8])
                              allocated_cards.append(9)
                        elif card_picked == 10:
                              computer_cards.append(cards_used[9])
                              allocated_cards.append(10)
                        elif card_picked == 11:
                              computer_cards.append(cards_used[10])
                              allocated_cards.append(11)
                        elif card_picked == 12:
                              computer_cards.append(cards_used[11])
                              allocated_cards.append(12)
                        elif card_picked == 13:
                              computer_cards.append(cards_used[12])
                              allocated_cards.append(13)
                        elif card_picked == 14:
                              computer_cards.append(cards_used[13])
                              allocated_cards.append(14)
                        elif card_picked == 15:
                              computer_cards.append(cards_used[14])
                              allocated_cards.append(15)
                        elif card_picked == 16:
                              computer_cards.append(cards_used[15])
                              allocated_cards.append(16)
                        elif card_picked == 17:
                              computer_cards.append(cards_used[16])
                              allocated_cards.append(17)
                        elif card_picked == 18:
                              computer_cards.append(cards_used[17])
                              allocated_cards.append(18)
                        elif card_picked == 19:
                              computer_cards.append(cards_used[18])
                              allocated_cards.append(19)
                        elif card_picked == 20:
                              computer_cards.append(cards_used[19])
                              allocated_cards.append(20)
                        elif card_picked == 21:
                              computer_cards.append(cards_used[20])
                              allocated_cards.append(21)
                        elif card_picked == 22:
                              computer_cards.append(cards_used[21])
                              allocated_cards.append(22)
                        elif card_picked == 23:
                              computer_cards.append(cards_used[22])
                              allocated_cards.append(23)
                        elif card_picked == 24:
                              computer_cards.append(cards_used[23])
                              allocated_cards.append(24)
                        elif card_picked == 25:
                              computer_cards.append(cards_used[24])
                              allocated_cards.append(25)
                        elif card_picked == 26:
                              computer_cards.append(cards_used[25])
                              allocated_cards.append(26)
                        elif card_picked == 27:
                              computer_cards.append(cards_used[26])
                              allocated_cards.append(27)
                        elif card_picked == 28:
                              computer_cards.append(cards_used[27])
                              allocated_cards.append(28)
                        elif card_picked == 29:
                              computer_cards.append(cards_used[28])
                              allocated_cards.append(29)
                        elif card_picked == 30:
                              computer_cards.append(cards_used[29])
                              allocated_cards.append(30)
            else:
                  break
      
      if len(player_cards) == 5:
            print("Your cards are:\n " +player_cards[0]["name"] +"\n " +player_cards[1]["name"] +"\n " +player_cards[2]["name"] +"\n " +player_cards[3]["name"] +"\n " +player_cards[4]["name"])
            original_cards = len(player_cards)
      elif len(player_cards) == 10:
            print("Your cards are:\n " +player_cards[0]["name"] +"\n " +player_cards[1]["name"] +"\n " +player_cards[2]["name"] +"\n " +player_cards[3]["name"] +"\n " +player_cards[4]["name"] +"\n " +player_cards[5]["name"] +"\n " +player_cards[6]["name"] +"\n " +player_cards[7]["name"] +"\n " +player_cards[8]["name"] +"\n " +player_cards[9]["name"])
            original_cards = len(player_cards)
      elif len(player_cards) == 15:
            print("Your cards are:\n " +player_cards[0]["name"] +"\n " +player_cards[1]["name"] +"\n " +player_cards[2]["name"] +"\n " +player_cards[3]["name"] +"\n " +player_cards[4]["name"] +"\n " +player_cards[5]["name"] +"\n " +player_cards[6]["name"] +"\n " +player_cards[7]["name"] +"\n " +player_cards[8]["name"] +"\n " +player_cards[9]["name"] +"\n " +player_cards[10]["name"] +"\n " +player_cards[11]["name"] +"\n " +player_cards[12]["name"] +"\n " +player_cards[13]["name"] +"\n " +player_cards[14]["name"])
            original_cards = len(player_cards)
      chooser = "player"
      while True:
            if len(computer_cards) == 0:
                  clear()
                  print("You won!")
                  raw_input("Press RETURN to quit\n>>> ")
                  clear()
                  quit()
            elif len(player_cards) == 0:
                  clear()
                  print("The computer won!")
                  raw_input("Press RETURN to quit\n>>> ")
                  clear()
                  quit()
            clear()
            print("The computer's card is:\nName: " +computer_cards[len(computer_cards)-1]["name"] +"\n")
            print("Your card is:\nName: " +player_cards[len(player_cards)-1]["name"] +"\nIntelligence: " +str(player_cards[len(player_cards)-1]["intelligence"]) +"\nExcitement: " +str(player_cards[len(player_cards)-1]["excitement"]) +"\nLeadership: " +str(player_cards[len(player_cards)-1]["leadership"]))
            if chooser == 'player':
                  player_category = raw_input("\nWhat category would you like to use?\n>>> ")
                  player_category = player_category.lower()
                  if player_category == 'intelligence':
                        if player_cards[len(player_cards)-1]['intelligence'] > computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("You won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['intelligence']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['intelligence']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['intelligence'] == computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("You drew!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['intelligence']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['intelligence']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['intelligence'] < computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("The computer won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['intelligence']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['intelligence']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
                  elif player_category == 'excitement':
                        if player_cards[len(player_cards)-1]['excitement'] > computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("You won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['excitement']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['excitement']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['excitement'] == computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("You drew!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['excitement']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['excitement']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['excitement'] < computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("The computer won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['excitement']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['excitement']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
                  elif player_category == 'leadership':
                        if player_cards[len(player_cards)-1]['leadership'] > computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("You won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['leadership']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['leadership']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['leadership'] == computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("You drew!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['leadership']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['leadership']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['leadership'] < computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("The computer won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['leadership']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['leadership']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
                  else:
                        clear()
                        raw_input("Invalid Input - please try again...\nPress RETURN!\n>>> ")
                        
            elif chooser == 'computer':
                  print("\nIt's the Computer's Turn\n")
                  raw_input("Press RETURN to continue\n>>> ")
                  computer_category = rc(['intelligence','excitement','leadership'])
                  if computer_category == 'intelligence':
                        if player_cards[len(player_cards)-1]['intelligence'] > computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("The computer picked Intelligence\n")
                              print("You won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['intelligence']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['intelligence']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['intelligence'] == computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("The computer picked Intelligence\n")
                              print("You drew!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['intelligence']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['intelligence']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['intelligence'] < computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("The computer picked Intelligence\n")
                              print("The computer won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['intelligence']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['intelligence']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
                  elif computer_category == 'excitement':
                        if player_cards[len(player_cards)-1]['excitement'] > computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("The computer picked Excitement\n")
                              print("You won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['excitement']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['excitement']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['excitement'] == computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("The computer picked Intelligence\n")
                              print("You drew!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['excitement']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['excitement']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['excitement'] < computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("The computer picked Excitement\n")
                              print("The computer won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['excitement']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['excitement']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
                  elif computer_category == 'leadership':
                        if player_cards[len(player_cards)-1]['leadership'] > computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("The computer picked Leadership\n")
                              print("You won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['leadership']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['leadership']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['leadership'] == computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("The computer picked Leadership\n")
                              print("You drew!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['leadership']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['leadership']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['leadership'] < computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("The computer picked Leadership\n")
                              print("The computer won!")
                              print("Your score: " +str(player_cards[len(player_cards)-1]['leadership']) +"\nComputer's Score: " +str(computer_cards[len(computer_cards)-1]['leadership']) +"\n")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
            
clear()
menu()