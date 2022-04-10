# https://programmers.co.kr/learn/courses/30/lessons/67256

# 입력값 > [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
# 기댓값 > "LRLLLRLLRRL"

inputNumbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# inputNumbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# inputNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

inputHand = "right"
# inputHand = "left"
# inputHand = "right"

def index_2d(data, search):
    for i, e in enumerate(data): # enumerate 함수: 해당 배열과 함께 인덱스(0~x)를 for 문으로 돌림
        try:
            return i, e.index(search) #i는 행이 되고, e는 열이 됨
        except ValueError:
            pass
    raise ValueError("{!r} is not in list".format(search))

def solution(numbers, hand):

    prevPositionHandR = [3, 0] # 초기 오른손 포지션
    prevPositionHandL = [3, 2] # 초기 왼손 포지션
    arrayPosition = [] # 출력될 배열
    arrayKeyPad = [ [ 1, 2, 3], [ 4, 5, 6], [ 7, 8, 9], [ '*', 0, '#'] ] # 키패드 배열

    for indexNumber in numbers:
        # 아래 함수는 키패드 배열에서 원하는 인덱스를 찾아주는 함수 ex)키패드 2번일때, [0, 1] 출력 / 키패드 9번일때, [2, 2] 출력
        findIndex = index_2d(arrayKeyPad, indexNumber)

        if findIndex[1] == 0: # 찾은 인덱스가 왼쪽 배열이라면 출력에 L 추가
            arrayPosition.append('L')
            prevPositionHandL = findIndex
        elif findIndex[1] == 2: # 찾은 인덱스가 오른쪽 배열이라면 출력에 R 추가
            arrayPosition.append('R')
            prevPositionHandR = findIndex
        else: # 찾은 인덱스가 중앙쪽 배열이라면
            # 이전에 올려두고 있는 손가락 위치와 비교하여 차이 계산
            tempDifL = abs(findIndex[0] - prevPositionHandL[0]) + abs(findIndex[1] - prevPositionHandL[1])
            tempDifR = abs(findIndex[0] - prevPositionHandR[0]) + abs(findIndex[1] - prevPositionHandR[1])
            
            if tempDifL < tempDifR: # 어느쪽이 가까운지 비교하여 L 또는 R 추가
                arrayPosition.append('L')
                prevPositionHandL = findIndex
            elif tempDifL > tempDifR:
                arrayPosition.append('R')
                prevPositionHandR = findIndex
            else:
                if hand == 'right': # 혹은 같은 거리라면 오른손잡이인지 왼손잡이인지 차이에 따라 판단
                    arrayPosition.append('R')
                    prevPositionHandR = findIndex
                else:
                    arrayPosition.append('L')
                    prevPositionHandL = findIndex

    answer = ''.join(arrayPosition) # 배열을 String 으로

    return answer

print('LRLLLRLLRRL')
# print('LRLLRRLLLRR')
# print('LLRLLRLLRL')
print(solution(inputNumbers, inputHand))