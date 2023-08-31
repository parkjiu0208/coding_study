def solution(my_string, index_list):
    answer = ''
    for i in range (len(index_list)):
        answer += (my_string[index_list[i]])
    return answer

print(solution("cvsgiorszzzmrpaqpe",[16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
#스스로 풀었다는 것이 대견..하다..! 프로그래밍적 사고가 되는 것 같다.