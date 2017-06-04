class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length=len(nums)
        index=[]
        for i in range(length):
            index.append(i)
        total=[]
        for i in range(length):
            total.append((nums[i],index[i]))
        total.sort(key=lambda x:x[0])
        i=0
        j=length-1
        while(i!=j):
            if(total[i][0]+total[j][0]>target):
                j=j-1
            if(total[i][0]+total[j][0]<target):
                i=i+1
            if(total[i][0]+total[j][0]==target):
                if(i!=j):
                    return [total[i][1],total[j][1]]
test=Solution()
print(test.twoSum([3,2,4],6))