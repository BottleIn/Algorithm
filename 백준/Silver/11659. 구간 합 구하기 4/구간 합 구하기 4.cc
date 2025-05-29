#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#define endl "\n"
#define MAX 100000
#define ll long long

using namespace std;

int N, M;
int num[MAX + 2];
int dp[MAX + 2];


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;
	for(int i = 1; i <= N; i++) {
		int a;
		cin >> a;
		if (i == 1) dp[i] = a;
		num[i] = a;
	}
	
	for (int i = 2; i <= N; i++) {
		dp[i] += num[i] + dp[i - 1];
	}

	while (M--) {
		int c, d;
		cin >> c >> d;
		if (c == 1) cout << dp[d] << endl;
		else cout << dp[d] - dp[c - 1] << endl;
	}

	return 0;
}