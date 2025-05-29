#include <cstring>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#include <set>
#define endl "\n"
#define MAX 500
#define ll long long
int INF = 987654321;
using namespace std;
typedef pair<int, int> pii;

int dis[MAX+2][MAX+2];
vector<pair<int, int>> indgree[MAX];
int N, M;
int a, b, w;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (i == j) dis[i][j] = 0;
			else dis[i][j] = INF;
		}
	}

	while (M--) {
		cin >> a >> b;
		dis[a][b] = 1;
	}

	for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				dis[i][j] = min(dis[i][k] + dis[k][j], dis[i][j]);
			}
		}
	}
	/*for (int k = 1; k <= N; k++) {
		for (int i = 1; i <= N; i++) {
			cout << dis[k][i] << " ";
		}
		cout << endl;
	}*/


	int ans = 0;
	for (int i = 1; i <= N; i++) {
		int count = 0;
		int k = 1;

		while (k <= N) {
			//cout << k << endl;
			if (dis[i][k] == INF) {
				k++;
				continue;
				//cout << "A" << endl;
			}
			else count++;
			k++;
		}

		k = 1;
		while (k <= N) {
			if (dis[k][i] == INF) {
				k++;
				continue;
			}
			if (i == k) {
				k++; continue;
			}
			else count++;
			k++;
			//cout << "B" << endl;
		}

		//cout << count << endl;
		if (count == N) ans++;
	}
		cout<< ans << endl;
	
	return 0;
}