#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef long long ll;
#define TEN_BILLION 1000000000
#define MAX_LEN 100	// 길이는 100개
#define START_NUM_SIZE 10

#define LEN_SIZE_IS_ONE 1

int N;
ll All_Stair_Number_DP[MAX_LEN + 10][START_NUM_SIZE + 1]; // 에러 방지를 위한 배열 길이 조정
ll answer;

int main(void)
{
	//첫째 줄에 N이 주어진다.N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.
	scanf("%d", &N);

	// 초항 설정
	/*
	* 길이가 1일 때, 나오는 총 계단수
	* All_Stair_Number_DP : 맨 처음에 오는 수에 따른 경우의 수를 저장
	* startNumber : 시작 숫자 (1~9)
	* 길이가 1이면 시작 숫자 하나로 하나의 계단 수를 만들 수 있다.(시작 수가 0인건 고려X)
	*/
	for (int startNumber = 1;startNumber <= 9;startNumber++) {
		All_Stair_Number_DP[LEN_SIZE_IS_ONE][startNumber] = 1;
	}

	// 점화식(Bottom-Up 방식)
	// 시작 숫자 startNumber
	/*
	* 앞에 있는 숫자가 0이면, 다음 계단수 한 개를 만들 수 있다.(1)
	* 앞에 있는 숫자가 1이면, 다음 계단수 두 개를 만들 수 있다.(0,1)
	* 앞에 있는 숫자가 2이면, 다음 계단수 두 개를 만들 수 있다.(1,3)
	* ...
	* 앞에 있는 숫자가 8이면, 다음 계단수 두 개를 만들 수 있다.(7,9)
	* 앞에 있는 숫자가 9이면, 다음 계단수 두 개를 만들 수 있다.(8)
	* 
	* 
	* 다음에 나올 숫자는 전에 있는 숫자에서 나올 수 있는 경우의 수
	* 
	* DP[2][3]은 길이가 2이고, 계단수의 마지막 수가 3일 때 나올 수 있는 경우의 수이다.
	* ex) 23, 43
	* DP[3][3]은 길이가 3이고, 계단수의 마지막 수가 3일때 나올 수 있는 경우의 수.
	* ex) 123 323 343 543 => 4가지
	* DP[3][8]은 길이가 8이고, 계단수의 마지막 수가 8일때 나올 수 있는 경우의 수.
	* ex) 678 878 898 => 3가지
	* 
	* 계단수의 마지막 수가 N인 경우의 수는 그 이전 길이의 마지막 계단수가 N-1 or N+1 여야만 함.
	* 이거 0~9까지 돌리면 모든 길이가 N일 때 나올 수 있는 총 계단수 구할 수 있음.
	* 
	* 
	* * 시작숫자가 1이면 0,2로 시작하는 계단수 만들기 가능
	* DP[2][0] = DP[1][1]
	* DP[2][1] = DP[1][0] + DP[1][2]
	* 1 -> 10 12 -> 101 121 123 -> 1010 1012 1210 1212 1232 1234
	* DP[1][1] = 1-> DP[2][0] DP[2][2] -> DP[3][1] DP[3][2] DP[3][3]
	* 2 -> 21 23 -> 210 212 232 234
	* DP[1][2] = 1 -> DP[2][1] DP[2][3]
	* 
	*/

	for (int len = 2;len <= N;len++) // 길이가 2일때부터(길이가 1일때 결과 가져와서 씀)
	{
		for (int lastNumber = 0;lastNumber < 10;lastNumber++) // 길이 2부터는 계단 수 마지막 수가 0일 될 수 있음
		{
			if (lastNumber == 0) {
				// 지금 마지막 수가 0에서 파생되는 값은 "1만큼 짧은 길이"의 마지막 수가 8일때만 파생될 수 있음.
				All_Stair_Number_DP[len][lastNumber] = (All_Stair_Number_DP[len - 1][lastNumber + 1]) % TEN_BILLION;
			}
			else if (lastNumber == 9) {
				// 지금 마지막 수가 9에서 파생되는 값은 "1만큼 짧은 길이"의 마지막 수가 8일때만 파생될 수 있음.
				All_Stair_Number_DP[len][lastNumber] = (All_Stair_Number_DP[len - 1][lastNumber - 1]) % TEN_BILLION;
			}
			else {
				// 지금 마지막 수가 0, 9가 아닐 때 파생되는 값은 "1만큼 짧은 길이"의 마지막 수의 +1, -1 일때만 파생될 수 있음.
				All_Stair_Number_DP[len][lastNumber] = (All_Stair_Number_DP[len - 1][lastNumber - 1] + All_Stair_Number_DP[len - 1][lastNumber + 1]) % TEN_BILLION;
			}
		}
	}

	for (int i = 0;i < 10;i++) {
		answer += All_Stair_Number_DP[N][i];
	}

	printf("%lld", answer % 1000000000);

	return 0;
}
