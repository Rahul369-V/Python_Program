
// Time Taken to find Armstrong number or not
 
import time 
start=time.time()
print("hello")
num=153
temp=num
sum=0
while(num>0):
    digit=num%10
    sum+=digit**3
    num=num//10
if(temp==sum):
    print("{} number is armstrong number".format(temp))
else:
    print("{} number is not a armstrong number".format(temp))
stop=time.time()

timeTaken=(stop-start)
print("time taken for this program is :{}".format(timeTaken))
