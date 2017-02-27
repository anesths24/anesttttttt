var=map(int, raw_input("dwse mia lista xarakthrwn me keno anamesa tous kai me na periexodai mhdenika").split())
print var 
k=var.count(0)

for i in range(k):
   var.remove(0)

for j in range(k):
	var.append(0)

print var 
