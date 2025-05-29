#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <iostream>
#define endl "\n"
#define MAX 1000000

using namespace std;
int N, M, a, b;
int primeArr[1000003];
long long ans;



void primeChk() {

	for (int i = 2; i*i <= MAX; i++) {
		if (primeArr[i] == 0) {
			for (int j = i * i; j <= MAX; j += i) {
				primeArr[j] = 1;
			}
		}

	}
}
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	//primeChk();
	long long a=1, b=1, c=1;
	for (int i = 1; i <= N; i++) {
		a = a * i;
	}
	for (int i = 1; i <= N-M; i++) {
		b = b * i;
	}
	for (int i = 1; i <= M; i++) {
		c = c * i;
	}
	cout << a / (b * c) << endl;
	return 0;
}