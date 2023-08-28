#eval() 함수는 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수. 이걸 잘 알아야겠다.
#숫자에 str 붙여야만 문자열 변환 가능.. 기억하자.
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))