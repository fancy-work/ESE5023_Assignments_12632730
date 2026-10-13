import math
def Pascal_triangle(k):
    row = []
    for i in range(k + 1):
        x = math.factorial(k) // (math.factorial(i) * math.factorial(k - i))
        row.append(x)
    print(row)

Pascal_triangle(100)
Pascal_triangle(200)
