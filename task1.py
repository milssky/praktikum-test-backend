from typing import List


def relative_complement(l1: List[int], l2: List[int]) -> List[int]:
    """
    Returns a list of elements that are in l1 and not in l2.
    """
    return list(set(l1) - set(l2))


if __name__ == "__main__":
    test_a = list(range(0, 10))
    test_b = list(range(-5, 5))

    print(relative_complement(test_a, test_b))   # [5, 6, 7, 8, 9]
