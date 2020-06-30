import math

# Functions
def arraydelta(array1,array2):
    if len(array1)!=len(array2):
        return -1
    else:
        sum=0
        for i in range(len(array1)):
            sum+=(array1-array2)**2
        return math.sqrt(sum)


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


# 创建二维系数矩阵
A = [[0 for j in range(10)]for i in range(9)]
Atrans = A = def_A(A)
eps=1E-8


# 列主元消元
x1=x2=[0]*9
while(abs()>eps):
    pass


# 解线性方程组
list_x=[0]*9
list_x[8]=Atrans[8][9]/Atrans[8][8]
i=7
while i>=0:
    k=i+1
    sum=0
    while k<=8:
        sum+=Atrans[i][k]*list_x[k]
        k+=1
    list_x[i]=1/Atrans[i][i]*(Atrans[i][9]-sum)
    i-=1



# 输出结果
print("根为：")
for i in range(9):
    print("x%d=%.12f"%(i+1,list_x[i])) # 因数量级均在1附近，未使用科学计数法
print("\n消元后的矩阵是：")
for i in range(9):
    for j in range(10):
        print("%.2f"%(Atrans[i][j]),end="\t\t")
    print("")
