class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [1] * len(nums)
        suffix_products = [1] * len(nums)

        # Compute products of all elements to the left of the 
        # current one, current one excluded. For nums[0], this
        # will just be one.
        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i-1] * nums[i-1]
        print(prefix_products)

        # Now repeat for all elements to the right.
        for i in range(len(nums)-2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i+1]
        print(suffix_products)

        excluded_products = list()
        for i in range(0, len(nums)):
            excluded_products.append(prefix_products[i] * suffix_products[i])

        return excluded_products