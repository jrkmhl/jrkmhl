class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        res = []
        while i<n-2:
            if i==0 or (nums[i]!=nums[i-1]):
                j=i+1
                k=n-1

                while j<k :
                    sm = nums[i]+nums[j]+nums[k]
                    if sm==0:
                        res.append([nums[i],nums[j],nums[k]])
                        while j<k and nums[j]==nums[j+1]:
                            j +=1
                        while j <k and nums[k]==nums[k-1]:
                            k -=1
                        j +=1
                        k -=1
                    elif sm < 0:
                        j +=1
                    else:
                        k -=1
                i +=1
            else:
                i +=1