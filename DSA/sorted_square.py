class Solution(object):
    def sortedSquares(self, nums):
        
        result = [0] * len(nums)
        l,r=0,len(nums)-1
        pos = len(nums)-1

        while l<=r :
            if abs(nums[l])>abs(nums[r]):
                result[pos]=nums[l]**2
                l+=1
            else :
                result[pos]=nums[r]**2
                r-=1
            
            pos-=1
        
        return result


#Optimized : Two pointer approach 
#Time and Space : O(N) & O(N)

# Instead of array result we can use deque colleciton.deque (If there memory constraint then deque can be used since it grows dynamically) 