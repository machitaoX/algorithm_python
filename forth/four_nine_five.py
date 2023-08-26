from typing import List


class Solution:

    def find_poisoned_duration(self, time_series: List[int], duration: int) -> int:
        if not time_series:
            return 0
        result = duration
        for i in range(1, len(time_series)):
            result = result + min(duration, time_series[i] - time_series[i - 1])
        return result
