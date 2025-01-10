class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution = []
        flag = None
        for i in range(0,len(nums)-1):
            for j in range(i,len(nums)-1):
                sum =nums[i] + nums[j+1]

                if sum == target:
                    solution.append(i)
                    solution.append(j+1)
                    flag = 1
                    break
            if flag:
                break

        return solution
