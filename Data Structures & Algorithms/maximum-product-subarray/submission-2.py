class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 2,-4,5,-8,9,-4,6
        # 2,-4,1,-1,1,-1,1
        # 0,
        # 4,5,2

        subarrays = []
        subarray = []
        for num in nums:
            if num == 0:
                subarrays.append(subarray)
                subarray = []
            else:
                subarray.append(num)
        subarrays.append(subarray)

        # even number of -ve elements is great 
        products = []
        if 0 in nums: products.append(0)
        for subarray in subarrays:
            if self.hasEvenN(subarray):
                products.append(self.product(subarray))
            else:
                products.append(self.bestProduct(subarray))
        
        return max(products)

            

    def hasEvenN(self, array) -> bool:
        isEven = True
        for num in array:
            if num <0:
                isEven = not isEven
        return isEven

    def product(self, array) -> int:
        if not array:
            return float("-inf")
        res = 1
        for num in array:
            res *= num
        return res

    def bestProduct(self, array) -> int:
        if len(array) == 1:
            return array[0]
        # has an odd number of -ves

        # left- most negative
        lNegIndex = 0
        for i in range(len(array)):
            if array[i] < 0:
                lNegIndex = i
                break
        
        # right most
        rNegIndex = 0
        for i in range(len(array)-1, -1, -1):
            if array[i] < 0:
                rNegIndex = i
                break
        
        if rNegIndex == lNegIndex: # only one neg
            return max(self.product(array[:lNegIndex]), self.product(array[lNegIndex+1:]))
            
        # four cases:
        return max(self.product(array[:lNegIndex]), self.product(array[lNegIndex+1:]), self.product(array[rNegIndex+1:]), self.product(array[:rNegIndex]))










        