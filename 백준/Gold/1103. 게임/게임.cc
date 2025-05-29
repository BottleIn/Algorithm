#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int N, M, answer = 0;
int map[50][50];
bool visit[50][50] = { false, };
int dp[50][50];

int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };

int DFS(int x, int y) {
	if (x < 0 || y < 0 || x >= N || y >= M || map[x][y] == 0)	return 0;

	if (visit[x][y] == true) {
		cout << -1 << endl;
		exit(0);
	}

	if (dp[x][y] != -1)
		return dp[x][y];

	visit[x][y] = true;
	dp[x][y] = 0;

	for (int i = 0; i < 4; i++) {

		int nx = x + (map[x][y] * dx[i]);
		int ny = y + (map[x][y] * dy[i]);

		dp[x][y] = max(dp[x][y], DFS(nx, ny) + 1);
	}

	visit[x][y] = false;

	return dp[x][y];

}


int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		string str;
		cin >> str;

		for (int j = 0; j < M; j++) {

			dp[i][j] = -1;

			if (str.at(j) == 'H')
				map[i][j] = 0;
			else
				map[i][j] = str.at(j) - '0';

		}
	}

	answer = DFS(0, 0);

	cout << answer << endl;

	return 0;
}
