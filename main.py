#!/usr/bin/env python
#Top trumps game

from random import randint as rr

def clear():
      for i in range(100):
            print("\n")
            
def menu():
      selection = raw_input("1. Play Game\n2. Help\n3. Quit\n>>> ")
      selection = selection.lower()
      if selection == 'play game' or selection == '1':
            clear()
            game()
      elif selection == 'help' or selection == '2':
            clear()
            print("Coming Soon!")
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
      f=open("cards.txt", "r")#open dogs.txt in read mode
      if f.mode == 'r': #if opened correctly in read mode, do
            contents = f.read()
            minions,footballers = contents.split(";")
            min1,min2,min3,min4,min5,min6,min7,min8,min9,min10 = minions.split(",")
            fb1,fb2,fb3,fb4,fb5,fb6,fb7,fb8,fb9,fb10,fb11,fb12,fb13,fb14,fb15,fb16,fb17,fb18,fb19,fb20 = footballers.split(",")
            m1,m2,m3,m4,m5,m6,m7,m8,m9,m10 = {"name":min1,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min2,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min3,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min4,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min5,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min6,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min7,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min8,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min9,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":min10,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)}
            f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20 = {"name":fb1,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb2,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb3,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb4,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb5,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb6,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb7,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb8,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb9,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb10,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb11,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb12,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb13,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb14,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb15,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb16,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb17,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb18,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb19,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},{"name":fb20,"intelligence":rr(1,10),"leadership":rr(1,10),"excitement":rr(1,10)},
            minions = [m1,m2,m3,m4,m5,m6,m7,m8,m9,m10]
            footballers = [f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16,f17,f18,f19,f20]

      while True:
            selection = raw_input("What would you like to play?\n1. Minions (5 cards each)\n2. Footballers (10 cards each)\n>>> ")
            selection = selection.lower()
            if selection == 'minions' or selection == '1':
                  clear()
                  cards_used = minions
                  break
            elif selection == 'footballers' or selection == '2':
                  clear()
                  cards_used = footballers
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
            else:
                  break
      
      if len(player_cards) == 5:
            print("Your cards are:\n " +player_cards[0]["name"] +"\n " +player_cards[1]["name"] +"\n " +player_cards[2]["name"] +"\n " +player_cards[3]["name"] +"\n " +player_cards[4]["name"])
            original_cards = len(player_cards)
      elif len(player_cards) == 10:
            print("Your cards are:\n " +player_cards[0]["name"] +"\n " +player_cards[1]["name"] +"\n " +player_cards[2]["name"] +"\n " +player_cards[3]["name"] +"\n " +player_cards[4]["name"] +"\n " +player_cards[5]["name"] +"\n " +player_cards[6]["name"] +"\n " +player_cards[7]["name"] +"\n " +player_cards[8]["name"] +"\n " +player_cards[9]["name"])
            original_cards = len(player_cards)
            
      while True:
            if len(computer_cards) == 0:
                  clear()
                  print("You won!")
                  raw_input("Press RETURN to return to the menu\n>>> ")
                  clear()
                  menu()
            elif len(player_cards) == 0:
                  clear()
                  print("The computer won!")
                  raw_input("Press RETURN to return to the menu\n>>> ")
                  clear()
                  menu()
            clear()
            print("Your card is:\nName: " +player_cards[len(player_cards)-1]["name"] +"\nIntelligence: " +str(player_cards[len(player_cards)-1]["intelligence"]) +"\nExcitement: " +str(player_cards[len(player_cards)-1]["excitement"]) +"\nLeadership: " +str(player_cards[len(player_cards)-1]["leadership"]))
            chooser = "player"
            if chooser == 'player':
                  player_category = raw_input("\nWhat category would you like to use?\n>>> ")
                  player_category = player_category.lower()
                  if player_category == 'intelligence':
                        if player_cards[len(player_cards)-1]['intelligence'] > computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("You won!")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['intelligence'] == computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("You drew!")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['intelligence'] < computer_cards[len(computer_cards)-1]['intelligence']:
                              clear()
                              print("The computer won!")
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
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['excitement'] == computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("You drew!")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['excitement'] < computer_cards[len(computer_cards)-1]['excitement']:
                              clear()
                              print("The computer won!")
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
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,computer_cards[len(computer_cards)-1])
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = "player"
                        elif player_cards[len(player_cards)-1]['leadership'] == computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("You drew!")
                              raw_input("Press RETURN to continue\n>>> ")
                              player_cards.insert(0,player_cards[len(player_cards)-1])
                              player_cards.pop(len(player_cards)-1)
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              chooser = chooser
                        elif player_cards[len(player_cards)-1]['leadership'] < computer_cards[len(computer_cards)-1]['leadership']:
                              clear()
                              print("The computer won!")
                              raw_input("Press RETURN to continue\n>>> ")
                              computer_cards.insert(0,player_cards[len(player_cards)-1])
                              computer_cards.insert(0,computer_cards[len(computer_cards)-1])
                              computer_cards.pop(len(computer_cards)-1)
                              player_cards.pop(len(player_cards)-1)
                              chooser = "computer"
                  else:
                        clear()
                        raw_input("Invalid Input - please try again...\nPress RETURN!\n>>> ")
            
clear()
menu()