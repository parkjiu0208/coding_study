def solution(x1, x2, x3, x4):
    answer = (x1 or x2) and (x3 or x4)
    return answer

print(solution(False,True,True,True))

# 어렵진 않지만, or, and, xor 등의 개념을 다시 정립할 수 있었음.