

for i in range(11):
  print("5 X",i,"=",5*i)
  if(i==4):
    break

print("break worked")



for i in range(11):
  if i % 4 == 0:
    continue
  print("5 X",i,"=",5*i)
