if __name__=="__main__":
    person_data={"name":"Rani","aadhar_no":"1234 5678 0987","age":21,"college":"Raisoni college"}
    print(person_data)
    
    person_data_list=[
                       {"name":"Rohi" , "aadhar_no":"1234 4478 0987" , "age":21, "college":"Raisoni college"},
                       {"name":"Rohini" , "aadhar_no":"1234 9879 0987" , "age":18, "college":"VDF college"},
                       {"name":"Pragati" , "aadhar_no":"1234 2348 0987" ,  "age":22 , "college":"UPS college"},
                       {"name":"Ranumai" , "aadhar_no":"1234 1118 0987" , "age":20 , "college":"kids college"}
    ]
    for record in person_data_list :
        print(record["name"],record["aadhar_no"])
        print(record["age"],record["college"])