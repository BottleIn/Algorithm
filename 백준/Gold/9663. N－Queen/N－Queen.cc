#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;

int N, ans = 0;
int chess[15][15];
bool CH(int a, int b) {
	int x = a;
	int y = b;
	while (x > 0) { //column 바로 위
		x--;
		if (chess[x][y] == 1) return false;
	}
	x = a;
	y = b;
	while (x > 0 && y > 0) { //왼쪽 대각선
		x--;
		y--;
		if (chess[x][y] == 1) return false;
	}
	x = a;
	y = b;
	while (x > 0 && y < N) { // 오른쪽 대각선
		x--;
		y++;
		if (chess[x][y] == 1) return false;
	}
	return true;
}
void queen(int x) {
	if (x == N) {
		ans++;
		return;
	}
	for (int i = 0; i < N; i++) {
		if (CH(x, i)) {
			chess[x][i] = 1;
			queen(x + 1);
			chess[x][i] = 0;
		}
	}
}
int main() {
	ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
	cin >> N;
	queen(0);
	cout << ans;
	return 0;
}


