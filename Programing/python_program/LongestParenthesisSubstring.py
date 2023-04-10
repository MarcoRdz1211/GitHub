def longest_paranthesised_substring(paranthesis):
    contador,ans = 0,0
    
    for i in paranthesis:
        if i=="(":
            contador += 1
        else:
            contador -= 1
            
        if contador>=0:
            ans += 1            


    if ans==0:
        return -1

    else:
        return ans
    
paranthesis = input()
answer = longest_paranthesised_substring(paranthesis)
print(answer)
