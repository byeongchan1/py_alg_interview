# 771. Jewels and Stones
# https://leetcode.com/problems/jewels-and-stones/

# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
# Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

# Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = {}
        count = 0
        
        for s in S:
            if s not in freqs:
                freqs[s] = 1
            else:
                freqs[s] += 1
        
        for s in J:
            if s in freqs:
                count += freqs[s]
        
        return count
