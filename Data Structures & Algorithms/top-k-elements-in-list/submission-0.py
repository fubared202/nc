class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First, a simple count of the integers.
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # Now create the values array.
        values = [0] * len(nums)
        for key, v in counts.items():
            if values[v-1] == 0:
                values[v-1] = [key,]
            else:
                values[v-1].append(key)

        # Now output in the reverse order until we have output k items
        top_k = list()
        for v in values[::-1]:
            if v != 0:
                for item in v:
                    top_k.append(item)
                    if len(top_k) == k:

                        return top_k


        
        