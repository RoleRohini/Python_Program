#Initialize array     
arr = [5, 2, 8, 7, 1];     
temp = 0;    
     
#Displaying elements of original array    
print("Elements of original array: ");    
for i in range(0, len(arr)):     
    print(arr[i]),    
     
#Sort the array in descending order    
for i in range(0, len(arr)):    
    for j in range(i+1, len(arr)):    
        if(arr[i] < arr[j]):    
            temp = arr[i];    
            arr[i] = arr[j];    
            arr[j] = temp;    
     
print();    
     
#Displaying elements of array after sorting    
print("Elements of array sorted in descending order: ");    
for i in range(0, len(arr)):     
    print(arr[i]),   