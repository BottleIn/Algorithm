#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
#define Max 1000000000
using namespace std;

int main()
{
	int cases;
	long long dp[101][11];
	long long ans = 0;

	cin >> cases;

	dp[1][0] = 0;

	for(int i=1; i<10; i++)
	{
		dp[1][i] = 1;
	}

	for(int j=2; j<=cases; j++)
	{
		for(int k=0; k<10; k++)
		{
			if(k==0)  {dp[j][k] = dp[j-1][k+1] % Max; continue;}
			if(k==9)  {dp[j][k] = dp[j-1][k-1] % Max; continue;}
			dp[j][k] = (dp[j-1][k-1] + dp[j-1][k+1]) % Max;
		}
	}
	for(int i=0; i<10; i++)
	{
		ans = ans + dp[cases][i];
	}

	cout<< ans % Max <<"\n";

}