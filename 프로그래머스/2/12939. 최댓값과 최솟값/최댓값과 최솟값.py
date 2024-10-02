def solution(s):
    s = s.split(' ')
    a = list(map(int, s))
    return str(min(a))+' '+str(max(a))