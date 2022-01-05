# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/
# Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned.
# It is guaranteed there is at least one word that is not banned, and that the answer is unique.
# The words in paragraph are case-insensitive and the answer should be returned in lowercase.

import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # list comprehension 사용
        # 정규표현식 사용 (\w는 alphabat + number, ^는 역 표시)
        words = [word for word in re.sub('[^\w]', " ", paragraph).lower().split()
                if word not in banned]
        
        counts = collections.Counter(words) # collection.Counter(list) 하게 되면, dict 생성되는데, element들 마다 나온 횟수 매칭됨
        # Counter({'ball': 2, 'bob': 1, 'a': 1, 'the': 1, 'flew': 1, 'far': 1, 'after': 1, 'it': 1, 'was': 1})
        
        # Counter의 most_common(n) 메서드는 빈번하게 발생하는 elements 내림차순으로 n개까지 보여줌
        # counts.most_common(1) = [('ball', 2)]
        return counts.most_common(1)[0][0]
        