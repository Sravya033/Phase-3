#find the max element in the list
def find_max(result,i,n,num):
    if i>=n:
        print(result)
        return 
    result=max(result,num[i])
    find_max(result,i+1,n,num)
num=[200,30,10,15]
result=num[0]
n=len(num)
i=0
find_max(result,i,n,num)

def find_max2(index,n,nums):
    if index==n:
        return 0
    nextElement=find_max2(index+1,n,nums)
    return max(nextElement,nums[index])


nums=[20,30,10,15,60,70]
n=len(num)
result=find_max2(0,n,nums)
print("max element is",result)