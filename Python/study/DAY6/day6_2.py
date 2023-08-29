def solution(arr, queries):
    answer = []
    tmp = []
    
    for s, e, k in queries:
        tmp = list(filter(lambda x: x > k, sorted(arr[s:e+1])))
        if len(tmp) > 0:
            answer.append(tmp[0])
        else:
            answer.append(-1)
    
    return answer

arr1=[0, 1, 2, 4, 3]
queries1= [[0, 4, 2],[0, 3, 2],[0, 2, 2]]	
print(solution(arr1, queries1))


# 이해하기 어려움ㅠㅠ