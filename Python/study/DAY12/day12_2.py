
def solution(array, n):
    fianl = 0
    answer = []
    for i in array:
        answer.append(abs(n-i))
    answer.sort()
    if answer[0]+n in array:
        final = answer[0]+n
    if n-answer[0] in array:
        final = n-answer[0]
    return final

print(solution([3, 10, 28],	20))

#어려운데 스스로 풀었다..! 뿌듯