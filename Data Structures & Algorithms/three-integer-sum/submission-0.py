class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        matching_triplets = list()
        i = 0
        while i < len(nums):
            # Find the pairs that will complement i.
            print(i)
            j, k = i+1, len(nums)-1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    # Got a triplet, save it.
                    matching_triplets.append([nums[i], nums[j], nums[k]])
                    orig_j, orig_k = nums[j], nums[k]
                    j += 1
                    k -= 1

                    # And skip over duplicates.
                    while j < len(nums) and nums[j] == orig_j:
                        j += 1
                    while k > 0 and nums[k] == orig_k:
                        k -= 1
            orig_i = nums[i]
            i += 1
            while i < len(nums) and nums[i] == orig_i:
                i += 1
        
        return matching_triplets

