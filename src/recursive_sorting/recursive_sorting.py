# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):

    splits = [[i] for i in arr] #start out by splitting the array into arrays each containing only 1 number

    while(len(splits[0]) != len(arr)):#continue while we haven't merged all splits back down into a single sorted array again
        newSplits = []
        for(i in range(0, len(splits), 2)):#loop over splits in increments of 2
            if(i + 1 < len(splits) - 1):
                newSplits.append(merge(splits[i], splits[i + 1]))
            else:#splits is odd, so splits[i] doesn't have a partner to the right to merge with.
                newSplits.append(splits[i])

        







# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
