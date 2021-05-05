def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(list1)):
            curr_ele = arr[i]
            pos = i
            while pos >= gap and curr_ele < arr[pos-gap]:
                arr[pos] = arr[pos-gap]
                pos = pos - gap
            arr[pos] = curr_ele
        gap = gap // 2


if __name__ == '__main__':
    list1 = [19,12,45,23,22,66,77,33,56,90,21,2,4,89]
    shell_sort(list1)
    print(list1)

