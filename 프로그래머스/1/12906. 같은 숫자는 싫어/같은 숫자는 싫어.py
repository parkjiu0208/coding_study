def solution(arr):
    answer = [arr[0]]
    j=0
    for i in range(1, len(arr)):
        if arr[i] != answer[j]:
            answer.append(arr[i])
            j+=1
    return answer