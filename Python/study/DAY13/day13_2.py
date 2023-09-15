def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        temp = myString[i:i+(len(pat))]
        if temp == pat:
            answer += 1
    return answer
        
print(solution("banana","ana"))
# 진짜 어려웠는데 생각보다.. 쉬웠다... 쉽게 생각할 것.!