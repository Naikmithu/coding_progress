class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        dist = 0

        for i in range(1,len(arr)-1):

            if arr[i-1]<arr[i]>arr[i+1]:
                l=r=i
                while l>0 and arr[l-1]<arr[l]:
                    l-=1
                while r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                
                dist = max(dist,r-l+1)
        
        return dist
    
    
    #  <Mountain_Peak>    ----^----
    # find the longest distance of the mountain 
    #two -pointer 
    