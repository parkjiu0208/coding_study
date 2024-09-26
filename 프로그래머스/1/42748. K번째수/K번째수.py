def solution(array, commands):
    answer = []
    for c in commands:
        li_so = sorted(array[c[0]-1:c[1]])
        answer.append(li_so[c[2]-1])
    return answer