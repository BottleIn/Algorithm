#include <string>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <vector>
#include <iostream>
#define endl "\n"
using namespace std;
int N, M, a, b;

//const int dy[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
//const int dx[] = { 0, 1, 1, 1, 0, -1, -1, -1 };

int x3, y3;
int tmp;

int GCD(int x, int y) {
	while (y) {
		int r = x % y;
		x = y;
		y = r;
	}
	return x;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	while (N--) {
		int K, C;
		int a;
		cin >> C >> K;   //순서 변경
		a = C;

		if (GCD(K, C) != 1) {
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		if (K == 1) {
			if (C >= 1000000000) { cout << "IMPOSSIBLE\n"; continue; }
			else cout << C + 1 << "\n";
			continue;
		}
		else if (C == 1) {
			cout << 1 << "\n";
			continue;
		}
		int x1 = 1, y1 = 0, x2 = 0, y2 = 1;
		tmp = K % C;

		while (tmp != 0) {
			int q = K / C;

			x3 = x1 - (q * x2);
			y3 = y1 - (q * y2);
			x1 = x2; y1 = y2;
			x2 = x3; y2 = y3;
			//tmp = K % C;
			K = C;
			C = tmp;
			tmp = K % C;
		}
		while (x2 < 0) {
			x2 += a;
		} // 해가 음수가 될 수도 있기 때문에 
		//처음 입력받은 C(명수)(입력 순서가 바뀐 거 같아요!)를 계속해서 0보다 커질 때까지 더해주시면 됩니다. 
		if (x2 > 1000000000 || x2 == 0) { cout << "IMPOSSIBLE\n"; continue; }
		cout << x2 << endl;
	}
	return 0;
}