class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            # base case
            if index == len(nums):
                res.append(path[:])
                return
            
            # decision 1 (include)
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            # decision 2 (skip (nums[index]))
            backtrack(index + 1, path)

        backtrack(0, [])
        return res