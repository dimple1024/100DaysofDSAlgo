def coins_problem(temp_arr,coins,rem_amount,min_coins):
    if rem_amount==0:
        return len(temp_arr.copy())
    for i in range(len(coins)):
        if len(temp_arr)>0:
            last_coin=temp_arr[len(temp_arr)-1]
            if coins[i]<last_coin:
                continue
        if coins[i]<=rem_amount:
            new_arr=temp_arr.copy()
            new_arr.append(coins[i])
            min_coins=min(coins_problem(new_arr,coins,rem_amount-coins[i],min_coins),min_coins)

    return min_coins


N=int(input("Enter number of coins: "))
amount=int(input("Enter the amount :"))
coins=[0]*N
for i in range(N):
    coins[i]=int(input())

print("Minimum number of coins required are:",coins_problem([],coins,amount,amount+1))
