def linear_search(unordered_list, term):
    for index, entry in enumerate(unordered_list):
        if entry == term:
            return index
    return None


def linear_search_ordered(ordered_list, term):
    for index, entry in enumerate(ordered_list):
        if entry == term:
            return index
        elif entry > term:
            return None
    return None


def binary_search(ordered_list, term):
    lowest = 0
    highest = len(ordered_list)-1
    while lowest <= highest:
        index = lowest+((highest-lowest)//2)
        if ordered_list[index] == term:
            return index
        elif ordered_list[index] < term:
            lowest = index+1
        else:
            highest = index-1
    return None


def interpolation_search(ordered_list, term):
    lowest = 0
    highest = len(ordered_list)-1
    while lowest <= highest and ordered_list[lowest] <= term <= ordered_list[highest]:
        index = lowest + (term - ordered_list[lowest]) * (highest - lowest) // (ordered_list[highest] - ordered_list[lowest])
        if ordered_list[index] == term:
            return index
        elif ordered_list[index] < term:
            lowest = index+1
        elif ordered_list[index] > term:
            highest = index-1
    return None

if __name__ == '__main__':
    unordered_list_test = [7, 21, 3, 49, 100, 6, 24, 49]
    print(f"\nsearch in unordered list: {unordered_list_test}")
    item1a = 49
    print(f"index of {item1a} is {linear_search(unordered_list_test, item1a)}")
    item1b = 1
    print(f"index of {item1b} is {linear_search(unordered_list_test, item1b)}")

    ordered_list_test = [3, 6, 7, 21, 24, 49, 100]
    print(f"\nsearch in ordered list: {ordered_list_test}")
    item2a = 24
    print(f"index of {item2a} is {linear_search_ordered(ordered_list_test, item2a)}")
    item2b = 8
    print(f"index of {item2b} is {linear_search_ordered(ordered_list_test, item2b)}")

    print(f"\nbinary search: {ordered_list_test}")
    print(f"index of {item2a} is {binary_search(ordered_list_test, item2a)}")
    print(f"index of {item2b} is {binary_search(ordered_list_test, item2b)}")

    print(f"\ninterpolation search: {ordered_list_test}")
    print(f"index of {item2a} is {interpolation_search(ordered_list_test, item2a)}")
    print(f"index of {item2b} is {interpolation_search(ordered_list_test, item2b)}")
