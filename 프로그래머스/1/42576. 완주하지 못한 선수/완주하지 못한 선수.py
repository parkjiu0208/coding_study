def solution(participant, completion):
    c = sorted(completion)
    p = sorted(participant)
    for i in range(len(c)):
        if p[i] != c[i]:
            return p[i]
    return p[-1]