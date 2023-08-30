def solution(l, r):
    answer = []
    for i in range(l,r+1):
        if all(num in ['0', '5'] for num in str(i)):
            answer.append(i)
            
    if len(answer) == 0:
        answer.append(-1)
        
    return answer

"""
도대체 어떻게 혼자 풀지.. ㅜㅜ 나중에 다시 풀어봐야겠다.
어쨌거나 all 함수라는 것을 알았다. 괄호 안에 것이 참일 때만 결과값을 반환하는 함수.
"""