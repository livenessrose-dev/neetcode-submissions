class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # sort so we skip dupliates easily
        candidates.sort()

        def dfs(idx, cur, total):
            # base case
            if total == target:
                res.append(cur.copy())
                return
            
            # if i is out of bounds, we are out of nums, or if the total is > target return immediately 
            for i in range(idx, len(candidates)):
                # to avoid duplicate combinations if canidates[i] == canidates[i - 1] and we are still in the same level of recursion so i > idx, we can SKIP that number
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                # stop early if current_sum + canidates[i] > target since the list is already sorted
                if total + candidates[i] > target:
                    break
        
            # First decision>: include the number and recurse with i + 1, can't reuse same element
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])

            # Second decision, backtrack by removing the last number
                cur.pop()

        dfs(0, [], 0)
        return res