#Cracking the interview , ques 8.1
#Recursion requires extra memory due to call stack formed, and runtime 3**n,
#however if followed a bottom up approach and memoisation i.e using the cached result,
#we can reduce the time complexity to O(n)

def triple_step(n,steps):
    steps[0]=1
    steps[1]=1
    steps[2]=2 # child can either go by taking 1 step twice or by hopping directly to step 2
    for i in range(3,n+1):
        #Note : this can even be generalised saying , child can take upto k steps at a time , then use a for loop
        #upto k for this summation
        steps[i]=steps[i-1]+steps[i-2]+steps[i-3]
    return steps[n]


#Driver of the code
n=int(input())
steps=[0]*(n+1)
print(triple_step(n,steps))
