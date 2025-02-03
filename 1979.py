# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PuPq6AaQDFAUq&

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N, K = map(int, input().split())

    row_input = []
    matrix_input = []

    for i in range(0, N):
        row_input = list(map(int, input().split()))
        matrix_input.append(row_input)
    
    def count_crossword(N, K, input):
        count = 0                                          # 단어가 들어갈 구간 개수 세기

        # 가로열 탐색
        for i in range(0, N):
            for j in range(0, N-K+1):
                if sum(input[i][j:j+K]) == K:              # 1이 연속해서 K개 존재할 경우 ([j] ~ [j+K-1])

                    if j == 0:                             # 1이 맨 처음[0]부터 시작하면
                        if input[i][K] == 0:               # 슬라이싱 바로 뒤 [K]번째 항목은 0으로 막혀야 함
                            count += 1

                    elif j == N-K:                         # 1이 맨 마지막[N-1]까지 이어지면
                        if input[i][N-K-1] == 0:           # 슬라이싱 바로 앞 [N-K-1]번째 항목은 0으로 막혀야 함
                            count += 1

                    else:
                        if input[i][j-1] == 0 and input[i][j+K] == 0:           # 리스트 바로 앞 뒤 항목이 0으로 막혀있음
                            count += 1

        # 세로열 탐색
        for a in range (0, N):
            for b in range(0, N-K+1):
                check_column = []                                               # K개 항목 확인 할 때 마다 초기화

                for c in range(0, K):
                    check_column.append(input[b+c][a])                          # 세로 열에 있는 항목 K개 check_column에 할당

                if sum(check_column) == K:                                      # 가로 세로 순서만 바뀌고 가로열 탐색과 동일

                    if b == 0:
                        if input[K][a] == 0 :
                            count += 1

                    elif b == N-K:
                        if input[N-K-1][a] == 0:
                            count += 1

                    else:
                        if input[b-1][a] == 0 and input[b+K][a] == 0:
                            count += 1

        return count

    print(f"#{test_case} {count_crossword(N, K, matrix_input)}")
'''
#가로, 세로열에 1이 연속해서 K개만 존재하는 리스트 내 구간을 찾아라라
N, K = 5, 3
matrix_input = [[1, 0, 0, 1, 0], 
                [1, 1, 0, 1, 1], 
                [1, 0, 1, 1, 1], 
                [0, 1, 1, 0, 1], 
                [0, 1, 1, 1, 0]]



def count_crossword(N, K, input):
    count = 0                                          # 단어가 들어갈 구간 개수 세기

    # 가로열 탐색
    for i in range(0, N):
        for j in range(0, N-K+1):
            if sum(input[i][j:j+K]) == K:              # 1이 연속해서 K개 존재할 경우 ([j] ~ [j+K-1])
        
                if j == 0:                             # 1이 맨 처음[0]부터 시작하면
                    if input[i][K] == 0:               # 슬라이싱 바로 뒤 [K]번째 항목은 0으로 막혀야 함
                        count += 1
                
                elif j == N-K:                         # 1이 맨 마지막[N-1]까지 이어지면
                    if input[i][N-K-1] == 0:           # 슬라이싱 바로 앞 [N-K-1]번째 항목은 0으로 막혀야 함
                        count += 1
                
                else:
                    if input[i][j-1] == 0 and input[i][j+K] == 0:           # 리스트 바로 앞 뒤 항목이 0으로 막혀있음
                        count += 1
    
    # 세로열 탐색
    for a in range (0, N):
        for b in range(0, N-K+1):
            check_column = []                                               # K개 항목 확인 할 때 마다 초기화

            for c in range(0, K):
                check_column.append(input[b+c][a])                          # 세로 열에 있는 항목 K개 check_column에 할당
            
            if sum(check_column) == K:                                      # 가로 세로 순서만 바뀌고 가로열 탐색과 동일

                if b == 0:
                    if input[K][a] == 0 :
                        count += 1

                elif b == N-K:
                    if input[N-K-1][a] == 0:
                        count += 1

                else:
                    if input[b-1][a] == 0 and input[b+K][a] == 0:
                        count += 1
    
    return count

print(count_crossword(N, K, matrix_input))
