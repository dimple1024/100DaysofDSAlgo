#Cracking the Coding Interview , ques 8.8
from collections import defaultdict
def permutation_with_dup(hashmap,len_string,temp_string,result):
    if len(temp_string)==len_string:
        result.append(temp_string)
    else:
        for i in hashmap:
            if hashmap[i]>0:
                new_temp_string=temp_string+i
                new_hashmap=hashmap.copy()
                new_hashmap[i]-=1
                permutation_with_dup(new_hashmap,len_string,new_temp_string,result)


string=input()
hashmap=defaultdict(int)

for i in string:
    hashmap[i]+=1
result=[]
permutation_with_dup(hashmap,len(string),"",result)
print(result)