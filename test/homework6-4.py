'''
Due to some BUGs of Pycharm(Community Version), I can no longer use Chinese words in my program, or they'll vanish upon input.
The problem would be presumably fixed next time with Professional Version used.
'''


# Importation Area
import math


# Functions Area
def arraydelta(array1, array2):
    if len(array1) != len(array2):
        return -1
    else:
        sum = 0
        for i in range(len(array1)):
            sum+=(array1[i] - array2[i]) ** 2
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
    A[0][9] = -15
    A[1][9] = 27
    A[2][9] = -23
    A[3][9] = 0
    A[4][9] = -20
    A[5][9] = 12
    A[6][9] = -7
    A[7][9] = 7
    A[8][9] = 10

    return A


# Executation Area
if __name__ == '__main__':
    A = [[0 for j in range(10)]for i in range(9)]
    A = def_A(A)
    eps = 1E-8
    x1 = [0] * 9
    x2 = [0] * 9
    x3 = [0] * 9
    x4 = [0] * 9
    # Gauss-Seidel Method
    step_GS = 0
    while (arraydelta(x1, x2) > eps or step_GS == 0):
        x1 = x2
        for i in range(9):
            t1 = 0
            for j in range(9):
                if j != i:
                    t1 += A[i][j] * x2[j]
            x2[i] = -(t1 - A[i][9]) / A[i][i]
        step_GS += 1
        print(hasd)
    # SOR Method
    step_SOR = []
    for k in range(99):
        omega = (k + 1) / 50
        step_SOR.append(0)
        while (arraydelta(x3, x4) > eps or step_SOR[k] == 0):
            x3 = x4
            for i in range(9):
                t2 = 0
                for j in range(9):
                    if j != i:
                        t2 += A[i][j] * x4[j]
                t2 = -(t2 - A[i][9]) / A[i][i]
                x4[i] = (1 - omega) * x4[i] + omega * t2
            step_SOR[k] += 1
    best = range(99).index(min(step_SOR))


# Output Area果
    print("The roots are:")
    for i in range(9):
        print("x%d = %.12f" % (i+1, x2[i]))
    print("The overall steps of Gauss-Seidel Iteration Method is %d\n" % step_GS)
    print("SOR Iteration results:")
    for k in range(len(step_SOR)):
        print("Relaxation factor: %.2f, Iteration steps: %d" % ((k + 1) / 50, step_SOR[k]))
    print("The best relaxation factor is: %.2f" % ((best+1) / 50))
