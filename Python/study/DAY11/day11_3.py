def solution(s, e):
    answer = []
    for i in range(s,e-1,-1):
        answer.append(i)
    return answer

print(solution(10,3))
