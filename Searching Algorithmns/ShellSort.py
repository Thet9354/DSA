# Python3 program for implementation of Shell Sort

def shellSort(arr):
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        # check the array in from left to right
        # til the last possible index of j
        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1

            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k-gap], arr[k] = arr[k], arr[k-gap]

                k -= 1

            gap //= 2


# Driver to check the code 
arr2 = [12, 34, 54, 2, 3]
print("Input array:", arr2)

shellSort(arr2)
print('Sorted array', arr2)