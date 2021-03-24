guess = ["rock","scissors","paper"]
from random import choice
print("rock, paper,scissors game start")
print("石头剪刀布游戏开始")
print("1是石头，2是剪刀，3是布")
print("规则：三盘两胜")
print("\r")      

def change(inputs):
    if inputs == "1":
        return "rock"
    elif inputs == "2":
        return "scissors"
    elif inputs == "3":
        return "paper"
    else:
        return "wrong"

    
def rule(player,computer):
    global player_score
    global computer_score
    
    if player == computer:
        return "draw"
    if player == "rock" and computer == "scissors":
        player_score += 1
        return "you won this turn"
    if player == "rock" and computer == "paper":
        computer_score += 1
        return "you loss this turn"
    if player == "scissors" and computer == "paper":
        player_score += 1
        return "you won this turn"
    if player == "scissors" and computer == "rock":
        computer_score += 1
        return "you loss this turn"
    if player == "paper" and computer == "rock":
        player_score += 1
        return "you won this turn"
    if player == "paper" and computer == "scissors":
        computer_score += 1
        return "you loss this turn"


while True:
    player_score = 0
    computer_score = 0
    times = 3

    while times > 0:
        print("your turn , please input your choice")
        you = input()
        insert = change(you)
        if insert == "wrong":
            print("you input wrong,please input again")
            continue
        com = choice(guess)
        print("your choose %s,computer choose %s" %(insert,com))
        result = rule(insert,com)
        print(result)
        times -= 1
        if player_score == 2 or computer_score == 2:
            break

    if player_score > computer_score:
        print("\r")
        print("your score is: %s, computer score is %s" %(player_score,computer_score))
        print("You Win")
    elif player_score < computer_score:
        print("\r")
        print("your score is: %s, computer score is %s" %(player_score,computer_score))
        print("You Loss")
    elif player_score == computer_score:
        print("\r")
        print("your score is: %s, computer score is %s" %(player_score,computer_score))
        print("Draw")

    print("\r")
    print("要继续下一把吗? y/n")
    answer = input()
    print("\r")
    if answer == "n":
        break
    
