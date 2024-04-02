class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxN = 0
        for num in nums:
            maxN = max(maxN, num)
        arr = [0]*(maxN +1)
        for num in nums:
            arr[num] += num
        prev = arr[0]
        curr = arr[1]
        for i in range(2, len(arr)):
            temp = curr
            curr = max(curr, prev + arr[i])
            prev = temp
        return curr
        
#Time Complexity: O(n+maxN)
#Space Complexity: O(maxN)