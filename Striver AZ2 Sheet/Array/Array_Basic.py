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

