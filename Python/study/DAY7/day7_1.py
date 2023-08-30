def solution(start_num, end_num):
    result = []
    for i in range(start_num,end_num+1):
        result.append(i)
    return result

print(solution(3,10))

#def solution(start, end):
#    return list(range(start, end + 1))
# 다른 사람의 풀이. list 안에 range 함수를 써서 리스트 생성이 가능하다는 것을 알게 되었음.