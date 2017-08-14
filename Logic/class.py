
in_arr = [4, 5, 25, 64, 24, 47, 97, 29]
sort_arr = []

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
def bubble_sort(arr):
    done = False
    while done == False:
        done = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                done = False

def selection_sort(arr):
    finished = 0
    minimum = finished
    while finished < len(arr):
        for i in range(finished, len(arr)):
            if arr[i] < arr[finished]:
                swap(arr, finished, i)
                finished = finished + 1
def insertion_sort(arr):
    result = []
    while len(arr) > 0:
        

print "This is the array unsorted", in_arr             

selection_sort(in_arr)

print "This is the sorted array ", in_arr


                
