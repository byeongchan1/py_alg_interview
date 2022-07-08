# 393. UTF-8 Validation
# https://leetcode.com/problems/utf-8-validation/

# Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

# For a 1-byte character, the first bit is a 0, followed by its Unicode code.
# For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
# This is how the UTF-8 encoding would work:

from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        # 문자 바이트만큼 10으로 시작 판별
        def check(size):
            for i in range(start +1, start + size + 1):
                if i >= len(data) or (data[i]) >> 6) != 0b10:
                    return False
            return True

        start = 0
        while start < len(data):
            # 첫바이트 기준 총 문자 바이트 판별
            first = data[start]
            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True