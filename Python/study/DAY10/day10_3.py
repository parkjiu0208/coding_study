def solution(my_string):
    answer = [0 for i in range(52)]
    for string in my_string:
        if string.isupper(): k = 65
        else: k = 71
        answer[ord(string)-k] += 1
    return answer

print(solution("Programmers"))

#도저히 모르겠다. 다시 풀어야 해서 적는다. 문제 - 문자 개수 세기