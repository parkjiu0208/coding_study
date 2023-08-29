def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        if numLog[i+1] - numLog[i] == 1:
            answer += 'w'
        elif numLog[i+1] - numLog[i] == -1:
            answer += 's'
        elif numLog[i+1] - numLog[i] == 10:
            answer += 'd'
        elif numLog[i+1] - numLog[i] == -10:
            answer += 'a'
    return answer
numLog1 = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]
print(solution(numLog1))
#혼자 힘으로 해결해서 뿌듯!!