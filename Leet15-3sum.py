'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []  #to store the triplets
        nums.sort()
        
        lenght = len(nums)
        
        for i in range(lenght-2):
            '''
            Thinking about why '-2' we are using left and right pointers for each iteration.
            theose two pointers are removed from the lenght of iteration.
            '''
            #dealing with edge cases
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1 , lenght -1 #l->left , r->right
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                
                if total <0:
                    #our sorted num left side is full of negative so moving it right(increasing thr index)
                    l=l+1
                elif total > 0:
                    #our sorted num right side is full of positive so moving it left(decreasing thr index)
                    r =r-1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l] == nums[l+1] :
                        l = l+1
                    while l>r and nums[r] == nums[r-1]:
                        r = r-1
                    l = l+1
                    r = r-1
        return ans
         
        
