class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product = 1
        count_zeros = 0
        for num in nums:
            if num != 0:
                full_product *= num
            else:
                count_zeros += 1
        
        multiples = []
        for num in nums:
            if count_zeros > 1:
                multiples.append(0)
            elif count_zeros == 1 and num == 0:
                multiples.append(full_product)
            elif count_zeros == 1 and num != 0:
                multiples.append(0)
            else:
                multiples.append(int(full_product / num))

        return multiples