# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    row_input = []
    matrix_input = []

    for i in range(0, N):
        row_input = list(map(int, input().split()))
        matrix_input.append(row_input)

        
    def how_many_flies(N, M, input):

        fly_swap = []
        fly_dead = 0
        fly_max = 0

        for h in range(0, N-M+1):
            for i in range(0, N-M+1):
                fly_swap = []                                      # 매 횟수마다 리스트 초기화

                for j in range(0, M):
                    fly_swap.extend(input[h+j][i:i+M])             # fly_swap 리스트에 M*M 행렬에 들어있는 항목 추가

                fly_dead = sum(fly_swap)                           # M*M 행렬에 들어있던 파리 개수 전부 더하기

                if fly_dead > fly_max:                             # 파리 개수 세서 최댓값을 갱신할 떄마다 새로 저장
                    fly_max = fly_dead

        return fly_max

    print(f"#{test_case} {how_many_flies(N, M, matrix_input)}")
'''

N, M = 6, 3
matrix_input = [[29, 21, 26, 9, 5, 8], 
                [21, 19, 8, 0, 21, 19], 
                [9, 24, 2, 11, 4, 24], 
                [19, 29, 1, 0, 21, 19], 
                [10, 29, 6, 18, 4, 3], 
                [29, 11, 15, 3, 3, 29]]


def how_many_flies(N, M, input):

    fly_swap = []
    fly_dead = 0
    fly_max = 0

    for h in range(0, N-M+1):
        for i in range(0, N-M+1):
            fly_swap = []                                      # 매 횟수마다 리스트 초기화

            for j in range(0, M):
                fly_swap.extend(input[h+j][i:i+M])             # fly_swap 리스트에 M*M 행렬에 들어있는 항목 추가

            fly_dead = sum(fly_swap)                           # M*M 행렬에 들어있던 파리 개수 전부 더하기

            if fly_dead > fly_max:                             # 파리 개수 세서 최댓값을 갱신할 떄마다 새로 저장
                fly_max = fly_dead

    return fly_max

print(how_many_flies(N, M, matrix_input))