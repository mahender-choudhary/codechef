# Problem

# Recently, Chef visited his doctor. The doctor advised Chef to drink at least 
# 2000
# 2000 ml of water each day.Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.

# Input Format

# The first line contains a single integer T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer X — the amount of water Chef drank today.


#code

# cook your dish here
T = int(input())
for _ in range(T):
    X = int(input())
    if X >= 2000:
        print('YES')
    else:
        print("NO")