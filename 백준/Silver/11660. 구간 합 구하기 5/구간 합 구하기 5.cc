#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#define endl "\n"
#define MAX 1024
#define ll long long

using namespace std;

int N, M;
int num[MAX + 2][MAX+2];
int dp[MAX + 2][MAX + 2];


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			int a;
			cin >> a;
			if (j == 1) dp[i][j] = a;
			num[i][j] = a;
		}
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 2; j <= N; j++) {
			dp[i][j] = dp[i][j - 1] + num[i][j];
		}
	}

	while (M--) {
		int x1, y1, x2, y2,ans = 0;
		cin >> x1 >> y1 >> x2 >> y2;
		int min_y = min(y1, y2);
		int max_y = max(y1, y2);
		for (int tmp = x1; tmp <= x2; tmp++) {
			//int dp1 = dp[x1][max_y] - dp[x1][min_y - 1];
			//int dp2 = dp[x2][max_y] - dp[x2][min_y - 1];
			ans += dp[tmp][max_y] - dp[tmp][min_y - 1];
		}
		
		//ans += dp[tmp][max_y] - dp[tmp][min_y - 1];


		//if (x1 == x2 && y1 == y2) cout << ans / 2 << endl;
		cout << ans << endl;
	}

	return 0;
}