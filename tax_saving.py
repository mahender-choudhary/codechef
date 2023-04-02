# In Chefland, everyone who earns strictly more than 
# Y rupees per year, has to pay a tax to Chef. Chef has allowed a special scheme where you can invest any amount of money and claim exemption for it.
# You have earned X (X>Y) rupees this year. Find the minimum amount of money you have to invest so that you don't have to pay taxes this year.

# Input Format

# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of a single line of input consisting of two space separated integers X and Y denoting the amount you earned and the amount above which you will have to pay taxes.

#code
# cook your dish here

T = int(input())
for _ in range(T):
    x , y = map(int, input().split())
    if x > y:
        print(x - y)
    else:
        continue