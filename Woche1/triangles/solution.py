triangleCount = int(input())

for _ in range(0, triangleCount):
    lines = int(input())
    # Gaus Formel, // -> Ganzzahl Division 
    print(lines * (lines + 1) // 2)