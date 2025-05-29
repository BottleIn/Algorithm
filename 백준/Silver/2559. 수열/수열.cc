#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	
	int num,cnt;
	long temp= -1000000;
	cin >> num >> cnt;
	vector<long> ps(num+1);

	ps[0] =0;
	for(int i=1; i<=num; i++)
	{
		long a;
		cin >> a;
		ps[i] = ps[i-1]+a;
	}
	/*
	for(int i=1; i<=num; i++)
	{
		cout<<ps[i]<<" ";
	}
cout<<"\n";
*/
	for(int i=cnt; i<=num; i++)
	{
		temp=max(temp,ps[i]-ps[i-cnt]);
	}
	cout<<temp;
	return 0;
}