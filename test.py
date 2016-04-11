import datetime
fib = []
fib.append(0)
fib.append(1)
numb = 50000
startTime = datetime.datetime.now()
for i in range(2,numb+1):
	fib.append(fib[i-1]+fib[i-2])
endTime = datetime.datetime.now()
print "Milliseconds: ",(endTime.microsecond-startTime.microsecond)/1000


# def fibo(numb):
# 	if numb==0:
# 		return 0
# 	elif numb<=2:
# 		return 1
# 	else:
# 		return fibo(numb-1)+fibo(numb-2)
# startTime1 = datetime.datetime.now()
# fibo(30)
# endTime1 = datetime.datetime.now()
# print "Milliseconds: ",(endTime1.microsecond-startTime1.microsecond)/1000


