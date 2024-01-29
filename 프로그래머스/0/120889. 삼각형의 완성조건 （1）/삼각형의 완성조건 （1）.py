def solution(sides):
    M = max(sides)
    sides.remove(M)
    if sides[0]+sides[1] > M:
        return 1
    else:
        return 2