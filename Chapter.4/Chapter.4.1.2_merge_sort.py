## merge sort algorithm

# num.1
"""
# list input
unsorted_list = [int(x) for x in input().split()]


## n/2로 나누고, 1개씩의 요소가 남기까지 재귀적으로 conquer 한다.
## 그 후, 그 다음에 2개씩의 요소들을 반복적으로 merge 한다.

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        print("데이터가 하나 밖에 없습니다.")
        return unsorted_list

    mid = len(unsorted_list) // 2
    left = unsorted_list[:mid]
    right = unsorted_list[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)

def merge(left, right):
    i = 0
    j = 0
    sorted_list = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while (i < len(left)):
        sorted_list.append(left[i])
        i += 1

    while (j < len(right)):
        sorted_list.append(right[j])
        j += 1

    return sorted_list

print(merge_sort(unsorted_list)) """
