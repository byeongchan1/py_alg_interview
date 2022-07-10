# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # 1을 뺀 값과 AND 연산 횟수 측정
            n &= n - 1
            count += 1
        return count