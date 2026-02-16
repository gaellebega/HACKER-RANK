# we will only make the roundoff if and only if the the difference is less than 3
# 73 the next multiple of 5 is 75  we will find the difference that is less than 3 then we will round of the grades
# 67 the next multiple of 5 is 70 the difference is equla to 3 so we can not make the round of


grades=int(input())
# next_grade=int(input())
# max_val=100
# multiples=grade%5==0
resp=[]
for grade in grades:
  if grade >= 38:
    mods = grade%5
    if mods>=3:
      grades+=(5-mods)
  resp.append(grade)    
print(resp)

