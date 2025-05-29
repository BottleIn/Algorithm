#include <iostream>
#include <algorithm>
#include <vector>
#define FAST cin.tie(NULL); ios::sync_with_stdio(false);
using namespace std;

struct meet_time
{
	int start, end;
};

bool cmp(meet_time a, meet_time b)
{
	if(a.end == b.end) return a.start < b.start;
	return a.end < b.end;
}

int main()
{
	int n, count = 0;
	int temp = 0;
	cin >> n;
	vector<meet_time> meets(n);

	for(int i=0; i<n; i++)
	{
		cin >> meets[i].start >> meets[i].end;
	}
	
	sort(meets.begin(), meets.end(), cmp);

	for(int i=0; i<n; i++)
	{
		if(meets[i].start >= temp)
		{
			count++;
			temp = meets[i].end;
		}
	}
	cout<<count;
}