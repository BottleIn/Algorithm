#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;
/*
struct meet_time
{
	int start, end;
};

bool cmp(meet_time a, meet_time b)
{
	if(a.end == b.end) return a.start < b.start;
	return a.end < b.end;
}*/

int main()
{
	int n, count = 0;
	cin >> n;
	vector<int> person_time(n);
	vector<int> less_time(n+1 , 0);

	for(int i=0; i<n; i++)
	{
		cin >> person_time[i];
	}
	
	sort(person_time.begin(), person_time.end());

	for(int i=1; i<=n; i++)
	{
		less_time[i] = less_time[i-1] + person_time[i-1];
		count += less_time[i];
	}


	cout<<count;
}