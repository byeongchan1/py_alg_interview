# 239. Sliding Window Maximum
# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.

from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque()
        current_max = float('-inf')

        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            # 새로 추가된 값이 기존 최대보다 큰 경우 교체
            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v

            results.append(v)

            # 최대값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        return results