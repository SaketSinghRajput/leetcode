class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        s= list(set(nums))
        len_s = len(s)
        arr = [0] * len_s
        for i in range(l):
            for j in range(len_s):
                if s[j] == nums[i]:
                    arr[j] += 1
    
        for i in range(len_s):
            if arr[i] > l/2:
                return s[i]
        