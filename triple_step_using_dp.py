#Cracking the interview , ques 8.1
#Recursion requires extra memory due to call stack formed, and runtime 3**n,
#however if followed a bottom up approach and memoisation i.e using the cached result,
#we can reduce the time complexity to O(n)

def triple_step(n,steps):
    steps[0]=1
    steps[1]=1
    steps[2]=2 # child can either go by taking 1 step twice or by hopping directly to step 2
    for i in range(3,n):
        #Note : this can even be generalised saying , child can take upto k steps at a time , then use a for loop
        #upto k for this summation
        step[i]=step[i-1]+step[i-2]+step[i-3]
    return step[n]




#Driver of the code
n=int(input())
steps=[0]*n
print(triple_step(n,steps))
