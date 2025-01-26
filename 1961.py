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
'''

N = 3
a1 = [1, 2, 3]
a2 = [4, 5, 6]
a3 = [7, 8, 9]
matrix_input = []

matrix_input.append(a1)
matrix_input.append(a2)
matrix_input.append(a3)

clock90 = []
clock180 = []
clock270 = []