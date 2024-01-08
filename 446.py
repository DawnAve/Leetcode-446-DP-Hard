class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums) # Length of the array
        total = 0   # Answer

        # A default dictionary, dp[i][j] means the number of arithmetic arrays that ends in index "i"
        # With common difference "j"
        # defaultdict(int) will automatically assign 0 to un-initialized elements in the dictionary
        dp = [defaultdict(int) for _ in range(n)]

        # Loop from the second index to the end
        for i in range(1,n):

            # Loop from the start to i
            for j in range(i):

                # Calculate the common diffference
                diff = nums[i] - nums[j]

                # Therefore, we have an arithmetic array ending in "i", with difference diff
                dp[i][diff]+=1

                # If there are arithmetic arrays that end in "j"
                if diff in dp[j]:

                    # We add the the existing number of arrays to [i][diff]
                    dp[i][diff] += dp[j][diff]
                    total +=dp[j][diff]
                    
        return total
