#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 300001
#define ll long long
const int INF = 0x3f3f3f3f;

/*
DP 버전
*/
using namespace std;
int N, M;
int a, b, w;
int dis[MAX];
vector<pair<int, int>> indgree[MAX];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // pq 오름차순
int start;
bool visited[MAX];



int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;
	cin >> start;

	for (int i = 0; i < M; i++) {
		cin >> a >> b >> w;
		indgree[a].push_back({ b, w });
	}

	for (int i = 1; i <= N; i++) {
		visited[i] = false;
	}

	fill(dis, dis + N + 1, INF);

	dis[start] = 0;

	pq.push(make_pair(0, start));

	while (!pq.empty()) {
		int curD = pq.top().first;   // 현재까지의 weight
		int cur = pq.top().second;	 // 현재 목적지
		pq.pop();
		if (visited[cur]) continue;
		visited[cur] = true;

		for (auto next : indgree[cur]) {
			if (dis[next.first] > curD + next.second) {		// 현재까지 weight + 다음 목적지까지 걸리는 weight
				dis[next.first] = curD + next.second;	//갱신값
				pq.push(make_pair(dis[next.first], next.first));  // (거리 갱신값 , 다음 목적지)
			}
		}
	}


	for (int i = 1; i <= N; i++) {
		if (dis[i] == INF) cout << "INF" << endl;
		else cout << dis[i] << endl;
	}


	return 0;
}