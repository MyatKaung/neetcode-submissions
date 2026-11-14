class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ## add boundary ballons
        nums =[1]+nums+[1]
        n=len(nums)

        ##initialize dp with zeros
        dp =[[0]*n for _ in range(n)]

        #choose interval size
        for gap in range(2,n):
            for left in range(n-gap):
                right = left+gap

                for k in range(left+1, right):
                    # calculate total coins 
                        coins = (
                        dp[left][k]
                        + dp[k][right]
                        + nums[left] * nums[k] * nums[right])


                        # Step 7: Store maximum coins
                        dp[left][right] = max(
                            dp[left][right], coins
                        )

        return dp[0][n-1]



        