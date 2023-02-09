from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first_count = 0
        second_count = 0
        first_value = None
        second_value = None

        result = 0
        sequence = 0
        previous = None
        for f in fruits:

            if first_value is None or f == first_value:
                first_count += 1
                first_value = f
            elif second_value is None or f == second_value:
                first_count += 1
                second_value = f
            else:
                result = first_count + second_count if first_count + second_count > result else result
                first_count, first_value = sequence, previous
                second_count, second_value = 1, f

            if previous is None or f == previous:
                sequence += 1
            else:
                sequence = 1
            previous = f
        return first_count + second_count if first_count + second_count > result else result
