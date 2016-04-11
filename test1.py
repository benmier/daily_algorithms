import datetime
a=0
b=1
c=1
n=50000
startTime2 = datetime.datetime.now()
for i in range(2,n+1):
	c=a+b
	a=b
	b=c
endTime2 = datetime.datetime.now()
print "Milliseconds: ",(endTime2.microsecond-startTime2.microsecond)/1000
