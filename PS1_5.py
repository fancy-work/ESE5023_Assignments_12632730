import matplotlib.pyplot as plt
#生成所有可能的字符串
def generate_all():
    digits = "123456789"
    expressions = ["1"]
    for digit in digits[1:]:
        new_expressions = []
        for expr in expressions:
            new_expressions.append(expr + "+" + digit)
            new_expressions.append(expr + "-" + digit)
            new_expressions.append(expr + digit)
        expressions = new_expressions
#将所有可能的字符串转换成表达式并求值，筛选出符合范围的
    results = []  
    for expr in expressions:
        value = eval(expr)
        if isinstance(value, int) and 1 <= value <= 100:
            results.append((expr, value))
    return results

def Find_expression(i):
    all_results = generate_all()
    found = False
    for expr, value in all_results:
        if value == i:
            print(f"{expr}={i}")
            found = True
    if not found:
        print(f"No solution found for {i}")

# 生成所有结果
all_results = generate_all()

# 统计 1~100 每个整数的解的数量
Total_solutions = []
for target in range(1, 101):
    count = 0
    for expr, value in all_results:
        if value == target:
            count += 1
    Total_solutions.append(count)

# 找出最大值和最小值对应的数字
max_count = max(Total_solutions)
min_count = min(Total_solutions)
max_numbers = [i+1 for i, c in enumerate(Total_solutions) if c == max_count]
min_numbers = [i+1 for i, c in enumerate(Total_solutions) if c == min_count]

print("Total_solutions =", Total_solutions)
print("最大解数量:", max_count, "对应数字:", max_numbers)
print("最小解数量:", min_count, "对应数字:", min_numbers)

# 绘图
x = list(range(1, 101))
plt.plot(x, Total_solutions, marker=".")
plt.xlabel("Target integer")
plt.ylabel("Number of solutions")
plt.title("Number of solutions for integers 1 to 100")
plt.grid(True)
plt.tight_layout()
plt.show()
