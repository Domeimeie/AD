def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def mergeLists(sortedLeftList, sortedRightList):
    mergedList = []
    indexLeft = 0
    indexRight = 0
    for i in range(len(sortedLeftList) + len(sortedRightList)):
        if indexLeft == len(sortedLeftList):
            mergedList.append(sortedRightList[indexRight])
            indexRight += 1
        elif indexRight == len(sortedRightList):
            mergedList.append(sortedLeftList[indexLeft])
            indexLeft += 1
        elif sortedLeftList[indexLeft] <= sortedRightList[indexRight]:
            mergedList.append(sortedLeftList[indexLeft])
            indexLeft += 1
        else:
            mergedList.append(sortedRightList[indexRight])
            indexRight += 1

    return mergedList
    
def mergesort(list):
    if len(list) <= 1:
        return list
    
    leftList, rightList = split_list(list)

    sortedLeftList = mergesort(leftList)
    sortedRightList = mergesort(rightList)

    return mergeLists(sortedLeftList, sortedRightList)

testCount = int(input())
for i in range(testCount):
    unsorted_list = [int(x) for x in input().split()]
    result_list = mergesort(unsorted_list)
    print(" ".join(str(element) for element in result_list))