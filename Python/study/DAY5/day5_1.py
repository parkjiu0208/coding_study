def solution(num_list):
    even=''
    odd=''
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even+=str(num_list[i])
        else:
            odd+=str(num_list[i])
    result = int(even)+int(odd)
    return result
#리스트를 문자열로 가져오는 것을 알게 되었음.
#빈 문자열을 만든 후, 리스트 값을 문자열로 변환하여 빈 문자열에 넣기.