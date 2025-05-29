#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 100001
#define ll long long
const int INF = 987654321;

using namespace std;
int N, M;
int a, b, w;
int dis[103][103];
vector<pair<int, int>> indgree[MAX];
//priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

int start;
bool cycle;

/*void bellman_ford() {
	fill(dis, dis + N + 1, INF); // 변경하려는 원소의 범위 시작주소, 변경하려는 원소 개수, 변경 값
	dis[1] = 0;

	for (int k = 1; k <= N; k++) {		// 모든 간선 찾기
		for (int i = 1; i <= N; i++) {
			for (auto nexts : indgree[i]) {
				int next = nexts.first;
				int nextcost = nexts.second;

				if (dis[i] != INF && dis[next] > dis[i] + nextcost) {
					dis[next] = dis[i] + nextcost;
					if (k == N) cycle = true;		//다 돌았을 때 업데이트 되면 음수 cycle이 존재한다는 뜻
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
*/
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M;

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (i == j) dis[i][j] = 0;
			else dis[i][j] = INF;
		}
	}

	for (int i = 0; i < M; i++) {
		cin >> a >> b >> w;
		if(dis[a][b] == INF)  dis[a][b] = w;
		else dis[a][b] = min(dis[a][b], w);
		
	}
	/*for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			cout << dis[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
*/

	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j]);
			}
		}
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (dis[i][j] == INF) cout << 0 << " ";
			else cout << dis[i][j] << " ";
		}
		cout << endl;
	}
	//bellman_ford();

	return 0;
}