'''
    given an arroy of integers, return indices of the numbers which add up to a specific target

    usecases - 
        - each input will have only one solution
        - each input can have more than one solution
'''

'''
    solution
        maintain a mapping from each number to its index
        check if target num has already been found
'''

class Solution:
    def two_sum(self, nums, target):
        """
        :type nums: list[int]
        :type target: int
        :rtype: list[int]
        """
        num_to_index = {}
        for i, num in enumerate(nums):
            if target - num in num_to_index:
                return [num_to_index[target - num], i]
            num_to_index[num] = i
        return []

s = Solution()
print(s.two_sum([2,3,4,5,6], 12))
