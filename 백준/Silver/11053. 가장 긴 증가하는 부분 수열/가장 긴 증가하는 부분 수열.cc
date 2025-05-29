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

	cin >> cases;

	for(int i = 1; i <= cases; i++)
	{
		cin >> num[i];
	}
	
	for (int i = 1; i<=cases; i++)
	{
		dp[i] = 1;
		for(int j = i - 1; j>=1; j--)
		{
			if(num[i] > num[j])
			{
				dp[i] = max(dp[i], dp[j]+1);
			}
		}
		temp = max(temp,dp[i]);
	}
	
	cout<<temp;

	return 0;
}