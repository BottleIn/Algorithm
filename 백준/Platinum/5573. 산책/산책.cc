#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#define MOD 100000

using namespace std;

#define ll long long

int dp[1003][1003];
int dp2[1003][1003];
int w, h;
int goal;
int goal_x, goal_y;
int main() {
	ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	cin >> w >> h >> goal;

	//input
	for (int i = 1; i <= w; i++) {
		for (int j = 1; j <= h; j++) {
			int a;
			cin >> a;
			if (a == 1)	//오른쪽
				dp[i][j] = 1;
			else if (a == 0) //아래
				dp[i][j] = 0;
		}
	}
	
	

	/*for (int i = 1; i <= w; i++) {
		for (int j = 1; j <= h; j++) {
			cout << dp[i][j];
		}
		cout << endl;
	}
	cout << endl;*/

	int x = 1, y = 1;
	
	dp2[1][1] = goal - 1;
	

	//업데이트
		for (int x = 1; x <= w; x++) {
			for (int y = 1; y <= h; y++) {
				//if (x == 1 && y == 1) continue;
				dp2[x][y + 1] += dp2[x][y] / 2;
				dp2[x + 1][y] += dp2[x][y] / 2;

				if (dp2[x][y] % 2 == 1) {
					if(dp[x][y] == 1) dp2[x][y+1]++;
					else if (dp[x][y] == 0) dp2[x+1][y]++;
				}
			}
		}


		/*for (int i = 1; i <= w; i++) {
			for (int j = 1; j <= h; j++) {
				cout << dp2[i][j];
			}
			cout << endl;
		}
		cout << endl;*/



		for (int i = 1; i <= w; i++) {
			for (int j = 1; j <= h; j++) {
				//if (i == 1 && j == 1) continue;

				if (dp2[i][j] % 2 == 1) {		//홀수면 방향 바꾸기
					if (dp[i][j] == 0) dp[i][j] = 1;
					else if (dp[i][j] == 1) dp[i][j] = 0;
				}
			}
		}


		/*for (int i = 1; i <= w; i++) {
			for (int j = 1; j <= h; j++) {
				cout << dp[i][j];
			}
			cout << endl;
		}*/


		goal_x = 1; goal_y = 1;
		//cout << w << h << endl;


		while (goal_x <= w && goal_y <= h) {
			if (dp[goal_x][goal_y] == 1) goal_y++;
			else goal_x++;
			//cout << goal_x << " " << goal_y << endl;
			
		}
		cout << goal_x << " " << goal_y;
		
	return 0;
}