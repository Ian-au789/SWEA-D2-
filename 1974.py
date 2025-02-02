# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5Psz16AYEDFAUq&

# 제출용 답안
'''
row_input = []
matrix_input = []

for i in range(0, 9):
    row_input = list(map(int, input().split()))
    matrix_input.append(row_input)

    ~~~
    
print(f"#{test_case} {check_sudoku(matrix_input)}")
'''

# set을 이용해서 중복 없이 1부터 9까지 저장. 하나라도 없으면 set의 길이가 9가 아닌 것 이용

matrix_input = [[4, 5, 7, 1, 6, 3, 8, 2, 9], 
                [6, 3, 9, 8, 2, 7, 5, 4, 1], 
                [7, 9, 3, 4, 8, 5, 1, 6, 2], 
                [1, 8, 2, 5, 4, 9, 6, 3, 7], 
                [8, 6, 1, 7, 9, 2, 3, 5, 4], 
                [5, 2, 4, 6, 3, 1, 7, 9, 8], 
                [3, 7, 6, 9, 1, 4, 2, 8, 5], 
                [2, 4, 5, 3, 7, 8, 9, 1, 6], 
                [9, 1, 8, 2, 5, 6, 4, 7, 3]]

def check_sudoku(input):
    stamp = 0

    # 가로 열 확인
    for i in range(0, 9):
        test1 = set()
        test1.update(input[i])

        if len(test1) != 9:
            stamp += 1
    
    if stamp > 0:
        return 0
    
    stamp = 0      #stamp reset

    # 세로 열 확인
    for i in range(0, 9):
        test2 = set()
        for j in range(0, 9):
            test2.add(input[j][i])

        if len(test2) != 9:
            stamp += 1
    
    if stamp > 0:
        return 0
    
    stamp = 0       #stamp reset

    # 3*3 격자 확인
    for k in range(0, 3):
        test3 = set()

        for m in range(0, 3):
            for n in range(0, 3):
                test3.update(input[3*k+n][3*m+0:3*m+3])

            if len(test3) != 9:
                stamp += 1
      
    if stamp > 0:
        return 0

    # 모든 테스트 통과시
    if stamp == 0:
        return 1
    
    
print(check_sudoku(matrix_input))
