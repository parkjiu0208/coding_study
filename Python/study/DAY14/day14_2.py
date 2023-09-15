def solution(arr):
    a=0
    for i in arr:
        if i <50 and i%2 != 0:
            arr[a] = i*2
        elif i >= 50 and i%2 == 0:
            arr[a] = i/2
        a+=1
    return arr
print(solution([1, 2, 3, 100, 99, 98]))