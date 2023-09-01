def solution(my_string, n):
    answer = ''
    a = len(my_string)
    answer += my_string[a-n:]
    return answer

print(solution("ProgrammerS123",11))