#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;

int main()
{
	int cases,temp;
	int num[301]= {0, };
	int dp[301] = {0, };

	cin >> cases;

	for(int i = 1; i <= cases; i++)
	{
		cin >> num[i];
	}

	dp[1] = num[1];
	dp[2] = num[1] + num[2];
	dp[3] = max(num[1]+num[3],num[2]+num[3]);

	for(int j=4; j<=cases; j++)
	{
		dp[j] = max(dp[j-2]+num[j],dp[j-3]+num[j-1]+num[j]);
	}
	
	cout<<dp[cases]<<"\n";

	return 0;
}