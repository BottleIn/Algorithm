#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
#define endl "\n"
using namespace std;
const long long MAX = 1 << 20;
int N, a, b;
long long arr[2*MAX];
int cnt;
long long tmp;

void update(int idx, long long num) {
	arr[idx] = num;
	while (idx > 1) {
		idx /= 2;
		arr[idx] = arr[idx * 2] + arr[idx * 2 + 1];
	}
}
long long sum(int idx, int NowS, int NowE, int WanS, int WanE) {
	if (NowS > WanE || NowE < WanS) return 0LL; // 원하는 범위 나가리
	if (idx >= tmp) return arr[idx];// 기저 도달 (노드 한 개)

	if (NowS >= WanS && NowE <= WanE) return arr[idx];// 원하는 범위에 쏙 들어옴
	// 쪼개
	int mid = (NowS + NowE) / 2;
	return sum(2 * idx, NowS, mid, WanS, WanE) + sum(2 * idx + 1, mid + 1, NowE, WanS, WanE);
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	//priority_queue<int, vector<int>, greater<int>> pq;
	cin >> N >> a >> b;
	int height = ceil(log2(N));
	tmp = pow(2, height);
	//cout << tmp;
	for (long long i = tmp; i < tmp + N; i++) {
		cin >> arr[i];
	}
	for (long long j = tmp - 1; j >= 1; j--) {
		arr[j] = arr[j * 2] + arr[j * 2 + 1];
	}
	/*
	for (int i = 1; i < tmp * 2; i++) {
		cout << arr[i] << endl;
	}*/

	for (int i = 0; i < a + b; i++) {
		int e, r;
		long long t;
		cin >> e >> r >> t;

		if (e == 1) {
			update(r + tmp - 1, t);
		}
		else {
			cout << sum(1, 1, tmp, r, t) << endl;
		}
	}

	return 0;
}