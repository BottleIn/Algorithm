#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;

int main()
{
	int cases;
	int num[10100]= {0, };
	int dp[10100] = {0, };

	cin >> cases;

	for(int i = 1; i <= cases; i++)
	{
		cin >> num[i];
	}
	dp[0] = num[0] = 0;
	dp[1] = num[1];
	dp[2] = num[1] + num[2];

	for(int j=3; j<=cases; j++)
	{
		dp[j] = max(dp[j-1],max(dp[j-2]+num[j],dp[j-3]+num[j-1]+num[j]));
	}
	
	cout<<dp[cases];

	return 0;
}