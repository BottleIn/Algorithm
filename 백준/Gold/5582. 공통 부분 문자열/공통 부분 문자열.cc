#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#define endl "\n"
#define MAX	4000

using namespace std;
int dp[MAX+2][MAX+2];

int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	string word1, word2;
	cin >> word1 >> word2;
	int ans = 0;

	for (int i = 1; i <= word2.size(); i++) {
		for (int j = 1; j <= word1.size(); j++) {

			if (word2[i - 1]== word1[j-1]) {
				if(dp[i-1][j-1] == 0) dp[i][j]++;
				else dp[i][j] = 1 + dp[i - 1][j - 1];

				ans = max(ans, dp[i][j]);
			}
		}
	}

	cout << ans << endl;
}