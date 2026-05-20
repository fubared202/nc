class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = dict()
        for index, num in enumerate(nums):
            if (target - num) in nums_set:
                return [nums_set[target - num], index]
            elif num not in nums_set:
                nums_set[num] = index

        return [-1, -1]   # should never be hit as per the problem spec !