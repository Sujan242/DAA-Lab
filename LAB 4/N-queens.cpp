#include<bits/stdc++.h>
using namespace std;
void fun(vector<int> v,int i)
{
	if(i==v.size())
	{
        for(int i=0;i<v.size();i++)
        {
            cout<<v[i]<<" ";

        }
        cout<<endl;
		return ;
	}
	for(int j=0;j<v.size();j++)
	{
		int flag=0;
		for(int k=0;k<i;k++)
		{
			if(v[k]==j || abs(v[k]-j)==abs(k-i))
			{
				flag=1;
                break;
			}
		}
		if(flag==0)
		{
			v[i]=j;
			fun(v,i+1);
		}
	}
}


void fun(int N)
{
    vector<int> arr(N,0);
    fun(arr,0);
}
int main()
{
	int n;
	cin>>n;
	fun(n);
	return 0;
}