# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Pq-OKAVYDFAUq

# 제출용 답안
'''
N = int(input())
row_input = []
matrix_input = []

for i in range(0, N):
    row_input = list(map(int, input().split()))
    matrix_input.append(row_input)

print(f"#{test_case}")

    for column in range(0, N):
        for row in range(0, N):
            print(matrix_input[N-1-row][column], end='')

        print(" ", end = '')

        for row in range(0, N):
            print(matrix_input[N-1-column][N-1-row], end='')

        print(" ", end = '')

        for row in range(0, N):
            print(matrix_input[row][N-1-column], end='')
        
        print("")
'''

N = 6
a1 = [6, 9, 4, 7, 0, 5]
a2 = [8, 9, 9, 2, 6, 5]
a3 = [6, 8, 5, 4, 9, 8]
a4 = [2, 2, 7, 7, 8, 4]
a5 = [7, 5, 1, 9, 7, 9]
a6 = [8, 9, 3, 9, 7, 6]
matrix_input = []

matrix_input.append(a1)
matrix_input.append(a2)
matrix_input.append(a3)
matrix_input.append(a4)
matrix_input.append(a5)
matrix_input.append(a6)

M = len(matrix_input)

for column in range(0, M):
    print("")

    for row in range(0, M):
        print(matrix_input[M-1-row][column], end='')
    
    print(" ", end = '')

    for row in range(0, M):
        print(matrix_input[M-1-column][M-1-row], end='')

    print(" ", end = '')

    for row in range(0, M):
        print(matrix_input[row][M-1-column], end='')

