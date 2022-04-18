
def solution(answers):
    answer = []
    
    first = 0   # 첫번째 수포자 idx
    second = 1  # 첫번째 수포자 idx
    third = 2   # 첫번째 수포자 idx
    
    # 수포자 정답 갯수 초기화
    supoza_answers_cnt = [0, 0, 0]
        
    # 각 수포자가 찍는 방식
    supoza1 = [1, 2, 3, 4, 5]
    supoza2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supoza3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # 정답 비교하고 맞은 갯수 카운트
    for idx in range(len(answers)):
        if answers[idx] == supoza1[idx%5] :
            supoza_answers_cnt[first]+=1
            
        if answers[idx] == supoza2[idx%8] :
            supoza_answers_cnt[second]+=1
            
        if answers[idx] == supoza3[idx%10] :
            supoza_answers_cnt[third]+=1
        
    # 가장 많이 맞은 갯수를 찾는다.
    max_buff = max(supoza_answers_cnt[first], supoza_answers_cnt[second], supoza_answers_cnt[third])
        
    # 가장 많이 맞은 사람을 찾는다. (오름차순)
    if max_buff == supoza_answers_cnt[0]:
        answer.append(1)
    
    if max_buff == supoza_answers_cnt[1]:
        answer.append(2)
    
    if max_buff == supoza_answers_cnt[2]:
        answer.append(3)
        
    return answer
