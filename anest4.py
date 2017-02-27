import math
def bubbleSort(alist):
    for h in range(len(alist)-1,0,-1):
        for i in range(h):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

s=raw_input("dwse mia parastash airthmwn")
alist = list(map(int,s.split()))
x=len(alist)
athroisma=0
typikh_apoklish=0
bubbleSort(alist)
print(alist)



for j in range(x-2):
	if (j!=0 and j!=1):
		athroisma=(athroisma+alist[j])
mo=(athroisma/(x-4))
for m in range(x-2):
	if (m!=0 and m!=1):
		typikh_apoklish=typikh_apoklish+((alist[m]-mo)**2)
typikh_apoklish=typikh_apoklish/(x-4)




k=math.sqrt(typikh_apoklish)
print "h typikh apoklish xwris toys 2 megalyterous kai 2 mikroterous arithmous einai:",k