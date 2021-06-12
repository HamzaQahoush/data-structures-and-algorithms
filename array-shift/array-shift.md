## code

    def insertShiftArray(arr,val):
     arrLength=len(arr)
     if arrLength %2 == 0:
        return(arr[:(arrLength//2)] + [val] + arr[(arrLength//2):])
     else:
        return(arr[:arrLength//2+1] +
        [val] + arr[arrLength//2+1:]

## White Boarding

![](https://i.ibb.co/VSWhZbh/array-shift-1.jpg)
