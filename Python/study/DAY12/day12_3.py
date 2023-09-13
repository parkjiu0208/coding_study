def solution(num_list):
    j = 0
    for i in num_list:
        if i < 0:
            return j
            break
        elif j == len(num_list)-1 and i>=0:
            return -1
        j+=1

print(solution([12, 4, 15, 46, 38, -2, 15]))

#어렵다.. 그치만 해냈다 뿌듯~
