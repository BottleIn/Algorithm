#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstring>
#define endl "\n"
#define MAX 1000000
#define ll long long

using namespace std;

int N, M;
int num[MAX + 2];
int dp1[MAX + 2];
int dp2[MAX + 2];

int GCD(int a, int b) {
	if (b == 0) return a;
	return GCD(b, a%b);
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	for(int i = 1;i <= N; i++) {
		int a;
		cin >> a;
		num[i] = a;
	}
	
	for (int i = 1; i <=N; i++) {
		dp1[i] = GCD(dp1[i-1],num[i]);
	}
	for (int i = N; i >= 1; i--) dp2[i] = GCD(num[i], dp2[i + 1]);

	int deletedNum = -1;
	int tmp = 0;


	for (int i = 1; i <= N; i++) {
		int res = GCD(dp1[i - 1], dp2[i + 1]);
		if (tmp < res && (num[i] % res)) {
			tmp = res;
			deletedNum = num[i];
		}
	}

	if (deletedNum == -1) cout << -1;
	else cout << tmp << " " << deletedNum << endl;
	return 0;
}