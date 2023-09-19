
if __name__=="__main__": 
    maths_student={"Rani","Bani","Tani","Sani","Mani","Ani"}
    python_student={"Rani","Tani","RAm","Sam","Ben","Den"}

#fint student who like both math and python
    print(maths_student & python_student)
   
    #fint student who like math    
    print(maths_student - python_student) 
   
    #fint student who like only one sub 
    print(maths_student ^ python_student) 
   
     #fint student who like both python only    
    print(python_student - maths_student) 