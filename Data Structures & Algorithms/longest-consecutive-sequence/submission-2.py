class Solution:
    def longestConsecutive(self, nums):
        numsSet = set(nums)
        longest = 0

        for x in numsSet:
            if x - 1 not in numsSet:
                current = x
                current_length = 1

                while current + 1 in numsSet:
                    current += 1
                    current_length += 1

                longest = max(longest, current_length)

        return longest
