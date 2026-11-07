class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen =set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

'''
Okay, so for this problem, I would use a set because a set stores unique values, and I can check whether a number already exists efficiently.

First, I create an empty set called seen.

Then I loop through the array and check each number one by one.

For each number, I check whether it already exists in seen.

If it does, that means we've encountered the same number before, so we found a duplicate and can immediately return True.

Otherwise, I add the number to the set and continue checking.

If the loop finishes without finding any duplicate, I return False.
'''