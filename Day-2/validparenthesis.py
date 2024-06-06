def validparenthesis(result,n,openOnes,closedOnes):
    if closedOnes>openOnes:
        return 
    if openOnes>n//2 or closedOnes>n//2:
        return
    if len(result)==n:
        print(result)
        return
    validparenthesis(result+"(",n,openOnes+1,closedOnes)
    validparenthesis(result+")",n,openOnes,closedOnes+1)
n=8
result=""
validparenthesis(result,n,0,0)