sum = int(input())
x = int(input())
if (sum == x):
    print(sum//2, x//2)
    for i in range(sum-1):
        y = sum - i
    if (x == i*y):
        print(f'i = {i}, y = {y}')
     