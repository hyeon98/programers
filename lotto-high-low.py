# https://programmers.co.kr/learn/courses/30/lessons/77484

inputLottos = [44, 1, 0, 0, 31, 25]
inputWinNums = [31, 10, 45, 1, 6, 19]
result = [3, 5]

# inputLottos = [0, 0, 0, 0, 0, 0]
# inputWinNums = [38, 19, 20, 40, 15, 25]
# result = [1, 6]

# inputLottos = [45, 4, 35, 20, 3, 9]
# inputWinNums = [20, 9, 3, 45, 4, 35]
# result = [1, 1]

def solution(lottos, win_nums):

    set1 = set(lottos) # 집합으로 만들어줌. 유니크한 값을 가지게 됨.
    set2 = set(win_nums)

    countBlank = 0
    for index in lottos: # 입력된 로또숫자중 빈칸을 세기 위해 실행
        if index == 0:
            countBlank += 1

    scoreMinimum = len(set1 & set2) # 교집합을 구한 이후 교집합의 숫자를 구함. 즉 최소 맞춘 갯수
    scoreMaximum = scoreMinimum + countBlank # 최대 맞춪 갯수는 [최소 갯수 + 빈칸 갯수], 빈칸 갯수를 당첨 숫자로 바꾸면 되기 때문

    # 순위      당첨 내용
    # 1        6개 번호가 모두 일치
    # 2	       5개 번호가 일치
    # 3	       4개 번호가 일치
    # 4	       3개 번호가 일치
    # 5	       2개 번호가 일치
    # 6(낙첨)	그 외
    rankMinimum = 0
    rankMaximum = 0
    if scoreMinimum == 6: # 맞춘 갯수를 순위로 변환
        rankMinimum = 1
    elif scoreMinimum == 5:
        rankMinimum = 2
    elif scoreMinimum == 4:
        rankMinimum = 3
    elif scoreMinimum == 3:
        rankMinimum = 4
    elif scoreMinimum == 2:
        rankMinimum = 5
    else:
        rankMinimum = 6

    if scoreMaximum == 6:
        rankMaximum = 1
    elif scoreMaximum == 5:
        rankMaximum = 2
    elif scoreMaximum == 4:
        rankMaximum = 3
    elif scoreMaximum == 3:
        rankMaximum = 4
    elif scoreMaximum == 2:
        rankMaximum = 5
    else:
        rankMaximum = 6

    answer = [rankMaximum, rankMinimum]
    return answer

print(result)
print(solution(inputLottos, inputWinNums))