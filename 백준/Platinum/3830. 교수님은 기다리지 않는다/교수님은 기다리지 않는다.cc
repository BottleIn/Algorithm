#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 1000000

using namespace std;
int N, M;
int primeArr[1000003];
long long ans;
int a, b, c;
int arr[100001];
long long dis[100001];
char thg;

int find(int tmp) {
	if (arr[tmp] < 0) return tmp;
	//arr[tmp] - find(arr[tmp]);
	int x_temp = find(arr[tmp]);

	dis[tmp] += dis[arr[tmp]];
	return arr[tmp] = x_temp;
}
void myUnion(int x, int y, int W) {
	int xRoot = find(x);
	int yRoot = find(y);
	if (xRoot == yRoot) return;



	dis[yRoot] = (-dis[y]) + dis[x] + W;
	arr[yRoot] = xRoot;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	while (1) {
		cin >> N >> M;
		if (N == 0 && M == 0) return 0;
		for (int i = 1; i <= N; i++) {
			arr[i] = -1;
			dis[i] = 0;
		}

		while (M--) {
			cin >> thg;
			if (thg == '!') {
				cin >> a >> b >> c;
				myUnion(a, b, c);

				/*for (int i = 1; i <= N; i++) {
					cout << i<<" is :: " << arr[i] << " " << dis[i] << endl;
				}
				cout << endl;*/


			}
			else {
				cin >> a >> b;
				if (find(a) == find(b)) cout << dis[b] - dis[a] << endl; // 기준 최신화
				else cout << "UNKNOWN" << endl;
			}
		}

		
	}
	
	return 0;
}