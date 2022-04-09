# https://programmers.co.kr/learn/courses/30/lessons/67256

# 입력값 > [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"
# 기댓값 > "LRLLLRLLRRL"

inputNumbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
inputHand = "right"

def solution(numbers, hand):

    prevIndexNumber = 0
    positionHandR = 0
    positionHandL = 0
    arrayPosition = []
    for indexNumber in numbers:
        if indexNumber == 1 or indexNumber == 4 or indexNumber == 7:
            # print('L', end='')
            arrayPosition.append('L')
            positionHandL = indexNumber
        elif indexNumber == 3 or indexNumber == 6 or indexNumber == 9:
            # print('R', end='')
            arrayPosition.append('R')
            positionHandR = indexNumber
        else:
            # print('M', end='')
            arrayPosition.append('M')
        prevIndexNumber = indexNumber

    tempStr = ''.join(arrayPosition)
    answer = tempStr
    return answer

# solution(inputNumbers, inputHand)
print('LRLLLRLLRRL')
print(solution(inputNumbers, inputHand))