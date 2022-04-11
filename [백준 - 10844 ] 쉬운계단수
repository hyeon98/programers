#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

typedef long long ll;

int N;
ll DP[110][11];
ll answer;

int main(void)
{
	scanf("%d", &N);

	for (int i = 1;i <= 9;i++) {
		DP[1][i] = 1;
	}

	for (int i = 2;i <= N;i++)
	{
		for (int j = 0;j < 10;j++)
		{
			if (j == 0) {
				DP[i][j] = (DP[i - 1][j + 1]) % 1000000000;
			}
			else if (j == 9) {
				DP[i][j] = (DP[i - 1][j - 1]) % 1000000000;
			}
			else {
				DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j + 1]) % 1000000000;
			}
		}
	}


	for (int i = 0;i < 10;i++) {
		answer += DP[N][i];
	}

	printf("%d", answer % 1000000000);

	return 0;
}
