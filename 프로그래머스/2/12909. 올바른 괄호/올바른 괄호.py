def solution(s):
    if len(s) % 2 > 0:
        return False
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if stack:
        return False
    return True