def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        a = int(i[s:s+l:1])
        if a>k:
            answer.append(a)
    return answer

intStrs1 = ["0123456789","9876543210","9999999999999"]

print(solution(intStrs1,50000,5,5))

#스스로 문제를 풀다. 매우뿌듯..!! 코딩 두뇌가 돌아가는 것 같다 히히