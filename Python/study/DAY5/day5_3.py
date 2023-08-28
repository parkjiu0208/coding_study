def solution(num_list):
    answer = 0
    multiply = 1
    add = 0
    
    for i in num_list:
        multiply *= i
        add += i
        
    answer = 1 if multiply < add*add else 0
    
    return answer

num_list1 =  [3, 4, 5, 2, 1]
print(solution(num_list1))



# 다른 사람 풀이이다.
# 계속 += 만 쓰다보니 *=과 같은 코드를 쓸 수 있다는 것을 잊었다...!! 그래서 그게 좀 아쉽지만 기억해야겠다.
# for 문에서 in 뒤에 리스트를 넣으면 각 원소가 i 가 된다는 사실을 이제 깨달았다! 이것도 기억해야겠다.