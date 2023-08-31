def solution(a, b, c, d):
    answer = 0
    origin = [a, b, c, d]
    arr = list(set(origin))
    
    if len(arr) == 4:
        answer = min(arr)
    elif len(arr) == 3:
        p = max(origin, key=origin.count)
        tmp = [num for num in arr if num != p]
        answer = tmp[0] * tmp[1]
    elif len(arr) == 2:
        if max([origin.count(num) for num in arr]) > 2:
            p = max(origin, key=origin.count)
            q = min(origin, key=origin.count)
            answer = pow(((10 * p) + q), 2)
        else:
            answer = ((arr[0] + arr[1]) * abs(arr[0] - arr[1]))  
    elif len(arr) == 1:
        answer = int(str(arr[0]) * 4)
    
    return answer


#set이라는 것을 이런 식으로 사용할 수 있다는 사실을 처음 알았다. 중복을 허용하지 않는다는 특성을 이렇게 활용하다니. 다음에 다시 한 번 풀어봐야겠다.