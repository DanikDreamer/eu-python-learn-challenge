from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        result = []
        for element in input_array:
            bool_value, func_result = func(element)
            if bool_value:
                result.append(func_result)
        return result
