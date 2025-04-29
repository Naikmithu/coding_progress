class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        dp = [amount+1]*(amount+1)
        dp[0]=0

        for i in range(1,amount+1):
            for c in coins:
                if i-c>=0:
                    dp[i]=min(dp[i],1+dp[i-c])
                
        
        return dp[amount] if dp[amount]!=amount+1 else -1
    
    #Dynamic Programming : Target problem is broken down into subproblems, and the solution to each subproblem is stored in a table (dp array) to avoid redundant calculations.
# The dp array is initialized with a value greater than the target amount (amount+1) to represent that the amount is not achievable.
#at each iteration, we check if the current amount (i) can be achieved by subtracting the coin value (c) from it.
# If it can, we update the dp array with the minimum number of coins needed to achieve that amount.