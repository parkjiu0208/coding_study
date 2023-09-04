def solution(my_string, is_suffix):
    temp = []
    for i in range(len(my_string)):
        temp.append(my_string[i:])
    if is_suffix in temp:
        return 1
    else:
        return 0
