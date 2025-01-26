# https://swexpertacademy.com/main/code/problem/problemDetail.do

# 제출용 정답
'''
T = int(input())
for test_case in range(0, T ):
    
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sum = 0
    multi_sum = 0
    sum_temp = 0

    if a == b:
        for i in range(0, a):
            sum_temp += A[i] * B[i]

    elif a < b:
        for i in range(0, b-a+1):
            for j in range(0, a):
                multi_sum += A[j] * B[i+j]

            if sum_temp <= multi_sum:
                sum_temp = multi_sum
            multi_sum = 0
           
    else:
        for i in range(0, a-b+1):
            for j in range(0, b):
                multi_sum += A[i+j] * B[j]

            if sum_temp <= multi_sum:
                sum_temp = multi_sum
            multi_sum = 0

    print(f"#{test_case+1} {sum_temp}")
'''
a, b = 3, 5
A = [1, 5, 3]
B = [3, 6, -7, 5, 4]

sum = 0
multi_sum = 0
sum_temp = 0

if a == b:
    for i in range(0, a):
        sum_temp += A[i] * B[i]

elif a < b:
    for i in range(0, b-a+1):
        for j in range(0, a):
            multi_sum += A[j] * B[i+j]

        if sum_temp <= multi_sum:
            sum_temp = multi_sum
        multi_sum = 0
        
else:
    for i in range(0, a-b+1):
        for j in range(0, b):
            multi_sum += A[i+j] * B[j]

        if sum_temp <= multi_sum:
            sum_temp = multi_sum
        multi_sum = 0

print(sum_temp)