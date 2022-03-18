def chk_ISBN(isbn : str) -> bool:
    sum=0
    for i,n in enumerate(isbn[:-1]):
        if i%2==1:
            sum+=int(n)*3
        else:
            sum+=int(n)
            
    code=sum%10
    
    if code!=0:
        code=10-code
        
    # if code==int(isbn[-1]):
    #     return True
    # else:
    #     return False
    return code==int(isbn[-1])
    



#print(chk_ISBN("9788997924271"))

