def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i%q == r:
            answer += code[i]
    return answer

print(solution(3,1,"qjnwezgrpirldywt"))

#문자열은 쉽게 풀리는 듯 하다.