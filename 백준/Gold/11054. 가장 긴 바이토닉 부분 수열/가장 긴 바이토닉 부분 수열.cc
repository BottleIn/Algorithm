#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;

int main()
{
	int cases, temp = 0;
	int num[1010]= {0, };
	int dp[1010] = {0, };
	int dp1[1010] = {0, };
	int dp2[1010] = {0, };

	cin >> cases;

	for(int i = 1; i <= cases; i++)
	{
		cin >> num[i];
	}
	
	for (int i = 1; i<=cases; i++)
	{
		for(int j = i - 1; j>=1; j--)
		{
			if(num[i] > num[j])
			{
				dp[i] = max(dp[i], dp[j]+1);
				dp1[i] = dp[i];
			} 
		}
	}

	/*
	for(int i = 1; i <= cases; i++)
	{
		cout<<dp1[i]<<" ";
	}
	cout<<"\n";
	*/

	for(int i = 1; i <= cases; i++)
	{
		dp[i] = 0;
	}

	for(int i = cases; i>=1; i--)
	{
		for(int j = i + 1; j<=cases; j++)
		{
			if(num[i] > num[j])
			{
				dp[i] = max(dp[i], dp[j]+1);
				dp2[i] = dp[i];
			}
		}
	}
	/*
	for(int i = 1; i <= cases; i++)
	{
		cout<<dp2[i]<<" ";
	}
	cout<<"\n";
	*/

	for(int i = 1; i <= cases; i++)
	{
		//cout<<dp[i]<<" ";
		temp = max(temp, dp1[i] + dp2[i]);
	}

	cout<<temp+1;

	return 0;
}