# def quick_sort(the_list):
#     # left index
#     l = 0

#     # pivot index
#     p = len(the_list)

#     # right index
#     r = pivot - 1

#     if l < r:
#         # increment l till we have an appropriate value
#         while the_list[l] <= the_list[p] && l < len(the_list):
#             l += 1

#         # decremt r till we have an appropriate value
#         while the_list[r] > the_list[p] && r >= l:
#             r -= 1

#     the_list[l], the_list[r] = the_list[r], the_list[l]

# ------------------------------------------------------------------

def quick_sort(arr, l, r):
    if l < r:
        # Partition the array by setting the position of the pivot value
        position = partition(arr, l, r)
        # Sort the l
        QuickSort(arr, l, position - 1)
        # Sort the r
        QuickSort(arr, position + 1, r)

def partition(arr, l, r):
    # set a pivot value as a point of reference
    p = arr[r]
    # create a variable to track the largest index of numbers lower than the defined pivot
#     DEFINE low <-- l - 1
#     for i = l to r do
#         if arr[i] <= pivot
#             low++
#             Swap(arr, i, low)

#      # place the value of the pivot location in the middle.
#      # all numbers smaller than the pivot are on the l, larger on the r.
#      Swap(arr, r, low + 1)
#      # return the pivot index point
#      return low + 1

# ALGORITHM Swap(arr, i, low)
#     DEFINE temp;
#     temp <-- arr[i]
#     arr[i] <-- arr[low]
#     arr[low] <-- temp
