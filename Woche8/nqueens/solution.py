def isCollision(row1, col1, row2, col2):
    # Check row (Not needed maybe????)
    if row1==row2:
        return True
    # check col
    if col1==col2:
        return True
    # check diagonal
    if abs(row1 - row2) == abs(col1 - col2):
        return True
    return 0

def isSafe(sol, row, col):
    for r in range(row):
        # Check if spot collides with existing entries
        if isCollision(r, sol[r], row, col):
            return False
    return True

def placeQueen(sol, row, n):
    # Exit if row complete
    if row == n:
        print_solution(sol)
        return

    for col in range(n):
        # Check if spot is safe
        if isSafe(sol, row, col):
            # Place Queen
            sol[row] = col
            # Recursive call dor next placement
            placeQueen(sol, row + 1, n)


def nqueens(n):
    sol = [0] * n
    placeQueen(sol, 0, n)

def print_solution(sol):
    l = len(sol)
    for i in range(l):
        for j in range(l):
            if j == sol[i]:
                print('Q', end='')
            else:
                print('.', end='')
        print()
    print()

testCount = int(input())

for _ in range(0, testCount):
    n = int(input())
    nqueens(n)
