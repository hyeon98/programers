def solution(N, stages):    #N : 전체 스테이지 개수
                            #stages : 현재 멈춰있는 스테이지 번호가 담겨있는 배열
    people_len = len(stages)    #스테이지에 도달한 플레이어 수
    fail = {}   #{}하는 이유는 배열의 인덱스로 출력하라고했음
    for i in range(1, N + 1):
        if people_len != 0: #0이면 어차피 다음 스테이지는 0
            fail[i] = stages.count(i) / people_len #각 스테이지의 실패율
            people_len -= stages.count(i)   #스테이지가 올라갈수록 사람 수 줄어듬
        else:   #clear 할 경우
            fail[i] = 0

    return sorted(fail, key=lambda i: fail[i], reverse=True)
                            #람다식 : 일회용함수(메모리낭비)