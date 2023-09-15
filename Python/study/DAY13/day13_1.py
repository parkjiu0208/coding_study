def solution(str_list):
    for i in str_list:
        if i == "l":
            return str_list[:str_list.index("l")]
            break
        elif i == "r":
            return str_list[str_list.index("r"):]
            break
        elif "l" not in str_list and "r" not in str_list:
            return []
            

'''
def solution(str_list):
    for li in str_list:
        if li == 'l':
            return str_list[:str_list.index('l')]
        elif li == 'r':
            return str_list[str_list.index('r')+1:]

-> 이건 동기의 코드. +1을 안한 걸 이 코드 통해서 알았다... ㅠ 한끝차이
'''