def solution(nums):
    get = len(nums)/2
    a = set(nums)
    if len(a)>=get:
        return get
    else:
        return len(a)