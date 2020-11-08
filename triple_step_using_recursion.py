
#Cracking the coding Interview , ques 8.1

#Top down approach,
def triple_step(n):
    if n<0:
        return 0
    elif n<=1:
        return 1
    else:
        # the last step can be made from either n-1 , n-2 or n-3
        return triple_step(n-1)+triple_step(n-2)+triple_step(n-3)


