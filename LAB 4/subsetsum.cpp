#include<bits/stdc++.h>
using namespace std;


void getsum(string str,int depth,int sum, vector<int> visited,vector<int> &arr,int &V)
{


    if(sum == V)
    {
            cout<<str<<endl;
    }
    if(depth >= arr.size()) 
    {
        return;
    }



    for(int i= 0;i<arr.size();i++)
    {
        if(visited[i] == 1) continue;
        visited[i] = 1;
        string temp;
        int tempsum;
        temp = str+"+"+to_string(arr[i]);
        tempsum = sum+arr[i];
        getsum(temp,depth+1,tempsum,visited,arr,V);
        temp = str+"-"+to_string(arr[i]);
        tempsum = sum-arr[i];
        getsum(temp,depth+1,tempsum,visited,arr,V);

    }

    
}


void solve(vector<int> &arr,int V)
{
    vector<int> visited(arr.size(),0);
    for(int i = 0;i<arr.size();i++)
    {
        visited[i] = 1;
        int sum = arr[i];
        string tempsum = "+"+to_string(arr[i]);
        getsum(tempsum,1,sum,visited,arr,V); 
        sum = -arr[i];
        tempsum = "-"+to_string(arr[i]);
        getsum(tempsum,1,sum,visited,arr,V);  
    }
}





int main()
{
    vector<int> arr{2,5,3,-6,-4,3,-3,7,8,1,9,-1,-7};
    int V = 6;
    solve(arr,V);
}