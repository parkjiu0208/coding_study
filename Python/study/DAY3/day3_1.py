def solution(a, b):
    a = f"{a}"
    b = f"{b}"
    if int(a+b) < int(b+a):
        return int(b+a)
    else:
        return int(a+b)
    answer = 0
    return answer

print(solution(9,91))

# 다른 사람의 풀이
#  def solution(a, b):
#      return int(max(f"{a}{b}", f"{b}{a}"))
# {a}{b} 이렇게 해서 숫자를 이어붙일 수 있다는 사실을 배움!
# 답이 so 명료...ㅜㅜ 더 노력하자...