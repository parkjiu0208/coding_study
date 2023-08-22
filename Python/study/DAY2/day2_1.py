def solution(my_string, overwrite_string, s):
    A = list(my_string)
    B = list(overwrite_string)
    for i in range (len(B)):
        A[s+i] = B[i]
        i+=1
    answer = ("".join(A))
    return answer

solution("He11oWor1d", "lloWorl", 2)