def calc_fibanonacci(n):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    val= calc_fibanonacci(n-1) + calc_fibanonacci(n-2)
    memo[n] = val
    return val


testCount = int(input())

for _ in range(0, testCount):
    memo = {}
    n = int(input())
    print(calc_fibanonacci(n))
    
