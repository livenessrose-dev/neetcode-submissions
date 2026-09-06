class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # if len is empty return empty list [[]]
        if len(nums) == 0:
            return [[]]

        # keep calling the recursive function without the first element, create a subarray starting at index, just get rid of first element 
        perms = self.permute(nums[1:])
        res = []
        # for each permutation
        # 1: Insert nums[0] at every position, from index 0 to len(permutations), then add each new list to the result
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        # return final result containing all permutations
        return res 
