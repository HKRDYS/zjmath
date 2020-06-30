def def_A(A):
    # Part A
    A[0][0] = 31
    A[0][1] = -13
    A[0][5] = -10
    A[1][0] = -13
    A[1][1] = 35
    A[1][2] = 9
    A[1][4] = 11
    A[2][1] = -9
    A[2][2] = 31
    A[2][3] = -10
    A[3][2] = -10
    A[3][3] = 79
    A[3][4] = -30
    A[3][8] = -9
    A[4][3] = -30
    A[4][4] = 57
    A[4][5] = -7
    A[4][7] = -5
    A[5][4] = -7
    A[5][5] = 47
    A[5][6] = -30
    A[6][5] = -30
    A[6][6] = 41
    A[7][4] = -5
    A[7][7] = 27
    A[7][8] = -2
    A[8][3] = -9
    A[8][7] = -2
    A[8][8] = 29
    # Part B
    A[0][9]=-15
    A[1][9]=27
    A[2][9]=-23
    A[3][9]=0
    A[4][9]=-20
    A[5][9]=12
    A[6][9]=-7
    A[7][9]=7
    A[8][9]=10

    return A


# 行交换函数
def row_exchange(list_ex,i1,i2):
    list_ex[i1],list_ex[i2] = list_ex[i2],list_ex[i1]

    return list_ex


# 创建二维系数矩阵
A = [[0 for i in range(10)]for j in range(9)]
A = def_A(A)
Atrans = A

# 列主元消元
j = 0
while j<8:
    i=j+1
    jp=jc=j
    # 列主元
    comp=[]
    while jc<=8:
        comp.append(Atrans[jc][j])
        jc+=1
    k=Atrans[j].index(max(comp))

    try:
        pass

    except():
        pass

    # 消元
    while jp<=8:
        if Atrans[i][j]!=0:
            Atrans[i][jp] += -Atrans[i][j]/A[i-1][j]*Atrans[i-1][jp]
        jp+=1
    j+=1


# 解线性方程组

# 输出结果
for i in range(9):
    for j in range(9):
        print(A[i][j], end="\t\t")
    print("")
