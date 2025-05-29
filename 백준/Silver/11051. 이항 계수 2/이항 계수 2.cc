	#include <string>
	#include <algorithm>
	#include <queue>
	#include <vector>
	#include <iostream>
	#define endl "\n"
	#define MAX 1001

	using namespace std;
	int N, M, a, b;
	int primeArr[10000];
	long long ans;
	long long DP[MAX][MAX];


	void primeChk() {

		for (int i = 2; i*i <= MAX; i++) {
			if (primeArr[i] == 0) {
				for (int j = i * i; j <= MAX; j += i) {
					primeArr[j] = 1;
				}
			}

		}
	}
	int main() {
		ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
		cin >> N >> M;

		DP[0][0] = 1;
		DP[1][0] = 1;
		DP[1][1] = 1;

		//primeChk();
		for (int i = 2; i <= N; i++)
			for (int j = 0; j <= i; j++)
			{
				if (j == 0) DP[i][0] = 1;
				else if (j == i) DP[i][j] = 1;
				else DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j]) % 10007;
				
			}


		cout << DP[N][M];
		return 0;
	}