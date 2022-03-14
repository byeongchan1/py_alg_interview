# 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

# Given a list of unique words, return all the pairs of the distinct 
# indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]
        
        output = []
        for i, word1 in enumerate(words):
            for j, word2 in enumerate(words):
                if i == j:
                    continue
                if is_palindrome(word1 + word2):
                    output.append([i, j])
        
        return output