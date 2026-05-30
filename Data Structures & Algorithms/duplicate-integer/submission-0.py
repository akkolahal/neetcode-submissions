from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (list(filter(lambda x: x[1]>1, Counter(nums).items()))):
            return True
        else:
            return False
        