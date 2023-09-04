if __name__=="__main__":
    list_1=list(range(1,101))
    list_2= []

    for number in list_1:
        if number%2==1:
            list_2.append(number)
    print(list_2)



