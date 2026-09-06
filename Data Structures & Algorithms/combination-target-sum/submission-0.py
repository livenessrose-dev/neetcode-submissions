class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            
            # if i is out of bounds, we are out of nums, or if the total is > target return immediately 
            if i >= len(nums) or total > target:
                return
            
            nums[i]

            # append to our current combination 
            # first decision, include it
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # second decision, don't include it 
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res