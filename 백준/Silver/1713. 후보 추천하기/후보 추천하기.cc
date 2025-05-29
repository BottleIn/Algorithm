#include <iostream>
#include <unordered_map>
#include <queue>
using namespace std;
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int vote[101] = { 0, };
	int in[101] = { 0, };
	int N, M;
	cin >> N >> M;
	int full = 0;

	for (int i = 1; i <= M; i++) {
		int a;
		cin >> a;
		if (full < N) {
			vote[a]++;
			if (in[a]) continue;
			else {
				in[a] = i;
				full++;
			}
		}
		else {
			if (in[a]) { vote[a]++; continue; }
			else {
				int max = 1001;
				int old = 1001;
				int target;

				for (int i = 1; i <= 100; i++) {
					if (vote[i] == max) {
						if (in[i] < old) {
							target = i;
							old = in[i];
							max = vote[i];
						}
					}

					if (vote[i] != 0 && vote[i] < max) {
						max = vote[i];
						old = in[i];
						target = i;
					}
				}


				vote[target] = 0;
				in[target] = 0;
				in[a] = i;
				vote[a]++;
			}
		}
	}

	for (int i = 1; i <= 100; i++) {
		if (in[i]) cout << i << ' ';
	}

	return 0;
}