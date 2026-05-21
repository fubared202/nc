class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_nums = []
        max_seq_so_far = 0

        # Identify all the potential sequence starts.
        # A number can only be a sequence start if the number one
        # less than it is missing in the input array.
        for num in nums:
            if (num-1) not in nums_set:
                # Now use O(1) lookup from the map to see which
                # sequence runs the longest.
                next_num = num + 1
                while next_num in nums_set:
                    next_num += 1

                # The delta is how far ahead were able to go. Don't
                # need to add 1 here since we start at +1.
                sequence_len = (next_num - num)
                if sequence_len > max_seq_so_far:
                    max_seq_so_far = sequence_len
        
        return max_seq_so_far
        