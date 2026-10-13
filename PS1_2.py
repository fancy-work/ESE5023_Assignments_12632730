#生成M1:5行10列，元素为0~50的随机整数
M1 = []
for i in range(5):
    row = []
    for j in range(10):
        row.append(random.randint(0, 50))
    M1.append(row)

#生成M2:10行5列，元素为0~50的随机整数
M2 = []
for i in range(10):
    row = []
    for j in range(5):
        row.append(random.randint(0, 50))
    M2.append(row)

def Matrix_multip(M1, M2):
    #创建一个五行五列的全0矩阵
    C = []
    for i in range(5):
        row = []
        for j in range(5):
            row.append(0)
        C.append(row)

    #for循环计算矩阵乘法
    for i in range(5):
        for j in range(5):
            total = 0
            for k in range(10):
                total = total + M1[i][k] * M2[k][j]
            C[i][j] = total

    return C

#打印结果
result = Matrix_multip(M1, M2)
print(result, "= M1 * M2")
