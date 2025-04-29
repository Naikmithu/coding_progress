class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        mindiff=float('inf')
        l=0
        sum=0

        for i in range(0,len(nums)):
            sum+=nums[i]

            while sum >= target:
                mindiff=min(mindiff,i-l+1)
                sum-=nums[l]
                l+=1
            
        return 0 if mindiff == float('inf') else mindiff
#sliding window : finding the minimum length of the array that adds up to the target value, once greater than the target value,
# we will remove the leftmost element and check if the sum is still greater than the target value.