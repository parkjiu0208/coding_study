def solution(n, k):
    answer = []
    for i in range(n//k):
        answer.append((i+1)*k)
    return answer

#다른 사람의 풀이 보기에 있는 답을 스스로 썼다는 것이 뿌듯하다. 굿!!