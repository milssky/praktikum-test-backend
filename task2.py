from typing import List
from random import randint


def remove_all_zero_elements(nums: List[int]) -> List[int]:
    """
    Removes all zero elemets in the nums list.
    """
    first_zero_index = 0
    for index in range(len(nums)):
        if nums[index] != 0:
            if index != first_zero_index:
                nums[index], nums[first_zero_index] = nums[first_zero_index], nums[index]
            first_zero_index += 1
    return nums[:first_zero_index]


if __name__ == "__main__":
    test_nums = [randint(-1, 1) for _ in range(0, 20)]
    print(test_nums)
    print(remove_all_zero_elements(test_nums))
