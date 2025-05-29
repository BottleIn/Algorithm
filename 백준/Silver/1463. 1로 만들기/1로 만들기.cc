#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;

int main()
{
	int cases;
	cin >> cases;
	vector<int> dp(cases+1);

	dp[1] = 0;
	dp[2] = 1;
	dp[3] = 1;

	for(int j=4; j<=cases; j++)
	{
		dp[j] = dp[j-1] + 1;
		if(j%2==0) dp[j] = min(dp[j/2]+1,dp[j]);
		if(j%3==0) dp[j] = min(dp[j/3]+1, dp[j]);
	}
	
	cout<<dp[cases]<<"\n";

}