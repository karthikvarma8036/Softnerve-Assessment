def subsetXORSum(nums):
               def calculateXOR(nums, index, currentXOR):
                            if index == len(nums):
                                     return currentXOR

    
                            includeXOR = calculateXOR(nums, index + 1, currentXOR ^ nums[index])

    
                            excludeXOR = calculateXOR(nums, index + 1, currentXOR)

                            return includeXOR + excludeXOR

              return calculateXOR(nums, 0, 0)
nums = [5,1,6]
result = subsetXORSum(nums)
print(result)
