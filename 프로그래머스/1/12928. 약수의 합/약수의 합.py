def solution(n):
    hap = 0
    for i in range(1,n+1):
        if (n/i)==n//i:
            hap+=i
    return hap