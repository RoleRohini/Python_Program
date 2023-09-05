  #even_odd using loop
if __name__=="__main__":
  
    list_of_nums = list(range(1,101))
    print(list_of_nums)

    for number in list_of_nums:
        if(number % 2)==0:
            print(number)

            count =1 
    while count < 101:
        if (count % 2)==0:
            print(count)

            count = count + 1

       