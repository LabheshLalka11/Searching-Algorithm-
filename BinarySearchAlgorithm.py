'''
The Time Complexity of Binary Search is : O(logn) 
The Space Complexity of Binary  Search is : O(1)
'''
sorted_array = [0, 1, 3, 8, 14, 18, 19, 34, 52]
def BinarySearch(array,element):
    print("Binary Search Technique")
    lower_bound = 0
    upper_bound = len(array)-1 
    Found = False
    while lower_bound<=upper_bound and not Found:
        mid = (lower_bound+upper_bound)//2
        
        if array[mid]==element:
            Found = True
            break
        else:
            if element<array[mid]:
                upper_bound = mid-1
            else:
                lower_bound = mid+1
                
    if Found==True:
        print("Found at Position:",mid+1)
    else:
        print("Not Found")

BinarySearch(sorted_array,19)
