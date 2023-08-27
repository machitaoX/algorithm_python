class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        length = len(s)
        result = ""
        for i in range(num_rows):
            move_index = i
            step_first = 2 * (num_rows - i - 1)
            step_second = 2 * i
            step = 0
            while move_index < length:
                result += s[move_index]
                if i == num_rows - 1 or (step == step_first and step_second != 0):
                    step = step_second
                else:
                    step = step_first
                move_index += step
        return result
