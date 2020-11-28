
def parenetheses(n,string,left,right,result):
        if left==n and right==n:
            temp=''.join(string)
            result.append(temp)
            return
        if left < n:
            new_string=string.copy()
            new_string.append("(")
            parenetheses(n,new_string,left+1,right,result)
        if right < left:
            new_string=string.copy()
            new_string.append(")")
            parenetheses(n,new_string,left,right+1,result)

n=int(input())
result=[]
parenetheses(n,[],0,0,result)
print(result)
