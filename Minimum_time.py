import math
class Solution(object):


    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(points) - 1):
            x1,y1 = points[i]
            x2,y2 = points[i+1]

            res+= max(abs(x2-x1),abs(y2-y1))
        
        return res


#Chebyshev distance is a metric used to calculate the distance between two points when movement is allowed 
# in horizontal, vertical, and diagonal directions (like how a King moves in chess).
# Time Complexity : O(n)