def solution(a, d, included):
    c=a
    result = 0
    for i in range(len(included)):
        if included[i] == True:
            result += c
        c+=d
        i+=1
    return result


included1 = [True, False, False, True, True]
print(solution(3,4,included1))