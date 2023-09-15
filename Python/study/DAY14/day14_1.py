def solution(arr, queries):
     for s, e in queries:
        for i in range(s,e+1):
            arr[i]+=1
     return arr
print(solution([0, 1, 2, 3, 4],[[0, 1],[1, 2],[2, 3]]))

# 뿌듯하다고 말하기도 지침ㅋㅋ 재밌어용