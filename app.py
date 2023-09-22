#User interaction
import role1, role2, game, random

print(game.gp) #calls the game information
d = input("choose between becoming a boy or girl")
if d == "boy":
    print(role1.boy) #calls the boy role's attributes
elif d == "girl":
    print(role2.girl) #calls the girl role's attributes 
print("You have chosen to be a",d)
n = input("Please choose a name for your person")
print("Welcome", n)
print(game.gp1) #calls the game information
if d == "boy": # if boy is chosen than this code/gameplay is activated 
    print("The first challenge deals with your strength, you are being tested by fighting the devil")
    print("Type 'go' to roll")
    r = input()
    if r == 'go':
        diceThrow1 = random.randrange(2, 13)   
        print(diceThrow1)    
    if diceThrow1 <= 3 and role1:
        print("Critical loss, strength decreased by 2, new strength is",role1.boy1-2)
    elif diceThrow1 >=4 and diceThrow1 <=7 and role1:
        print("Loss, strength decreased by 1, new strength is",role1.boy1-1)
    elif diceThrow1 >=8 and diceThrow1 <=10 and role1:
        print("Win, strength increased by 1, new strength is",role1.boy1+1)
    elif diceThrow1 >=11 and role1:
        print("Crtical win, strength increased by 2, new strength is",role1.boy1+2)
    print("The second challenge deals with your intelligence, you are being tested by reading and understanding The Bible")
    print("Type 'go' to roll")
    r = input()
    if r == 'go':
        diceThrow2 = random.randrange(2, 13)      
        print(diceThrow2)
    if diceThrow2 <= 3 and role1:
        print("Critical loss, intelligence decreased by 2, new intelligence is",role1.boy2-2)
    elif diceThrow2 >=4 and diceThrow2 <=7 and role1:
        print("Loss, intelligence decreased by 1, new intelligence is",role1.boy2-1)
    elif diceThrow2 >=8 and diceThrow2 <=10 and role1:
        print("Win, intelligence increased by 1, new intelligence is",role1.boy2+1)
    elif diceThrow2 >=11 and role1:
        print("Crtical win, intelligence increased by 2, new intelligence is",role1.boy2+2)
    print("The third and final challenge is abstaining from intercourse")
    print("Type 'go' to roll")
    r = input()
    if r == 'go':
        diceThrow3 = random.randrange(2, 13)       
        print(diceThrow3)
    if diceThrow3 <= 3 and role1:
        print("Critical loss, beauty decreased by 2, new beauty is",role1.boy3-2)
    elif diceThrow3 >=4 and diceThrow3 <=7 and role1:
        print("Loss, beauty decreased by 1, new beauty is",role1.boy3-1)
    elif diceThrow3 >=8 and diceThrow3 <=10 and role1:
        print("Win, beauty increased by 1, new beauty is",role1.boy3+1)
    elif diceThrow3 >=11 and role1:
        print("Crtical win, strength increased by 2, new beauty is",role1.boy2+2)
    if role1.boy4:
        print("You have been saved and have won the game of life")
    else:
        print("You have been condemned and have lost the game of life")
elif d == "girl": #if girl is chosen than this code/ gameplay is activated 
    print("The first challenge deals with your strength, you are being tested by fighting the devil")
    print("Type 'go' to roll")
    r = input()
    if r == 'go':
        diceThrow1 = random.randrange(2, 13)   
        print(diceThrow1)    
    if diceThrow1 <= 3 and role2:
        print("Critical loss, strength decreased by 2, new strength is",role2.girl1-2)
    elif diceThrow1 >=4 and diceThrow1 <=7 and role2:
        print("Loss, strength decreased by 1, new strength is",role2.girl1-1)
    elif diceThrow1 >=8 and diceThrow1 <=10 and role2:
        print("Win, strength increased by 1, new strength is",role2.girl1+1)
    elif diceThrow1 >=11 and role2:
        print("Crtical win, strength increased by 2, new strength is",role2.girl1+2)
    print("The second challenge deals with your intelligence, you are being tested by reading and understanding The Bible")
    print("Type 'go' to roll")
    r = input()
    if r == 'go':
        diceThrow2 = random.randrange(2, 13)      
        print(diceThrow2)
    if diceThrow2 <= 3 and role2:
        print("Critical loss, intelligence decreased by 2, new intelligence is",role2.girl2-2)
    elif diceThrow2 >=4 and diceThrow2 <=7 and role2:
        print("Loss, intelligence decreased by 1, new intelligence is",role2.girl2-1)
    elif diceThrow2 >=8 and diceThrow2 <=10 and role2:
        print("Win, intelligence increased by 1, new intelligence is",role2.girl2+1)
    elif diceThrow2 >=11 and role2:
        print("Crtical win, intelligence increased by 2, new intelligence is",role2.girl2+2)
    print("The third and final challenge is abstaining from intercourse")
    print("Type 'go' to roll")
    r = input()
    if r == 'go':
        diceThrow3 = random.randrange(2, 13)       
        print(diceThrow3)
    if diceThrow3 <= 3 and role2:
        print("Critical loss, beauty decreased by 2, new beauty is",role2.girl3-2)
    elif diceThrow3 >=4 and diceThrow3 <=7 and role2:
        print("Loss, beauty decreased by 1, new beauty is",role2.girl3-1)
    elif diceThrow3 >=8 and diceThrow3 <=10 and role2:
        print("Win, beauty increased by 1, new beauty is",role2.girl3+1)
    elif diceThrow3 >=11 and role2:
        print("Crtical win, strength increased by 2, new beauty is",role2.girl2+2)
    if role2.girl4:
        print("You have been saved and have won the game of life")
    else:
        print("You have been condemned and have lost the game of life")
