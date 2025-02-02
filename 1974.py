# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&

# 제출용 답안
'''
row_input = []
matrix_input = []

for i in range(0, N):
    row_input = list(map(int, input().split()))
    matrix_input.append(row_input)

'''

# set을 이용해서 중복 없이 1부터 9까지 저장. 하나라도 없으면 set의 길이가 9가 아닌 것 이용

matrix_input = [[7, 3, 6, 4, 2, 9, 5, 8, 1], 
                [5, 8, 9, 1, 6, 7, 3, 2, 4], 
                [2, 1, 4, 5, 8, 3, 6, 9, 7], 
                [8, 4, 7, 9, 3, 6, 1, 5, 2], 
                [1, 5, 3, 8, 4, 2, 9, 7, 6], 
                [9, 6, 2, 7, 5, 1, 8, 4, 3], 
                [4, 2, 1, 3, 9, 8, 7, 6, 5], 
                [3, 9, 5, 6, 7, 4, 2, 1, 8], 
                [6, 7, 8, 2, 1, 5, 4, 3, 9]]

def check_sudoku(input):
    stamp = 0

    # 가로 열 확인
    for i in range(0, 9):
        test = set()
        test.update(input[i])

        if len(test) != 9:
            stamp += 1
    
    if stamp > 0:
        return 0
    
    stamp = 0      #stamp reset

    # 세로 열 확인
    for i in range(0, 9):
        test = set()
        for j in range(0, 9):
            test.add(input[j][i])

        if len(test) != 9:
            stamp += 1
    
    if stamp > 0:
        return 0
    
    stamp = 0       #stamp reset

    # 3*3 격자 확인
    for m in range(0, 3):
        for n in range(0, 3):
            test = set()

            for i in range(0, 3):
                for j in range(0, 3):
                    test.add(input[3*m+i][3*n+j])

                    if len(test) != 9:
                        stamp += 1
            
    if stamp > 0:
        return 0


    # 모든 테스트 통과시
    if stamp == 0:
        return 1

print(check_sudoku(matrix_input))
