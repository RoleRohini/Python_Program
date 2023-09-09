if __name__=="__main__":

    arr_1=[1,2,3]
    arr_2=[3,4,5]
    mul_list=[]

    if len(arr_1)!=len(arr_2):
        print("Error : lenght of array should be same")

    for index in range(0, len(arr_1)) :
        mul_list.append(arr_1[index] * arr_2[index]   )
      
        print (mul_list)