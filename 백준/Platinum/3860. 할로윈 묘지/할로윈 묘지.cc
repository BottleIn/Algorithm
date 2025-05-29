#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <set>
#define endl "\n"
#define MAX 900
#define ll long long
int INF = 987654321;
using namespace std;
typedef pair<int, int> pii;

int W, H, G, E;
int dx[] = { -1,1,0,0 };
int dy[] = { 0,0,-1,1 };
int dis[MAX + 1];
vector<pair<int, int>> indgree[MAX + 1];
set<int> myoji;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	while (1) {
		myoji.clear();
		for (int i = 0; i <= MAX; i++) {
			dis[i] = INF;
			indgree[i].clear();
		}

		cin >> W >> H;
		if (W == 0 && H == 0) break;
		int NUM = W * H;
		cin >> G;

		for (int i = 0; i < G; ++i) {
			int x, y;
			cin >> x >> y;
			myoji.insert(y*W + x);
		}

		cin >> E;
		for (int i = 0; i < E; ++i) {
			int x1, x2, y1, y2, time;
			cin >> x1 >> y1 >> x2 >> y2 >> time;
			int From = (y1*W) + x1;
			int To = (y2*W) + x2;
			indgree[From].push_back(pii(To, time));
		}


		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++) {
				int from = j * W + i;
				if (myoji.count(from)) continue; // 묘지 위치인 경우 출발 추가 X
				if (!indgree[from].empty()) continue; // 귀신 구멍인 경우 출발 추가 X
				if (NUM - 1 == from) continue; // 도착점인 경우 출발 추가 X

				for (int k = 0; k < 4; k++) {
					int nx = i + dx[k];
					int ny = j + dy[k];
					if (nx < 0 || nx >= W || ny < 0 || ny >= H) continue;
					int to = ny * W + nx;
					if (myoji.count(to)) continue; // 묘지 위치인 경우 도착 X
					indgree[from].push_back({ to,1 });
				}
			}
		}

		dis[0] = 0;
		bool cycle = false;
		for (int k = 0; k <= NUM; ++k) {
			for (int i = 0; i <= NUM; ++i) {
				if (dis[i] == INF) continue;

				for (auto next : indgree[i]) {
					int v = next.first; // 다음 노드
					int w = next.second; // 다음 노드까지 가는 비용
					if (dis[v] > dis[i] + w) {
						if (k == NUM) cycle = true;
						dis[v] = dis[i] + w;
					}
				}
			}
		}


		if (cycle) cout << "Never" << endl;
		else if (dis[NUM - 1] == INF) cout << "Impossible" << endl;
		else cout << dis[NUM - 1] << endl;
	}



	return 0;
}