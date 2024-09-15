def solution(s):
    x_count, xx_count, cnt = 0, 0, 0
    for i in s:
        if x_count == xx_count:
            cnt +=1
            x=i
        if x==i:
            x_count +=1  
        else:
            xx_count+=1
    return cnt