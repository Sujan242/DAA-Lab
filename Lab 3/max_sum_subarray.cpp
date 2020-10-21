// https://leetcode.com/problems/maximum-subarray/submissions/
class Solution {
public:
    
    int divide(vector<int> &a ,int l,int r )
    {
        if(l==r)
        {
            return a[l];
        }
        if(l>r)
        {
            return INT_MIN;
        }
        int mid=(l+r)/2;
        
        int left = divide(a, l , mid-1);
        int right = divide(a , mid+1 , r);
        int left_sum=0;
        int right_sum=0;
        int max_left_sum=INT_MIN;
        int max_right_sum=INT_MIN;
        for(int j=mid;j>=l;j--)
        {
            left_sum+=a[j];
            max_left_sum=max(max_left_sum , left_sum);
        }
        
        for(int j=mid+1;j<=r;j++)
        {
            right_sum+=a[j];
            max_right_sum=max(max_right_sum , right_sum);
        }
        int mid_included = max(max_left_sum , max_left_sum+max_right_sum);
        
        return max(mid_included , max(left,right));
    }
    int maxSubArray(vector<int>& nums) {
        return divide(nums , 0 , nums.size()-1);
    }
};