# https://programmers.co.kr/learn/courses/30/lessons/64061


inputBoard = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
inputMoves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):

    countBoard = 0
    countScore = 0
    pickUpItem = []
    for indexMoves in moves:
        # print(indexMoves)
        for index1Board in board:
            # print(index1Board)
            if index1Board[indexMoves-1] != 0:
                pickUpItem.append(index1Board[indexMoves-1])
                index1Board[indexMoves-1] = 0
                
                # [4, 3, 1, 1, 3, 2, 4]
                countItem = 0
                prevPickUpItem = 0
                for indexPickUpItem in pickUpItem:
                    if prevPickUpItem == indexPickUpItem:
                        # print('pickUpItem', pickUpItem)
                        # print('countItem', countItem)
                        # print('pickUpItem', pickUpItem[countItem])
                        del pickUpItem[countItem]
                        countScore += 1
                        # print('pickUpItem-1', pickUpItem[countItem-1])
                        del pickUpItem[countItem-1]
                        countScore += 1
                    else:
                        prevPickUpItem = indexPickUpItem
                    
                    countItem += 1
                break
            # print(index1Board[indexMoves+1])

    # print(inputBoard)
    # print(pickUpItem)
    # print(countScore)

    answer = countScore
    return answer

print(solution(inputBoard, inputMoves))

