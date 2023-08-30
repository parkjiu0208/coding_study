def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        for i in range(s,e+1):
            if i%k == 0:
                arr[i]+=1
    
    return arr


#수열과 구간 쿼리를 거의 혼자 풀다니... 감격!!!!  생각보다 그리 어렵지 않을 수도. 히힛