def solution(n, slicer, num_list):
    for i in range(len(num_list)):
        if n == 1:
            return num_list[:slicer[1]+1:]
        elif n == 2:
            return num_list[slicer[0]::]
        elif n == 3:
            return num_list[slicer[0]:slicer[1]+1:]
        elif n == 4 :
            return num_list[slicer[0]:slicer[1]+1:slicer[2]]
        
print(solution(3, [1, 5, 2]	,[1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 재밌당..ㅎㅎ
# a,b,c=slicer 이런 식으로 지정가능하다는 것을 타인의 풀이를 통해 알았다.
'''
def solution(n, slicer, num_list):
    a,b,c=slicer
    for i in range(len(num_list)):
        if n == 1:
            return num_list[:b+1:]
        elif n == 2:
            return num_list[a::]
        elif n == 3:
            return num_list[a:b+1:]
        elif n == 4 :
            return num_list[a:b+1:c]
수정해봄.
'''


