class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """

        mindiff=float('inf') #infinity
        l=[]
        sort_Arr=sorted(arr)
        for i in range(1,len(sort_Arr)):
            mindiff=min(mindiff,sort_Arr[i]-sort_Arr[i-1])
        
        for i in range(1,len(sort_Arr)):
            if sort_Arr[i]-sort_Arr[i-1] == mindiff:
                l.append([sort_Arr[i-1],sort_Arr[i ]])

        return l
    
    #find the smallest difference between two values and give me the list with the two elements taht gave min differnece 
    