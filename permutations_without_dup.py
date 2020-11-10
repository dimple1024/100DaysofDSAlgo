#Cracking the coding interview , ques 8.7
#Time complexity : O(n!)
#Space Complexity : O(N)
def permuations(string, rem_string,result):
    if len(rem_string)==0:
        result.append(string)
    else:
        for i in range(len(rem_string)):
            new_string=string+rem_string[i]
            new_rem_string=rem_string[:i]+rem_string[i+1:]
            permuations(new_string,new_rem_string,result)


string=input()
result=[]
permuations("",string,result)
print("Total number of permuations:"+str(result))
print("Permutations:\n")
print(result)