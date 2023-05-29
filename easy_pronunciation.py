# cook your dish here
T = int(input())
for _ in range(T):
    A = int(input())
    word = input()
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in word:
        if i in vowel:
            count = count + 1
    value = A - count
    if value < 4:
        print('YES')
    else:
        print("NO")