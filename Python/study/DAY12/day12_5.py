def solution(arr, query):
    answer = []
    for i in range(len(query)):
        if i==0 or i%2 ==0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr
print(solution([0, 1, 2, 3, 4, 5],[4, 1, 2]))

#12일차는 다 쉽지 않다 허허 again 뿌듯