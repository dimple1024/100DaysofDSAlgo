#Cracking the coding interview , ques 8.8
#Time complexity : O(2**n)
#Space Complexity : O(N)
def generate_parentheses(n,string,left,right,result):
    if left>n:
        return
    if right > left:
        return
    if left == n and right == n:
        result.append(string)
        return
    generate_parentheses(n,string+"(",left+1,right,result)
    generate_parentheses(n,string+")",left,right+1,result)

n=int(input())
result=[]
generate_parentheses(n,"",0,0,result)
print(result)



