"""
def solution(a, b):
    temp=2*a*b
    if f"{a}{b}" < f"{temp}":
        return 2*a*b
    else:
        return int(f"{a}{b}")

    이게 내 코드였는데... 맞을 때도, 틀릴 때도 있었다. 이유가 뭘까ㅜㅜ
"""
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

print(solution(2,91))

#아 왜 이렇게 했는데 난 안돼? 그치만 하다보면 나도 잘 되겠지..!