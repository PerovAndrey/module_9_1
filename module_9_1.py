def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results


def min_element(nums):
    return min(nums)


def max_element(nums):
    return max(nums)


def len_element(nums):
    return len(nums)


def sum_of_elements(nums):
    return sum(nums)


def sorted_element(nums):
    return sorted(nums)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))