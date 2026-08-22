class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = 0
        if target not in nums:
            return -1
        for i in range(len(nums)):
            if target != nums[i]:
                idx += 1
            else :
                break

        return idx
        