def solution(arr, idx):
    for i in range(idx,len(arr)+1,1):
        if arr[i] == 1:
            return i
            break
        elif arr[i] == 0:
            if i == len(arr)-1:
                return -1
            else:
                continue


print(solution([0, 0, 0, 1],1))