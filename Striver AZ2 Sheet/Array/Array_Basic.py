''' Q: Longest Subarray with given sum K'''

# # Brute Force Approach - O(n^2) and O(1) space complexity

# arr=[94 ,-33 ,-13 ,40 ,-82, 94, -33, -13, 40, -82]
# k=52
# n=len(arr)
# max_len=0
# for i in range(0,n):
#     s=0
#     for j in range(i,n):
#         s+=arr[j]
#         if (s==k):
#             max_len=max(max_len,j-i+1)
        
# print(max_len)

# # Better Approach using Hash Map and Prefix Sum - O(nlogn) for ordered map and O(n) and O(n2) for unordered in best and worst , space complexity O(n)

# prefix_sum = {}
# sum=0
# maxlen=0
# for i in range(n):
#     sum+=arr[i]
#     if sum==k:
#         maxlen=max(maxlen,i+1)

#     rem=sum-k
#     if(rem in prefix_sum):
#         len=i- prefix_sum[rem]
#         maxlen=max(maxlen,len)

#     if sum not in prefix_sum:
#         prefix_sum[sum]=i

# print(maxlen)

# # Optimal Approach using Two Pointers - O(n) time and O(1) space complexity -- Only for Positive Arrays

# left, right=0,0
# maxlen=0
# sum=arr[0]

# while right<n:
    
#     while left<=right and sum>k:
#         sum-=arr[left]
#         left+=1
    
#     if sum==k:
#         maxlen=max(maxlen,right-left+1)
    
#     right+=1
#     if right <n:
#         sum+=arr[right]
        
# print(maxlen)

''' Q: Two Sum'''

# Brute Force Approach - O(n^2) time and O(1) space complexity

arr = [2,6,5,8,8,11]
target = 13

def two_sum_brute1(arr,target):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]+arr[j]==target):
                return True
    return False

def two_sum_brute2(arr,target):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if(arr[i]+arr[j]==target):
                return [i,j]
    return [-1,-1]

def two_sum_better1(arr, target):
    hashmap={}
    for i in range(len(arr)):
        complement=target-arr[i]
        if complement in hashmap:
            return [hashmap[complement],i]
        else:
            hashmap[arr[i]]=i
    return [-1,-1]


def two_sum_optimal(arr,target):

    l=0
    r=len(arr)-1
    arr.sort()
    li=[]
    while l<r:
        sum=arr[r]+arr[l]
        if sum==target:
            return [l,r]
        elif sum <target:
            l+=1
        else:
            r-=1
    if not li:
        return [-1,-1]
    else:
        return li

# We cannot use the element at a given index twice.Hence a freq dic to keep tab of freq of elements.
def twoSum(arr, target, n):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    result = []
    for i in range(n):
        num = arr[i]
        complement = target - num

        # Check if both numbers are available
        if freq.get(num, 0) > 0 and freq.get(complement, 0) > 0:
            if num == complement:
                if freq[num] > 1:
                    result.append([num, num])
                    freq[num] -= 2
            else:
                result.append([num, complement])
                freq[num] -= 1
                freq[complement] -= 1

    if not result:
        return [[-1, -1]]
    return result

# flag=two_sum_brute1(arr,target)
# flag2=two_sum_brute2(arr,target)
# print(flag2)
            
# flag3=two_sum_better1(arr,target)
# print(flag3)
# flag4=two_sum_optimal(arr,target)
# print(flag4)
flag5=twoSum([1 ,-1 ,-1, 2, 2],1,5)

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

printAns(flag5)

print(flag5)
# Better Approach (Hashning) - O(n^2) time and O(1) space complexity