def binary_search(li, val, left=None, right=None):
    # set our default left and right values when not provided
    if left is None:
        left = 0

    if right is None:
        right = len(li)-1

    # return -1 when the value is not on our list
    if val < li[left] or val > li[right] or left > right:
        return -1

    # return the index if the value is at our edges or the mid
    if val == li[left]:
        return left

    if val == li[right]:
        return right

    mid = (right-left)//2 + left
    if val == li[mid]:
        return mid

    # recursively call binary search with new boundaries
    if val < li[mid]:
        return binary_search(li, val, left, mid-1)

    if val > li[mid]:
        return binary_search(li, val, mid+1, right)
