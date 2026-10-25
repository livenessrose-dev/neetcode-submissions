class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # list = []
        # for i in range(len(nums) - k + 1):
            # max_i = nums[i]
            # for j in range(i, i + k):
                # max_i = max(max_i, nums[j])
            # list.append(max_i)

        # return list
        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output



                