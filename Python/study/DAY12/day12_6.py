def solution(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i]==2:
            answer=(arr[i:])
            break
    if answer == []:
        return [-1]
    else:    
        while answer[-1]!=2:
            answer.pop()
        return answer

print(solution([1, 2, 1, 4, 5, 2, 9]))

#끝까지 포기하지 않고 나만의 풀이법 만들기. 뿌듯하다.~~
