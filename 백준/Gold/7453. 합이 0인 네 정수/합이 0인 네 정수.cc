#include <iostream>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>

/*
mid in the middle
2개씩 조합해서 정렬 => N^2 log(N^20
각각 앞 뒤에서 시작해서 탐색하기
*/

using namespace std;
int N;
long long cnt = 0;
long long arr[4000001][4];
long long tmp1[16000003];
long long tmp2[16000003];
long long left_cnt = 1, right_cnt = 1;

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> N;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 4; j++) {
			int num;
			cin >> num;
			arr[i][j] = num;
		}
	}


	long long k = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			tmp1[k++] = arr[i][0] + arr[j][1];
		}
	}
	k = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			tmp2[k++] = arr[i][2] + arr[j][3];
		}
	}
	sort(tmp1, tmp1 + k);
	sort(tmp2, tmp2 + k);

	//cout << k << endl;

	/*for (int i = 0; i < k; i++) {
		cout << tmp1[i] << " :::: " << tmp2[i] << endl;
	}*/


	long long s = 0;
	long long e = k - 1;

	while (s < k && e >= 0) {
		int sum = tmp1[s] + tmp2[e];
		if (sum == 0) {
			while (tmp1[s] == tmp1[s + 1] && s + 1 < k) {
				left_cnt++;
				s++;
			}

			while (tmp2[e] == tmp2[e - 1] && e - 1 >= 0) {
				right_cnt++;
				e--;
			}


			long long total = (long long) left_cnt * right_cnt;


			if (total != 1) {
				cnt += total;
				s ++;
				e --;
			}
			
			else {
				cnt++;
				s++;
				e--;
			}

			left_cnt = 1;
			right_cnt = 1;
		}
		else if (sum > 0) e--;
		else if( sum < 0) s++;
	}

	cout << cnt << endl;
	return 0;
}
