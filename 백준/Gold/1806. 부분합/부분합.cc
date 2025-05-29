#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
using namespace std;
long long arr[100001] = { 0, };
int N, M;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N >> M;
	int i = 0;
	int sum = 0;
	int cnt = 1;
	int min_cnt = 100001;
	for (int j = 0; j < N; j++) {
		int tmp;
		cin >> tmp;
		arr[j] = tmp;
	}
	int left = 0, right= 0;
	sum += arr[left];
	while (left <= right && right <= N) {
		
		if (sum < M) {
			sum += arr[++right];
			cnt++;
		}
		else if (sum >= M) {
			if (min_cnt > cnt) min_cnt = cnt;
			sum -= arr[left++];
			cnt--;
		}
		//cout << sum << ":: " << cnt <<"::"<<min_cnt<< endl;
	}
	if (min_cnt == 100001) {
		cout << 0 << endl;
		return 0;
	}
	cout << min_cnt << "\n";
	return 0;
}


