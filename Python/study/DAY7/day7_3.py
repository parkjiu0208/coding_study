def solution(arr):
    stk = []
    i = 0
    while i<len(arr):
        if i < len(arr):
            if stk ==[]:
                stk.append(arr[i])
                i+=1
            elif stk != [] and stk[-1] < arr[i]:
                stk.append(arr[i])
                i+=1
            elif stk !=[] and stk[-1] >= arr[i]:
                stk.pop()
    return stk

arr1 = [1, 4, 2, 5, 3]
print(solution(arr1))

#혼자 힘으로 풀다니..감격. stk == [] 써도 되고, len(stk) == 0 이런 식으로 써도 된다는 사실을 알게 되었음.