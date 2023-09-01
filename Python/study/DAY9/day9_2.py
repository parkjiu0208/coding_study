def solution(my_strings, parts):
    answer = ''
    i=0
    for s, e in parts:
        answer += my_strings[i][s:e+1:1]
        i+=1
    return answer

print(solution(["progressive", "hamburger", "hammer", "ahocorasick"],[[0, 4], [1, 2], [3, 5], [7, 7]]))

#인덱싱과 for문의 구동 방식에 익숙해진 것 같다. 스스로 풀었다!