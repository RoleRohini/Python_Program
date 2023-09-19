
if __name__ == "__main__" :

    arr_1 = list(range(10))
    arr_2 = []
    for num in arr_1 :
        arr_2.append(num * num)
    print(arr_2)

    arr_3 = [ num * num for num in arr_1 ]
    print(arr_3)

    arr_4 = list(map( lambda num :  num * num, arr_1))
    print(arr_4)