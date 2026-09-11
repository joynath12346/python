""""
In the famous Rock Paper Scissor game - Rock wins against scissors, paper wins
against rock, and scissors wins against paper.
Write a python program that takes two user inputs and returns who wins the game.
Sample Input:
> Player 1: rock
> Player 2: paper
Sample Output:
> Player 2 is the winner

""""


x = input()
y = input()

fl = False

if x == y:
    print("Draw")
    
elif x == "rock" and y == "scissors":
    print("Player 1 win")
    
elif x == "paper" and y == "rock":
    print("Player 1 win")
    
elif x == "scissors" and y == "paper":
    print("Player 1 win")
    
else :
    print("Player 2 win")
    
