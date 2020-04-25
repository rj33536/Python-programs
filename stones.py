
import random
player1 = input("Enter name of first player")
player2 = input("Enter name of second player")
player1_score = 0
player2_score = 0
turn = True
size=12
stones = []
for index in range(size):
    number = random.randint(1,10)
    stones.append(number)
while len(stones)>0:
    print()
    print(stones)
    if turn==True:
        print(player1,"turn")
    else:
        print(player2,"turn")
    choice = input("enter your choice (start/end) ")
    value=0
    if choice=="start":
        value = stones[0]
        stones = stones[1:] 
        
    else:
        value = stones[-1]
        stones = stones[:-1]
    if turn==True:
        player1_score  = player1_score + value
        turn = False
    else:
        player2_score  = player2_score + value
        turn = True
    print(player1+" score = "+str(player1_score))
    print(player2+" score = "+str(player2_score))

if player1_score>player2_score:
    print(player1,"wins!!!")
elif player1_score<player2_score:
    print(player2,"wins!!!")
else:
    print("It's a tie")
    
    
    
    
    
