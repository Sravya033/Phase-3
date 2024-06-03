#find the min element in the list
def find_min(result,i,n,num):
    if i>=n:
        print(result)
        return 
    result=min(result,num[i])
    find_min(result,i+1,n,num)


num=[200,30,10,15]
result=num[0]
n=len(num)
i=0
find_min(result,i,n,num)

def find_min2(index,n,nums):
    if index==n:
        return nums[0]
    return min(nums[index],find_min2(index+1,n,nums))


nums=[20,3,109,150,600,700]
n=len(nums)
print(find_min2(0,n,nums))
