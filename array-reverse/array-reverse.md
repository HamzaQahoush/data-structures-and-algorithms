## code
```
    code :
def reverse(alist):
    left = 0
    right = len(alist) - 1
    while left < right:
        alist[left], alist[right] = alist[right], alist[left]
        left += 1
        right -= 1
    return alist


print (reverse([1,3,4,5]))
```
## White Boarding

![](https://i.ibb.co/zQZPhp5/reverse-array.jpg)
