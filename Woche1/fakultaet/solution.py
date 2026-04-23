
def calc_factorial(n):
    if n <= 1:
        return 1
    return n * calc_factorial(n - 1)

testCount = int(input())
for _ in range(0, testCount):
    n = int(input())
    print(calc_factorial(n))
