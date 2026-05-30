from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq=Counter(s) #O(n)
        t_freq=Counter(t) #O(n)
        if s_freq.keys()==t_freq.keys() and s_freq.items()==t_freq.items():
            return True
        return False
        