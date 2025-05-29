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
int arr[1000005];
void primeChk() {

	for (int i = 2; i*i <= MAX; i++) {
		if (primeArr[i] == 0) {
			for (int j = i * i; j <= MAX; j += i) {
				primeArr[j] = 1;
			}
		}

	}
}


int find(int tmp) {
	if (arr[tmp] < 0) return tmp;
	arr[tmp] - find(arr[tmp]);
	return arr[tmp] = find(arr[tmp]);
}
void myUnion(int x, int y) {
	int xRoot = find(x);
	int yRoot = find(y);
	if (xRoot == yRoot) return; 
	arr[xRoot] = yRoot;
}

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	
	for (int i = 0; i <= N; i++) {
		arr[i] = -1;
	}

	while (M--) {
		cin >> a >> b >> c;

		if (!a) {
			myUnion(b, c);
		}
		else {
			if (find(b) == find(c)) cout << "yes" << endl;
			else cout << "no" << endl;
		}
	}
	return 0;
}