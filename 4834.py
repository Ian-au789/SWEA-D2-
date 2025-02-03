# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AYYPdof62mIDFARc

# 제출용 답안
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number = input()
    
    def many_number(N, num_string):
        num_list = []

        for i in range(0, N):
            num_list.append(int(num_string[i]))

        num_set = set()
        num_set.update(num_list)

        most_number = 0
        how_many = 0

        for element in num_set:
            count = num_list.count(element)

            if how_many < count:
                how_many = count
                most_number = element

            elif how_many == count:
                if most_number < element:
                    most_number = element

        return most_number, how_many
	
    result = many_number(N, number)
    print(f'#{test_case} {result[0]} {result[1]}')
'''

N = 5
input_str = "08971"

def many_number(N, num_string):
    num_list = []

    for i in range(0, N):
        num_list.append(int(num_string[i]))

    num_set = set()
    num_set.update(num_list)

    most_number = 0
    how_many = 0

    for element in num_set:
        count = num_list.count(element)

        if how_many < count:
            how_many = count
            most_number = element

        elif how_many == count:
            if most_number < element:
                most_number = element

    return most_number, how_many

print(many_number(N, input_str))