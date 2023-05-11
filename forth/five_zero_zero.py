from typing import List


class Solution:

    def find_words(self, words: List[str]) -> List[str]:
        res = []
        dict_map = {}
        line_one = 'qwertyuiop'
        for one in line_one:
            dict_map[one] = 1

        line_two = 'asdfghjkl'
        for two in line_two:
            dict_map[two] = 2

        line_three = 'zxcvbnm'
        for three in line_three:
            dict_map[three] = 3

        for word in words:
            word_letter_array = list(word.lower())
            first = dict_map[word_letter_array[0]]
            count = 0
            for word_letter in word_letter_array:
                if dict_map[word_letter] != first:
                    count = count + 1
                    break
            if count == 0:
                res.append(word)
        return res


if __name__ == '__main__':
    s = Solution()
    s.find_words()
