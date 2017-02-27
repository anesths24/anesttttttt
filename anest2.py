var = raw_input("dwse parentheseis: ")
print var
i=0
x=0 
y=0
flag="true"
while i<len(var) and flag=="true":
  
  if (var[i]=="(" ):
  	x=x+1
  elif (var[i]==")"):
  	y=y+1
  if (x>=y ):
    flag="true"
  else:
    flag="false"
  
         	
  i=i+1
if (flag=="true" and  x!=y):
   
   flag="false"
print flag