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
print("Welcome", n,)
print(game.gp1) #calls the game information
print("The first challenge deals with your strength, you are being tested by fighting the devil")
print("Type 'go' to roll")
r = input()
if r == 'go':
    diceThrow = random.randrange(1, 7)   
print(diceThrow)    
if diceThrow >=4:
    print("Critical loss, strength decreased")
else:
    print("Crtical win, strength increased")
print("The second challenge deals with your intelligence, you are being tested by reading and understanding The Bible")
print("Type 'go' to roll")
r = input()
if r == 'go':
    diceThrow = random.randrange(1, 7)      
print(diceThrow)
if diceThrow >=4:
    print("Critical loss, intelligence decreased")
else:
    print("Crtical win, intelligence increased")
print("The third and final challenge is abstaining from intercourse")
print("Type 'go' to roll")
r = input()
if r == 'go':
    diceThrow = random.randrange(1, 7)       
print(diceThrow)
if diceThrow >=4:
    print("Critical loss, beauty decreased")
else:
    print("Crtical win, beauty increased")
p = input("Before we tell you if you won or lost the game of life do you accept Jesus Christ as your Lord and saviour? yes or no ")
if p == "yes":
    print("You have been saved and won the game of life")
elif p == "no":
    print("You have lost the game of life")