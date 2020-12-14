def reverseArray(arr):
    # initial left and right index assignment
    left = 0
    right = len(arr)-1

    # loop through the array and swap items
    while(left < right):
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    # return the reversed arraybw
    return arr
