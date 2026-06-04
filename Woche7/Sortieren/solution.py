def quicksort(list):
    if len(list) <= 1:
        return list

    leftList = []
    rightList = []
    pivotList = []
    pivot = len(list) - 1

    for element in list:
        if element < list[pivot]:
            leftList.append(element)
        elif element > list[pivot]:
            rightList.append(element)
        else:
            pivotList.append(element)

    sortedLeftList = quicksort(leftList)
    sortedRightList = quicksort(rightList)
    return sortedLeftList + pivotList + sortedRightList

testCount = int(input())
for i in range(testCount):
    unsorted_list = [int(x) for x in input().split()]
    result_list = quicksort(unsorted_list)
    print(" ".join(str(element) for element in result_list))