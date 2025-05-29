#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 1000000
#define ll long long


/*
DP 버전
*/
using namespace std;
int N, M;
int primeArr[1000003];
ll ans;
int a, b, c;
int arr[505];
ll dp[505];
ll ans_time[505];
vector<int> indgree[505]; // 간선 정보 저장
queue <int> q;



ll get_dp(int a) {
	ll& tmp = dp[a];
	if (tmp != 0) return tmp;

	tmp = ans_time[a];
	ll preCost = 0;
	for (auto next : indgree[a]) {
		preCost = max(preCost, get_dp(next));
	}
	tmp += preCost;
	return tmp;
}


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> ans_time[i];
		while (1) {
			int pre;
			cin >> pre;
			if (pre == -1) break;
			indgree[i].push_back(pre);
		}
		
	}

	for (int j = 1; j <= N; j++) {
		cout << get_dp(j) << endl;
	}
	return 0;
}