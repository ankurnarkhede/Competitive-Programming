
#include<iostream>
#include<stack>
#include<climits>
#define longg long long
using namespace std;

longg sub(longg *arr, longg n)
{
	stack<longg> s;
	longg min = INT_MAX;
	s.push(-1);
	for(longg i=n-1; i>=0; i--)
	{
		if(arr[i]<min)
		{
			s.push(i);
			min = arr[i];
		}
	}
	longg maxcnt = 0;
	longg j = s.top();
	s.pop();
	for(longg i=0; i<n; i++)
	{
		while( j!=-1 && (arr[i]>arr[j] || j<=i) )
		{
			if(j-i+1 >maxcnt)
			{
				maxcnt = j-i+1;
			}
			j = s.top();
			s.pop();
		}
		if(j == -1)
		{
			return maxcnt;
		}
	}
}


int main()
{
	longg t;
	cin>>t;
	while(t--)
	{
		longg n;
		cin>>n;
		longg arr[n];
		for(longg i=0; i<n; i++)
		{
			cin>>arr[i];
		}
		cout<<sub(arr, n)<<endl;
	}
	return 0;
}