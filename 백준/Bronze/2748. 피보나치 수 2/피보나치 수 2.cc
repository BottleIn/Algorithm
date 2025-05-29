#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
long long fb[10000];
long long N;

int main() {
	fb[0] = 0; fb[1] = 1; fb[2] = 1;
	cin >> N;
	for (int i = 3; i <= N; i++) {
		fb[i] = fb[i - 2] + fb[i - 1];
	}
	cout << fb[N];
	return 0;
}


