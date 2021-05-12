'''
The Time Complexity of Linear Search is :  O(n)
The Space Complexity of Linear Search is : O(1)
'''



sorted_array = [0, 1, 3, 8, 14, 18, 19, 34, 52]

def linearSearch(array,element):
    print("Linear Searching Technique")
    for i in range(0,len(array)):
        if element == array[i]:
            print("Found at Position:",i+1)
            break
    else:
        print("Not Found")

linearSearch(sorted_array,14)
