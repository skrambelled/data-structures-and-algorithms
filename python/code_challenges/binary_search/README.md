# Challenge 03 - Binary Search

[Pull request]()

## Problem domain:

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach and Efficiency

### method 1

* O(n) space
* O(log(n)) time
* mutable
* steps:
  1. left index, right index, and middle index variables
  2. if the value we are searching for is less than the left or more than the right, return -1
  3. if the value IS the left, middle, or right, return that index
     * if value is less than the mid, recursively call with mid set as the right
     * if value is greater than the mid, recursively call with mid set as the left

## Whiteboard solution

![whiteboard](binary_search.png)

[<-- Python Challenges](../README.md)
