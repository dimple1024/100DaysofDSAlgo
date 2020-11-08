#Cracking the interview , ques 8.1
#Although the memoisation is a better approach in terms of time complexity, but it still requires O(n) space
#we can reduce this space by simply eliminating the use of array and using some temporary variables , since at every point
#while calculating the no. of ways , we only need the no of ways calculated for n-1 , n-2 and n-3 only.

def triple_step(n):
    steps_1=1  # Consider it as steps[0]
    steps_2=1  # Consider it as steps[1]
    steps_3=steps_2+steps_1 # Consider it as steps[2]
    for i in range(3,n+1):
        steps=steps_1+steps_2+steps_3
        #Swapping variables , to get the last three states
        steps_3,steps_2,steps_1=steps,steps_3,steps_2
    return steps


#Driver of the code
n=int(input())
print(triple_step(n))
