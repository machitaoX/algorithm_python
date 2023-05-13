from typing import List


class Solution(object):

    def next_greater_element(self, nums1: List[int], nums2: List[int]):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        m, n = len(nums1), len(nums2)
        res = [0] * m
        for i in range(0, m):
            index2 = nums2.index(nums1[i])
            k = index2 + 1
            while k < n and nums2[k] < nums2[index2]:
                k += 1
            res[i] = nums2[k] if k < n else -1
        return res
