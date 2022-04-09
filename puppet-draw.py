# https://programmers.co.kr/learn/courses/30/lessons/64061


inputBoard = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
inputMoves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):

    countScore = 0 # 점수 스코어
    pickUpItem = [] # 뽑힌 인형 리스트
    for indexMoves in moves: # 어디부터 뽑았나?
        for index1Board in board: # 배열 0 부터 끝까지 확인
            if index1Board[indexMoves-1] != 0: # 해당 확인 배열에서 비어있지 않는다면 픽업 진행
                pickUpItem.append(index1Board[indexMoves-1]) # 픽업
                index1Board[indexMoves-1] = 0 # 해당 위치의 인형은 사라짐
                
                countItem = 0 # 파이선 for 문법이 카운트 확인이 안됨. 따라서 변수 추가
                prevPickUpItem = 0
                for indexPickUpItem in pickUpItem: # 픽업이 되었으니 픽업 리스트 확인 필요.
                    # 전체를 돌리는 이유는 연속으로 터질 수도 있기 때문
                    if prevPickUpItem == indexPickUpItem: # 직전에 픽업된 인형과 현재 인형이 같다면
                        del pickUpItem[countItem] # 픽업 인형 터짐
                        countScore += 1 # 스코어 ++
                        del pickUpItem[countItem-1] # 직전 픽업 인형도 터짐
                        countScore += 1 # 스코어 ++
                    else:
                        prevPickUpItem = indexPickUpItem # 직전 인형 갱신
                    
                    countItem += 1 # 카운터 갱신
                break

    answer = countScore
    return answer

print(solution(inputBoard, inputMoves))

