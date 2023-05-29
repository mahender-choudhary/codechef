# Problem

# Chef is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a 6 on the die.

# In the current turn, Chef rolled the number X on the die. Determine if Chef can enter a new token into the play in the current turn or not.

# Input Format
# The first line contains a single integer T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer X — the number rolled by the Chef on the die.



# cook your dish here
def ludo_game(num):
    if num < 6:
        print("NO")
    else:
        print("YES")
        
t = int(input())
for _ in range(t):
    number = int(input())
    ludo_game(number)
