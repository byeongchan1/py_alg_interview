# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        