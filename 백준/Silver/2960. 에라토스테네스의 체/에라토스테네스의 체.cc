#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
#define endl "\n"
using namespace std;
int N,M;
int arr[1005];

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;

	for (int i = 2; i <= N; i++) {
		arr[i]++;
	}

	cin >> M;
	int k = 2;
	while (1) {
		for (int j = k; j <= N; j = j + k) {
			if (arr[j] != 0) {
				arr[j] = 0;
				M--;
			}
			if (M == 0) {
				cout << j<< endl;
				return 0;
			}
		}
		k++;
	}
		
	

	return 0;
}