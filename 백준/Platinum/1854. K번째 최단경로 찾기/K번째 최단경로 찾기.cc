#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <set>
#define endl "\n"
#define MAX 100002
#define ll long long
int INF = 987654321;
using namespace std;
typedef pair<int, int> pii;

int V,E;
int N, M;
int kth;
int a, b;
ll w;
int c, d;

struct cmp1 {
	bool operator()(pii a, pii b) {
		return a.second > b.second;
	}
};

struct cmp2 {
	bool operator()(int a, int b) {
		return a < b;
	}
};

vector<pair<ll, int>> indgree[MAX];
priority_queue<pair<int, int>, vector<pair<int, int>>, cmp1> pq; // pq 오름차순
priority_queue<int, vector<int>, cmp2> dist[1001];

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

	cin >> N >> M >> kth;

	for (int i = 0; i < M; i++) {
		cin >> a >> b >> w;
		indgree[a].push_back({ b,w });
	}

	pq.push(make_pair(1,0));

	while (!pq.empty()) {
		int cur = pq.top().first;
		int curD = pq.top().second;	
		pq.pop();
		bool Spread = false;

		if (dist[cur].size() < kth) {
			dist[cur].push(curD);
			Spread = true;
		}
		else if ((dist[cur].size() == kth && dist[cur].top() > curD)) {
			dist[cur].pop();
			dist[cur].push(curD);
			Spread = true;
		}


		if (Spread) {
			for (auto next : indgree[cur]) {
				int ss = next.first;
				int with = next.second;

				pq.push({ss , curD + with });
			}
		}


	}
	
	for (int i = 1; i <= N; i++) {
		if (dist[i].size() < kth) cout << -1 << endl;
		else cout << dist[i].top() << endl;
	}
	return 0;
}