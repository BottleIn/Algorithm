#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 100001
#define ll long long


/*
DP 버전
*/
using namespace std;
int N, M;
int a, b;
int c, d;
int depth[MAX];
ll parent[MAX][21];;
vector<int> indgree[MAX];

void DFS(int cur) { 
	for (auto next : indgree[cur]) {
		if (depth[next] != -1) continue;
		parent[next][0] = cur;
		depth[next] = depth[cur] + 1;
		DFS(next);
	}
}

int lca(int u, int v) {
	if (depth[u] < depth[v]) swap(u, v);
	int diff = depth[u] - depth[v];
	int j = 0;
	while (diff) {
		if (diff % 2) {
			u = parent[u][j];
		}
		j++;
		diff /= 2;
	}
	if (u != v) {
		for (int j = 20; j >= 0; j--) {
			if (parent[u][j] != parent[v][j]) {
				u = parent[u][j];
				v = parent[v][j];
			}
		}
		u = parent[u][0];
	}
	return u;
}


int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	
	cin >> N;
	for (int i = 1; i <= N; i++) {
		depth[i] = -1;
	}
	memset(parent, -1, sizeof(parent));
	depth[1] = 0;


	for (int i = 1; i < N; i++) {
		cin >> a >> b;
		indgree[a].push_back(b);
		indgree[b].push_back(a);
	}

	DFS(1);
	/*for (int i = 1; i <= N; i++) {
		cout << i << " 깊이 : "<< depth[i] << endl;
	}*/
	
	for (int k = 0; k <= 20; k++) {
		for (int i = 1; i <= N; i++) {
			int tmp = parent[i][k];			// i의 조상	
			if (tmp != -1) {
				parent[i][k + 1] = parent[tmp][k];  // i의 2^k번째 조상 업데이트
			}
		}
	}

	cin >> M;

	while (M--) {
		cin >> c >> d;
		cout << lca(c, d) << endl;
	}
	
	return 0;
}