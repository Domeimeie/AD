def bubble_sort(unordered_list):
    iteration_counter = 0
    last_index = len(unordered_list) - 1
    for i in range(last_index, 0, -1):
        # swap_counter = 0
        for j in range(i):
            iteration_counter += 1
            if unordered_list[j] > unordered_list[j + 1]:
                # swap_counter += 1
                unordered_list[j], unordered_list[j + 1] = unordered_list[j + 1], unordered_list[j]
        # if swap_counter == 0: break
    print(f"length = {len(unordered_list)},  iteration_counter = {iteration_counter}")


# list that is already sorted, but reverse
sorted_reverse = [4, 3, 2, 1]
bubble_sort(sorted_reverse)
print(sorted_reverse)
print()

# unsorted list
my_list = [12, 45, 31, 67, 453, 78, 9, 51, 95, 56, 83, 55, 81]
bubble_sort(my_list)
print(my_list)
print()

# sort the sorted list again
bubble_sort(my_list)
print(my_list)
print()

# sorted list
my_list = [1, 2, 3, 7, 6, 5]
bubble_sort(my_list)
print(my_list)
