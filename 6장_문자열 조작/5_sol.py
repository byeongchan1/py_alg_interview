# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # collections.defaultdict(list)는 key값이 없어도 호출 되는 dict를 구현하게 해준다 -> 간단히 구현가능
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
            # sorted('bat') = ['a', 'b', 't']
            # ''.join(list) 하면 하나의 string으로 붙여준다
            # '?'.join(list) 하면 list의 elements 사이에 ?를 추가하며 붙여준다.
        
        # anagrams.values() = dict_values(list) 형식으로 표현됨
        # 이것을 list로 묶으면 list in list 형식 나오게 됨
        return list(anagrams.values())
        