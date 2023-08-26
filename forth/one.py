from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums:
        :param target:
        :return:
        """
        for index in range(len(nums) - 1):
            rest = target - nums[index]
            if rest in nums[index + 1:]:
                return [index, nums[index + 1:].index(rest) + index + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.two_sum([1, 2, 3, 4, 5, 9], 10))

