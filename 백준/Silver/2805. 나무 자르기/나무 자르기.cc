#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
int N, M;
int arr[1000001];

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		long long tree; cin >> tree;
		arr[i] = tree;
	}
	sort(arr, arr + N);
	
	long long max_M = arr[N-1];
	long long min_M = 0;
	//cout << max_M << " " << min_M << "\n";
	while (min_M <= max_M) {
		//if (past_half == half) break;
		//cout << half << endl;
		long long temp = 0;		
		long long half = (max_M + min_M) / 2;
		for (int i = 0; i < N; i++) {
			if (arr[i] - half >= 0) temp += (arr[i] - half);
		}
		if (temp >= M) {
			min_M = half+1;
			//half = (half + max_M) / 2;
			//cout << "A" << endl;

		}
		else if (temp < M) {
			max_M = half-1;
			//half = (half + min_M) / 2;
			//cout << "B" << endl;
		}
	}
	cout << max_M;
	return 0;
}


