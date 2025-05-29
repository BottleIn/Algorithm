#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <set>
#define endl "\n"
#define MAX 10000
#define ll long long
int INF = 987654321;
using namespace std;
typedef pair<int, int> pii;


int N;

long long num[501][501];
long long dp[501][501];

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		for (int k = 0; k < N; k++) {
			cin >> num[i][k];
			if (i == k) break;
		}
		//cout << endl;
	}

	/*for (int i = 0; i < N; i++) {
		for (int k = 0; k < N; k++) {
			cout<< num[i][k]<<" ";
			if (i == k) continue;
		}
		cout << endl;
	}*/

	dp[0][0] = num[0][0];
	dp[1][0] = num[0][0] + num[1][0];
	dp[1][1] = num[0][0] + num[1][1];


	for (int i = 2; i < N; i++) {
		for (int k = 0; k < N; k++) {		
			if(k-1 >=0) dp[i][k] = num[i][k] + max(dp[i - 1][k], dp[i - 1][k - 1]);
			
			else dp[i][k] = num[i][k] + dp[i - 1][k];
		}
	}
	int mn = -1;
	for (int i = 0; i < N; i++) {
		if (mn < dp[N - 1][i]) mn = dp[N - 1][i];
	}
	cout << mn << endl;
	return 0;
}