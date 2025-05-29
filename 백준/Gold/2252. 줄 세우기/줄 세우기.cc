#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 1000000

using namespace std;
int N, M;
int primeArr[1000003];
long long ans;
int a, b, c;
int arr[32001];
vector<int> indgree[32001]; // 간선 정보 저장
queue <int> q;
char thg;



int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> N >> M;
	while (M--) {
		int pre,next;
		cin >> pre >> next;
		arr[next]++; // 앞에 학생 수
		indgree[pre].push_back(next);
	}

	for (int i = 1; i <= N; i++) {
		if (arr[i] == 0) q.push(i);
	}

	while (!q.empty()) {
		int now = q.front();
		q.pop();
		cout << now << " ";
		for (auto ite : indgree[now]) {
			arr[ite]--;
			if (arr[ite] == 0) q.push(ite);
		}
	}
	cout << endl;
	return 0;
}