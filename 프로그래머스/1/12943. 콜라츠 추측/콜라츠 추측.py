def solution(num):
    count = 0
    def collatz(n):
        nonlocal count
        if count > 500:
            return -1
        elif n == 1:
            return count
        elif n % 2 == 0:
            count += 1
            return collatz(n/2)
        elif n % 2 != 0:
            count += 1
            return collatz(n*3+1) 
    return collatz(num)