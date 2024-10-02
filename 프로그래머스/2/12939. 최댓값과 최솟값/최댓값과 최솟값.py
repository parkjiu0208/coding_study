def solution(s):
    answer = ''
    s = s.split(' ')
    a = list(map(int, s))
    answer += str(min(a))+' '
    answer += str(max(a))
    return answer