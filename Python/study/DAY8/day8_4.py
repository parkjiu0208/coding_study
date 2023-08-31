def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)

print(solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]]	))

#아직 남의 코드를 본다. 그래도 -1을 생각한 것과 for 문 안에 s,e 넣은 것 