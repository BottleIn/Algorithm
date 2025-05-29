#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 300001
#define ll long long
const int INF = 0x3f3f3f3f;

using namespace std;
int N, M;
int a, b, w;
long long dis[MAX];
vector<pair<int, int>> indgree[MAX];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
int start;
bool cycle;

void bellman_ford() {
	fill(dis, dis + N + 1, INF); // 변경하려는 원소의 범위 시작주소, 변경하려는 원소 개수, 변경 값
	dis[1] = 0;

	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (auto nexts : indgree[i]) {
				int next = nexts.first;
				int nextcost = nexts.second;

				if (dis[i] != INF && dis[next] > dis[i] + nextcost) {
					dis[next] = dis[i] + nextcost;
					if (k == N) cycle = true;
				}
			}
		}
	}
	if (cycle) cout << -1;
	else {
		for (int i = 2; i <= N; i++)
			cout << (dis[i] != INF ? dis[i] : -1) << "\n";
	}
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		cin >> a >> b >> w;
		indgree[a].push_back({ b, w });
	}

	bellman_ford();

	return 0;
}