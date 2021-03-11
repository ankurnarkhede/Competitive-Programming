# input no of test cases
t = int(input())

# input test cases
n = (list(map(int, input().strip().split(' '))))

# logic
for i in range(0, len(n), +1):
    for j in range(1, n[i] + 1, +1):
        if (j % 3 == 0 and j % 5 == 0):
            print('FizzBuzz')
        elif (j % 3 == 0):
            print('Fizz')
        elif (j % 5 == 0):
            print('Buzz')
        else:
            print(j)
