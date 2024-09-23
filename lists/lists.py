from typing import Optional

class ListExercise:
    @staticmethod
    def get_max_num(input_list: list[int]) -> Optional[int]:
        if not input_list:
            return None
        max_num = input_list[0]
        for num in input_list:
            if num > max_num:
                max_num = num
        return max_num

    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        max_num = ListExercise.get_max_num(input_list)
        return [max_num if num > 0 else num for num in input_list]

    @staticmethod
    def search(input_list: list[int], query: int, first: int = 0, last: int = -1) -> int:
        if last == -1:
            last = len(input_list) - 1

        if first > last or input_list[last] < query:
            return -1

        mid = (first + last) // 2

        if input_list[mid] == query:
            return mid
        if input_list[mid] < query:
            first = mid + 1
        if input_list[mid] > query:
            last = mid - 1

        return ListExercise.search(input_list, query, first, last)
