# Problem 

# Somu went to the gym today. He decided to do X sets of squats. Each set consists of 
# 15 squats. Determine the total number of squats that he did today.

# Input Format

# The first line contains a single integer T — the number of test cases. Then the test cases follow.
# The first and only line of each test case contains an integer X — the total number of sets of squats that Somu did.


#code

# cook your dish here
T = int(input())
for _ in range(T):
    squats_set = int(input())
    num_squats = 15 * squats_set
    print(num_squats)
    