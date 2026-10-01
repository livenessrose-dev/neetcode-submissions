class Solution:
    def climbStairs(self, n: int) -> int:
        
        # make a decision tree, make 2 decisions at every step, if you go too far don't include that
        # every path led to the base case almost
        # save sub problems, O(n) 0,1,2,3,4,5, caching the result, memorization, DP - Bottom UP, 
        # the end will always be 1,1 
        # just keep two variables that represent ways to reach the previous step, and 
        # ways to reach the step before that
        one = 1
        two = 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one







    

