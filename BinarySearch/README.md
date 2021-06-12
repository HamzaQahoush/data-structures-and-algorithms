# Binary_Search

Write a function called BinarySearch which takes in 2 parameters: a sorted array and the search key.
return the index of the array’s element that is equal to the value of the search key, or -1 if the element is not in the array

## Whiteboard Process

![](https://i.ibb.co/NtqQzXw/array-binary-search.jpg)

You can take look on [miro](https://miro.com/app/board/o9J_lAVhvac=/)

## Approach & Efficiency

we need to use apply the principle of Binary search.
so we need to look for value in the list and sure its exist between first and last index .
so we need to refers to them as left and right .
then we need to check our number if it exists in the middle of array.
for example : if the value of middle array is less than our target value .
so we confine our search on the mid of arr +1
and we repeat and , check of target value in new narrowed length etc
we will keep doing that until search range become empty that means the value does'nt exists
