# Problem

# Chef is fond of burgers and decided to make as many burgers as possible.
# Chef has A patties and B buns. To make 1 burger, Chef needs 1 patty and 1 bun.
# Find the maximum number of burgers that Chef can make.

# Input Format

# The first line of input will contain an integer T — the number of test cases. The description of T test cases follows.
# The first and only line of each test case contains two space-separated integers A and B, the number of patties and buns respectively.


# cook your dish here
def burger(patties, buns):
    if patties <= buns:
        print(patties)
    else:
        print(buns)
        
t = int(input())
for _ in range(t):
    num = input().split()
    patties = int(num[0])
    buns = int(num[1])
    burger(patties, buns)