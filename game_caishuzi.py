def small_game(num):
    answer = input()
    answer = int(answer)
    if answer>num:
        print("big")
        return False

    if answer<num:
        print("samll")
        return False

    if answer==num:
        print("yes")
        print("game over")
        return True



print("hello what's your name")
from random import randint
num = randint(1,100)
you = input()
print("oh, how are you!")
print("Let's Guess number!")
result = False

while result == False:
    result = small_game(num)

a = 10
b = 3.14
c = "test"
print("this is %d" %a)
print("this is %f" %b)
print("this is " + c)
print("this is num: %d, this is float: %f, this is str: %s" %(a,b,c))

for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end=' ') #如果需要在同行输出则需要添加 end=' '
    print()

